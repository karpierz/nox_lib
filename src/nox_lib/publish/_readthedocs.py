# flake8-in-file-ignores: noqa: F403,F405

# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

from __future__ import annotations

__all__ = ('docs_on_readthedocs',)

from ..util import *


def docs_on_readthedocs(session: nox_ext.Session, *,
                        html_dir: Path | str = "build/docs/html") -> None:
    # Publish documentation on Read the Docs
    root = session.root_dir
    html_dir = root/html_dir
