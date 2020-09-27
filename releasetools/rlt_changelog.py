#!/usr/bin/env python3
"""
Print the changes between the released version and now
"""
import argparse
import sys

from subprocess import run

from releasetools.app import App
from releasetools import tagtools


def app_main(app, args):
    tag = tagtools.get_release_tag()
    git_log_options = app.config["changelog"]["git_log_options"]
    run(["git", "log", git_log_options, f"{tag}..HEAD"])

    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.description = __doc__

    app = App(parser)
    return app.run(app_main)


if __name__ == "__main__":
    sys.exit(main())
# vi: ts=4 sw=4 et
