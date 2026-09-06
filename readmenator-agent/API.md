# API

## backdoor.py

### generar_archivo_pth `def generar_archivo_pth(host, port, ruta_salida)`
- Defined: `backdoor.py:51`
- Doc: Crea el objeto backdoor y lo guarda mediante torch.save.

### generar_loader_python `def generar_loader_python(ruta_pth, ruta_loader)`
- Defined: `backdoor.py:59`
- Doc: Genera un script Python que carga el .pth en memoria.

### generar_loader_cpp `def generar_loader_cpp(ruta_pth, ruta_cpp)`
- Defined: `backdoor.py:97`
- Doc: Versión conceptual en C++ utilizando libtorch.

### modo_interactivo `def modo_interactivo()`
- Defined: `backdoor.py:134`
- Doc: Solicita los parámetros al usuario en la consola.

### parsear_argumentos `def parsear_argumentos()`
- Defined: `backdoor.py:156`
- Doc: Configura argparse.

### main `def main()`
- Defined: `backdoor.py:184`

### __init__ `def __init__(self, host, port)`
- Defined: `backdoor.py:23`

### __reduce__ `def __reduce__(self)`
- Defined: `backdoor.py:38`
- Doc: El método __reduce__ debe retornar una tupla (callable, args).

## loader.cpp

### main `int main()`
- Defined: `loader.cpp:8`
- Doc: loader_fixed.cpp - Carga .pth usando torch::pickle_load para evitar jit::load include <torch/torch.h> include <c10/core/

## loader.py

### main `def main()`
- Defined: `loader.py:8`
