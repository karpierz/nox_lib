# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

__all__ = ('coverage',)

from ..util import *

def coverage(session: nox.Session, *,
             tests_module: str = "tests") -> None:
    env_dir = Path(session.virtualenv.location)
    data_file = env_dir/".coverage"
    html_dir  = env_dir/".coverage_html"
    session.py("-m", "coverage", "erase", f"--data-file={data_file}")
    session.py("-m", "coverage", "run",   f"--data-file={data_file}", "-m", tests_module,
               *session.posargs, success_codes=range(0, 256))
    session.py("-m", "coverage", "html",  f"--data-file={data_file}", f"--directory={html_dir}",
               success_codes=range(0, 256))
    session.py("-m", "coverage", "report", f"--data-file={data_file}")
