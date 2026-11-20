# flake8-in-file-ignores: noqa: F403,F405

# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

from __future__ import annotations

__all__ = ('flake8',)

from ..util import *


def flake8(session: nox_ext.Session, *,
           src_dir: Path | str = "src") -> None:
    root = session.root_dir
    src_dir = root/src_dir
    env_dir = Path(session.virtualenv.location)
    out_file = env_dir/"flake8out.txt"
    out_file.unlink(missing_ok=True)
    session.py("-m", "flake8", "--color", "never",
               "--output-file", out_file, f"{src_dir}/")
