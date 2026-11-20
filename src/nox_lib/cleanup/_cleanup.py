# flake8-in-file-ignores: noqa: F403,F405

# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

from __future__ import annotations

__all__ = ('clean_cmd', 'cleanup')

import subprocess

from ..util import *


def clean_cmd(session: nox_ext.Session, *,
              clean_cmd: str = ".clean.cmd") -> None:
    # no_package = true
    root = session.root_dir
    cmd = root/clean_cmd
    if cmd.is_file():
        session.run(cmd, stderr=subprocess.DEVNULL, external=True)


def cleanup(session: nox_ext.Session, *,
            build_dir: Path | str = "build",
            dist_dir:  Path | str = "dist",
            src_dir:   Path | str = "src") -> None:
    root = session.root_dir
    rmtree(root/build_dir)
    rmtree(root/dist_dir)
    for item in root.glob(f"{src_dir}/*.egg-info"): rmtree(item)
    for item in root.rglob("__pycache__"): rmtree(item)
    for item in root.rglob(".mypy_cache"): rmtree(item)
    rmtree(root/".tox")
    rmtree(root/".nox")
