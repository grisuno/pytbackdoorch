#!/bin/bash

pyinstaller --onefile \  ─╯
--hidden-import torch \
  --hidden-import torch.serialization \
  --hidden-import torch._C \
  --hidden-import torch._C._cudnn \
  --hidden-import torch._C._nvtx \
  --collect-all torch \
  loader.py
