# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `backdoor.py` (score: 0.90)
- `loader.cpp` (score: 0.20)
- `loader.py` (score: 0.10)
- `app.py` (score: 0.00)
- `install.sh` (score: 0.00)
- `pysintaller.sh` (score: 0.00)

## Hotspots (complexity + centrality)

- `backdoor.py` -- complexity: 1.0, centrality: 1.0, combined: 1.0
- `loader.cpp` -- complexity: 0.2, centrality: 1.0, combined: 0.7
- `loader.py` -- complexity: 0.1, centrality: 0.5, combined: 0.3
- `app.py` -- complexity: 0.0, centrality: 0.0, combined: 0.0
- `install.sh` -- complexity: 0.0, centrality: 0.0, combined: 0.0
- `pysintaller.sh` -- complexity: 0.0, centrality: 0.0, combined: 0.0

## Dataflow Issues (INFERRED, review each lead)

- `backdoor.py:28` `__init__` [UNCHECKED_ALLOC] `s`: Result of allocator stored in `s` is never checked against NULL.
- `loader.cpp:19` `main` [DEAD_STORE] `size`: `size` assigned at line 19 but never read afterwards.
