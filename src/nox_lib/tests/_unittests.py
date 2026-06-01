# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

__all__ = ('unittests',)

from ..util import *

def unittests(session: nox.Session, *,
              tests_module: str = "tests") -> None:
    session.py("--version")
    session.py("-m", tests_module, *session.posargs)
