# flake8-in-file-ignores: noqa: F403,F405

# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

from __future__ import annotations

__all__ = ('prep_cmd',)

from ..util import *


def prep_cmd(session: nox_ext.Session, *,
             prep_cmd: str = ".aprep.cmd") -> None:
    root = session.root_dir
    cmd = root/prep_cmd
    if cmd.is_file(): session.run(cmd, external=True)
