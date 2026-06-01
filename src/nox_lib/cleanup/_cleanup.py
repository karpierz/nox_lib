# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

__all__ = ('clean_cmd', 'cleanup')

from ..util import *

def clean_cmd(session: nox.Session, *,
              clean_cmd: str = ".clean.cmd") -> None:
    # no_package = true
    root = session.root_dir
    cmd = root/clean_cmd
    if cmd.is_file():
        session.run(cmd, stderr=subprocess.DEVNULL, external=True)

def cleanup(session: nox.Session, *,
            build_dir: Path | str = "build",
            dist_dir:  Path | str = "dist",
            src_dir:   Path | str = "src") -> None:
    root = session.root_dir
    rmtree(root/build_dir)
    rmtree(root/dist_dir)
    for item in root.glob(f"{src_dir}/*.egg-info"): rmtree(item)
    for item in root.glob("**/__pycache__"): rmtree(item)
    for item in root.glob("**/.mypy_cache"): rmtree(item)
    rmtree(root/".tox")
    rmtree(root/".nox")
