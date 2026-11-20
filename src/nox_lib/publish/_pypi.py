# flake8-in-file-ignores: noqa: F403,F405

# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

from __future__ import annotations

__all__ = ('on_pypi',)

from ..util import *


def on_pypi(session: nox_ext.Session, *,
            dist_dir: Path | str = "dist") -> None:
    # Publish on PyPI
    root = session.root_dir
    dist_path = root/dist_dir
    session.py("-m", "twine", "upload", dist_path/"*")
