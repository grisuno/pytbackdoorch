# Concepts

Second-brain semantic layer: nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

| Concept | Files | Mentions | Top Files |
|---------|-------|----------|-----------|
| `pth` | 3 | 10 | `backdoor.py`, `loader.cpp`, `loader.py` |
| `para` | 3 | 9 | `backdoor.py`, `loader.cpp`, `loader.py` |
| `loader` | 3 | 8 | `backdoor.py`, `loader.cpp`, `loader.py` |
| `carga` | 3 | 3 | `backdoor.py`, `loader.cpp`, `loader.py` |
| `backdoor` | 2 | 6 | `backdoor.py`, `loader.py` |
| `torch` | 2 | 5 | `backdoor.py`, `loader.cpp` |
| `cpp` | 2 | 4 | `backdoor.py`, `loader.cpp` |
| `load` | 2 | 4 | `backdoor.py`, `loader.cpp` |
| `archivo` | 2 | 3 | `backdoor.py`, `loader.py` |
| `ejecuta` | 2 | 3 | `backdoor.py`, `loader.py` |
| `pickle` | 2 | 2 | `backdoor.py`, `loader.cpp` |
| `script` | 2 | 2 | `backdoor.py`, `loader.py` |

## Dialectic Prompts

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
