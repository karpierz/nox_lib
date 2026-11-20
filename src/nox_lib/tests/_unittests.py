# flake8-in-file-ignores: noqa: F403,F405

# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

from __future__ import annotations

__all__ = ('unittests',)

from ..util import *


def unittests(session: nox_ext.Session, *,
              tests_module: str = "tests") -> None:
    session.py("--version")
    session.py("-m", tests_module, *session.posargs)
