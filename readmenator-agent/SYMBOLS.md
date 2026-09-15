# Symbols

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `PytorchBackdoor` | class | `backdoor.py:17` | `class PytorchBackdoor` |
| `__init__` | method | `backdoor.py:23` | `def __init__(self, host, port)` |
| `__reduce__` | method | `backdoor.py:38` | `def __reduce__(self)` |
| `generar_archivo_pth` | method | `backdoor.py:51` | `def generar_archivo_pth(host, port, ruta_salida)` |
| `generar_loader_cpp` | method | `backdoor.py:97` | `def generar_loader_cpp(ruta_pth, ruta_cpp)` |
| `generar_loader_python` | method | `backdoor.py:59` | `def generar_loader_python(ruta_pth, ruta_loader)` |
| `main` | method | `backdoor.py:184` | `def main()` |
| `modo_interactivo` | method | `backdoor.py:134` | `def modo_interactivo()` |
| `parsear_argumentos` | method | `backdoor.py:156` | `def parsear_argumentos()` |
| `buffer` | function | `loader.cpp:21` | `std::vector<char> buffer(size);` |
| `file` | function | `loader.cpp:13` | `std::ifstream file("backdoor.pth", std::ios::binary);` |
| `main` | function | `loader.cpp:8` | `int main()` |
| `sleep_for` | function | `loader.cpp:37` | `std::this_thread::sleep_for(std::chrono::minutes(1));` |
| `main` | function | `loader.py:8` | `def main()` |
