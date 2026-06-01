# Copyright (c) 2025 Adam Karpierz
# SPDX-License-Identifier: Zlib

__all__ = ('docs_on_gh_pages',)

from ..util import *

def docs_on_gh_pages(session: nox.Session, *,
                     html_dir: Path | str = "build/docs/html") -> None:
    # Publish documentation on GitHub Pages
    root = session.root_dir
    html_dir = root/html_dir
    # checkout gh-pages worktree
    env_dir = Path(session.virtualenv.location)
    gh_pages_dir = env_dir/"gh-pages"
    rmtree(gh_pages_dir)
    session.git("worktree", "prune")
    # session.git("worktree", "add", gh_pages_dir, "gh-pages")
    session.git("worktree", "add", "-B", "gh-pages", gh_pages_dir)
    # clean old docs
    (gh_pages_dir/".nojekyll").touch()
    for fpath in gh_pages_dir.iterdir():
        if fpath.name not in (".git",".nojekyll"):
            if fpath.is_dir():
                rmtree(fpath)
            else:
                fpath.unlink(missing_ok=True)
    # copy new docs
    copytree(html_dir, gh_pages_dir, dirs_exist_ok=True)
    # commit + push
    session.git("-C", gh_pages_dir, "add", ".")
    session.git("-C", gh_pages_dir, "commit", "-m", "Update documentation")
    session.git("-C", gh_pages_dir, "push", "--force", "origin", "gh-pages")
    # remove worktree
    session.git("worktree", "remove", "--force", gh_pages_dir)
    rmtree(gh_pages_dir)
    session.git("worktree", "prune")
