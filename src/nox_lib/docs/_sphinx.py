# flake8-in-file-ignores: noqa: F403,F405

# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

from __future__ import annotations

__all__ = ('sphinx',)

from ..util import *


def sphinx(session: nox_ext.Session, *,
           docs_dir: Path | str = "docs",
           html_dir: Path | str = "build/docs/html",
           with_doctests: bool = True,
           links_check:   bool = True) -> None:
    root = session.root_dir
    docs_dir = root/docs_dir
    html_dir = root/html_dir
    session.py("-m", "sphinxlint", "-i", "#", "-i", "#arch", "-i", ".nox", "-i", ".tox",
                                   "-i", "build", "-i", "dist", "-i", ".mypy_cache")
    # session.py("-m", "sphinx.apidoc", "-f", *[session.site_packages/f"{item}/"
    #                                           for item in PKG.TOP_LEVELS])
    session.py("-m", "sphinx.cmd.build", "-W", "-a", "-b", "html", "-E", docs_dir, html_dir)
    if with_doctests:
        session.py("-m", "sphinx.cmd.build", "-W", "-a", "-b", "doctest", docs_dir, html_dir)
    if links_check:
        session.py("-m", "sphinx.cmd.build", "-W", "-a", "-b", "linkcheck", docs_dir, html_dir)
