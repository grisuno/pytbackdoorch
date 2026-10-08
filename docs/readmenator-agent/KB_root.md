# Subsystem: root

## app.py
- Doc: Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación...
- Layer: utility
- Language: py

## backdoor.py
- Doc: PoC generador de backdoor en archivos .pth (PyTorch) Uso interactivo: python3 pth_builder.py Uso...
- Layer: utility
- Language: py
- Symbols:
  - `PytorchBackdoor` (class, line 17) `class PytorchBackdoor`
  - `generar_archivo_pth` (method, line 51) `def generar_archivo_pth(host, port, ruta_salida)`
  - `generar_loader_python` (method, line 59) `def generar_loader_python(ruta_pth, ruta_loader)`
  - `generar_loader_cpp` (method, line 97) `def generar_loader_cpp(ruta_pth, ruta_cpp)`
  - `modo_interactivo` (method, line 134) `def modo_interactivo()`
  - `parsear_argumentos` (method, line 156) `def parsear_argumentos()`
  - `main` (method, line 184) `def main()`
  - `__init__` (method, line 23) `def __init__(self, host, port)`
  - `__reduce__` (method, line 38) `def __reduce__(self)`

## install.sh
- Layer: utility
- Language: sh

## loader.cpp
- Doc: loader_fixed.cpp - Carga .pth usando torch::pickle_load para evitar jit::load
- Layer: utility
- Language: cpp
- Symbols:
  - `main` (function, line 9) `int main()`
  - `buffer` (function, line 21) `std::vector<char> buffer(size);`

## loader.py
- Doc: Carga el archivo .pth y ejecuta el backdoor (PoC) ADVERTENCIA: Este script es solo para entornos...
- Layer: utility
- Language: py
- Symbols:
  - `main` (function, line 8) `def main()`

## pysintaller.sh
- Layer: utility
- Language: sh
