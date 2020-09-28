#!/usr/bin/env python3
"""
Update the work branch
"""
import argparse
import sys

from subprocess import run

from releasetools.app import App


def app_main(app, args):
    git_cfg = app.config["git"]

    run(["git", "checkout", git_cfg["work_branch"]])
    run(["git", "pull"])
    work_branch = git_cfg["work_branch"]
    run(["git", "merge", f"origin/{work_branch}"])
    run(["git", "status"])
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.description = __doc__

    app = App(parser)
    return app.run(app_main)


if __name__ == "__main__":
    sys.exit(main())
# vi: ts=4 sw=4 et
