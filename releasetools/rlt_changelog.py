#!/usr/bin/env python3
"""
Print the changes between the released version and now
"""
import argparse
import sys

from subprocess import run

from releasetools.app import App
from releasetools import tagtools


def print_changelog(tag, options):
    run(["git", "log", options, f"{tag}..HEAD"])


def main():
    parser = argparse.ArgumentParser()
    parser.description = __doc__
    parser.parse_args()

    app = App()
    tag = tagtools.get_release_tag()

    print_changelog(tag, app.config["changelog"]["git_log_options"])

    return 0


if __name__ == "__main__":
    sys.exit(main())
# vi: ts=4 sw=4 et
