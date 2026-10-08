# root

*Community 0 | 6 files | cohesion 1.00*

## Definition

This community groups 6 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `PytorchBackdoor`, `__init__`, `__reduce__`, `buffer`, `generar_archivo_pth`, `generar_loader_cpp`, `generar_loader_python`, `main`. Core file: `backdoor.py` (9 symbols). Documented purpose: Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licencia: GPL v3  Descripción:.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 0 | yes |
| `backdoor.py` | py | utility | 9 | yes |
| `install.sh` | sh | utility | 0 | no |
| `loader.cpp` | cpp | utility | 2 | yes |
| `loader.py` | py | utility | 1 | yes |
| `pysintaller.sh` | sh | utility | 0 | no |

## Key Symbols

- `PytorchBackdoor` (class, `backdoor.py:17`) `class PytorchBackdoor` - Esta clase se serializa en el archivo .pth.
- `__init__` (method, `backdoor.py:23`) `def __init__(self, host, port)`
- `__reduce__` (method, `backdoor.py:38`) `def __reduce__(self)` - El método __reduce__ debe retornar una tupla (callable, args).
- `generar_archivo_pth` (method, `backdoor.py:51`) `def generar_archivo_pth(host, port, ruta_salida)` - Crea el objeto backdoor y lo guarda mediante torch.save.
- `generar_loader_python` (method, `backdoor.py:59`) `def generar_loader_python(ruta_pth, ruta_loader)` - Genera un script Python que carga el .pth en memoria.
- `generar_loader_cpp` (method, `backdoor.py:97`) `def generar_loader_cpp(ruta_pth, ruta_cpp)` - Versión conceptual en C++ utilizando libtorch.
- `modo_interactivo` (method, `backdoor.py:134`) `def modo_interactivo()` - Solicita los parámetros al usuario en la consola.
- `parsear_argumentos` (method, `backdoor.py:156`) `def parsear_argumentos()` - Configura argparse.
- `main` (method, `backdoor.py:184`) `def main()`
- `main` (function, `loader.cpp:9`) `int main()`
- `buffer` (function, `loader.cpp:21`) `std::vector<char> buffer(size);`
- `main` (function, `loader.py:8`) `def main()`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- [dataflow UNCHECKED_ALLOC] `backdoor.py:28` `__init__` `s`: Result of allocator stored in `s` is never checked against NULL.
- [dataflow DEAD_STORE] `loader.cpp:19` `main` `size`: `size` assigned at line 19 but never read afterwards.

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `install.sh`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `app.py`
- `backdoor.py`
- `install.sh`
- `loader.cpp`
- `loader.py`
- `pysintaller.sh`
