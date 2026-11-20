# flake8-in-file-ignores: noqa: F403,F405

# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

from __future__ import annotations

__all__ = ('mypy',)

from ..util import *


def mypy(session: nox_ext.Session) -> None:
    session.py("-m", "mypy")
