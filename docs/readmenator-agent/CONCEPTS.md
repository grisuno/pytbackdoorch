# Concepts

Nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

- `pth` | files=3 | mentions=10 | `backdoor.py`, `loader.cpp`, `loader.py`
- `para` | files=3 | mentions=9 | `backdoor.py`, `loader.cpp`, `loader.py`
- `loader` | files=3 | mentions=8 | `backdoor.py`, `loader.cpp`, `loader.py`
- `carga` | files=3 | mentions=3 | `backdoor.py`, `loader.cpp`, `loader.py`
- `backdoor` | files=2 | mentions=6 | `backdoor.py`, `loader.py`
- `torch` | files=2 | mentions=5 | `backdoor.py`, `loader.cpp`
- `cpp` | files=2 | mentions=4 | `backdoor.py`, `loader.cpp`
- `load` | files=2 | mentions=4 | `backdoor.py`, `loader.cpp`
- `archivo` | files=2 | mentions=3 | `backdoor.py`, `loader.py`
- `ejecuta` | files=2 | mentions=3 | `backdoor.py`, `loader.py`
- `pickle` | files=2 | mentions=2 | `backdoor.py`, `loader.cpp`
- `script` | files=2 | mentions=2 | `backdoor.py`, `loader.py`

## Dialectic

- Thesis: `archivo` centralizes 2 files; Antithesis: `backdoor` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `archivo` centralizes 2 files; Antithesis: `carga` pulls 3 files with 2 shared (Jaccard 0.67); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `archivo` centralizes 2 files; Antithesis: `ejecuta` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `archivo` centralizes 2 files; Antithesis: `loader` pulls 3 files with 2 shared (Jaccard 0.67); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `archivo` centralizes 2 files; Antithesis: `para` pulls 3 files with 2 shared (Jaccard 0.67); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `archivo` centralizes 2 files; Antithesis: `pth` pulls 3 files with 2 shared (Jaccard 0.67); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `archivo` centralizes 2 files; Antithesis: `script` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `backdoor` centralizes 2 files; Antithesis: `carga` pulls 3 files with 2 shared (Jaccard 0.67); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `backdoor` centralizes 2 files; Antithesis: `ejecuta` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `backdoor` centralizes 2 files; Antithesis: `loader` pulls 3 files with 2 shared (Jaccard 0.67); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
