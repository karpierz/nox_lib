# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

__all__ = ('flake8',)

from ..util import *

def flake8(session: nox.Session, *,
           src_dir: Path | str = "src") -> None:
    root = session.root_dir
    src_dir = root/src_dir
    env_dir = Path(session.virtualenv.location)
    out_file = env_dir/"flake8out.txt"
    session.py("-m", "flake8", "--color", "never",
               "--output-file", out_file, f"{src_dir}/")
