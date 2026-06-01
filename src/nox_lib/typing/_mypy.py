# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

__all__ = ('mypy',)

from ..util import *

def mypy(session: nox.Session) -> None:
    session.py("-m", "mypy")
