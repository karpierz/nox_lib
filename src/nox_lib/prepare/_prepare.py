# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

__all__ = ('prep_cmd',)

from ..util import *

def prep_cmd(session: nox.Session, *,
             prep_cmd: str = ".aprep.cmd") -> None:
    root = session.root_dir
    cmd = root/prep_cmd
    if cmd.is_file(): session.run(cmd, external=True)
