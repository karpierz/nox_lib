# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

# Helpers & Utils

__all__ = ('nox', 'nox_ext', 'Path', 'copytree', 'rmtree')

from pathlib import Path
from functools import partial
import shutil

import nox
import nox_ext

copytree = shutil.copytree
rmtree   = partial(shutil.rmtree, ignore_errors=True)
