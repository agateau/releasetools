#!/usr/bin/env python3
"""
Update the work branch
"""
import argparse
import sys

from releasetools.app import App
from releasetools.errors import ReleaseToolsError


def app_main(app, args):
    git_cfg = app.config["git"]
    work_branch = git_cfg["work_branch"]
    main_branch = git_cfg["main_branch"]

    if app.repo.is_dirty():
        raise ReleaseToolsError("Working tree contains changes")

    if app.repo.untracked_files:
        files = ", ".join(app.repo.untracked_files)
        raise ReleaseToolsError(f"Working tree contains untracked files ({files})")

    print(f"Switching to {work_branch} and updating it...")
    app.repo.heads[work_branch].checkout()
    app.repo.git.pull()

    print(f"\nMerging {main_branch} in...")
    app.repo.git.merge(f"origin/{main_branch}")

    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.description = __doc__

    app = App(parser)
    return app.run(app_main)


if __name__ == "__main__":
    sys.exit(main())
# vi: ts=4 sw=4 et
