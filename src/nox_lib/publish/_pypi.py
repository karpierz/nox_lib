# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

__all__ = ('on_pypi',)

from ..util import *

def on_pypi(session: nox.Session, *,
            dist_dir: Path | str = "dist") -> None:
    # Publish on PyPI
    root = session.root_dir
    dist_dir = root/dist_dir
    session.py("-m", "twine", "upload", dist_dir/"*")
