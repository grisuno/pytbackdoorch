# API

## backdoor.py
- `PytorchBackdoor.__init__` (method) `backdoor.py:23` `def __init__(self, host, port)`
- `PytorchBackdoor.generar_archivo_pth` (method) `backdoor.py:51` `def generar_archivo_pth(host, port, ruta_salida)` -- Crea el objeto backdoor y lo guarda mediante torch.save.
- `PytorchBackdoor.generar_loader_python` (method) `backdoor.py:59` `def generar_loader_python(ruta_pth, ruta_loader)` -- Genera un script Python que carga el .pth en memoria.
- `PytorchBackdoor.generar_loader_cpp` (method) `backdoor.py:97` `def generar_loader_cpp(ruta_pth, ruta_cpp)` -- Versión conceptual en C++ utilizando libtorch.
- `PytorchBackdoor.modo_interactivo` (method) `backdoor.py:134` `def modo_interactivo()` -- Solicita los parámetros al usuario en la consola.
- `PytorchBackdoor.parsear_argumentos` (method) `backdoor.py:156` `def parsear_argumentos()` -- Configura argparse.
- `PytorchBackdoor.main` (method) `backdoor.py:184` `def main()`

## loader.cpp
- `main` (function) `loader.cpp:9` `int main()`
- `buffer` (function) `loader.cpp:21` `std::vector<char> buffer(size);`

## loader.py
- `main` (function) `loader.py:8` `def main()`
