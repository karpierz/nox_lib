# flake8-in-file-ignores: noqa: F403,F405

# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

from __future__ import annotations

__all__ = ('build', 'build_sdist', 'build_wheel', 'build_wheel_py', 'build_check')

from ..util import *


def build(session: nox_ext.Session, *,
          dist_dir: Path | str = "dist",
          ignore: list[str] = [],
          ignore_bad_ideas: list[str] = [],
          with_check: bool = True) -> None:
    root = session.root_dir
    dist_path = root/dist_dir
    check_args = ["--verbose"]
    if ignore:
        check_args += ["--ignore", ",".join(ignore)]
    if ignore_bad_ideas:
        check_args += ["--ignore-bad-ideas",
                       ",".join(ignore_bad_ideas)]
    session.py("-m", "check_manifest", *check_args)
    session.py("-m", "build")
    if with_check:
        # Verify distribution files
        session.py("-m", "twine", "check", dist_path/"*")


def build_sdist(session: nox_ext.Session, *,
                dist_dir: Path | str = "dist",
                ignore: list[str] = [],
                ignore_bad_ideas: list[str] = [],
                with_check: bool = True) -> None:
    root = session.root_dir
    dist_path = root/dist_dir
    check_args = ["--verbose"]
    if ignore:
        check_args += ["--ignore", ",".join(ignore)]
    if ignore_bad_ideas:
        check_args += ["--ignore-bad-ideas",
                       ",".join(ignore_bad_ideas)]
    session.py("-m", "check_manifest", *check_args)
    session.py("-m", "build", "--sdist")
    if with_check:
        # Verify distribution files
        session.py("-m", "twine", "check", dist_path/"*")


def build_wheel(session: nox_ext.Session, *,
                dist_dir: Path | str = "dist",
                ignore: list[str] = [],
                ignore_bad_ideas: list[str] = [],
                with_check: bool = True) -> None:
    root = session.root_dir
    dist_path = root/dist_dir
    check_args = ["--verbose"]
    if ignore:
        check_args += ["--ignore", ",".join(ignore)]
    if ignore_bad_ideas:
        check_args += ["--ignore-bad-ideas",
                       ",".join(ignore_bad_ideas)]
    session.py("-m", "check_manifest", *check_args)
    session.py("-m", "build", "--wheel")
    if with_check:
        # Verify distribution files
        session.py("-m", "twine", "check", dist_path/"*")


def build_wheel_py(session: nox_ext.Session, *,
                   dist_dir: Path | str = "dist",
                   with_pyc_wheel: bool = False) -> None:
    root = session.root_dir
    dist_path = root/dist_dir
    session.py("--version")
    session.py("-m", "build", "--wheel")
    if with_pyc_wheel:
        pkg_fullname = session.package_data.FULLNAME
        session.py("-m", "pyc_wheel", "--quiet",
                   dist_path/f"{pkg_fullname}-{session.PKG_IMPL}{session.PKG_PVER}-*.whl")


def build_check(session: nox_ext.Session, *,
                dist_dir: Path | str = "dist",
                ignore: list[str] = [],
                ignore_bad_ideas: list[str] = []) -> None:
    root = session.root_dir
    dist_path = root/dist_dir
    check_args = ["--verbose"]
    if ignore:
        check_args += ["--ignore", ",".join(ignore)]
    if ignore_bad_ideas:
        check_args += ["--ignore-bad-ideas",
                       ",".join(ignore_bad_ideas)]
    session.py("-m", "check_manifest", *check_args)
    # Verify distribution files
    session.py("-m", "twine", "check", dist_path/"*")
