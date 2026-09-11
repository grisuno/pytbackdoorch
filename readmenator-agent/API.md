# API

## backdoor.py

### generar_archivo_pth (method) `def generar_archivo_pth(host, port, ruta_salida)`
- Defined: `backdoor.py:51`
- Doc: Crea el objeto backdoor y lo guarda mediante torch.save.

### generar_loader_python (method) `def generar_loader_python(ruta_pth, ruta_loader)`
- Defined: `backdoor.py:59`
- Doc: Genera un script Python que carga el .pth en memoria.

### generar_loader_cpp (method) `def generar_loader_cpp(ruta_pth, ruta_cpp)`
- Defined: `backdoor.py:97`
- Doc: Versión conceptual en C++ utilizando libtorch.

### modo_interactivo (method) `def modo_interactivo()`
- Defined: `backdoor.py:134`
- Doc: Solicita los parámetros al usuario en la consola.

### parsear_argumentos (method) `def parsear_argumentos()`
- Defined: `backdoor.py:156`
- Doc: Configura argparse.

### main (method) `def main()`
- Defined: `backdoor.py:184`

### __init__ (method) `def __init__(self, host, port)`
- Defined: `backdoor.py:23`

### __reduce__ (method) `def __reduce__(self)`
- Defined: `backdoor.py:38`
- Doc: El método __reduce__ debe retornar una tupla (callable, args).

## loader.cpp

### main (function) `int main()`
- Defined: `loader.cpp:8`
- Doc: loader_fixed.cpp - Carga .pth usando torch::pickle_load para evitar jit::load include <torch/torch.h> include <c10/core/

### file (function) `std::ifstream file("backdoor.pth", std::ios::binary);`
- Defined: `loader.cpp:13`
- Doc: Leer el archivo .pth como un buffer de bytes

### buffer (function) `std::vector<char> buffer(size);`
- Defined: `loader.cpp:21`

### sleep_for (function) `std::this_thread::sleep_for(std::chrono::minutes(1));`
- Defined: `loader.cpp:37`

## loader.py

### main (function) `def main()`
- Defined: `loader.py:8`
