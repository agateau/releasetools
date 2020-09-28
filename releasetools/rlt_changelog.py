#!/usr/bin/env python3
"""
Print the changes between the released version and now
"""
import argparse
import sys

from datetime import datetime
from subprocess import run

from releasetools.app import App
from releasetools import tagtools, versiontools


HEADER_TMPL = "## {version} - {date}\n"


def print_header(app):
    version = versiontools.read(app)
    date = datetime.now().strftime("%Y-%m-%d")
    print(HEADER_TMPL.format(version=version, date=date))


def print_changelog(tag, git_log_options):
    proc = run(["git", "log", git_log_options, f"{tag}..HEAD"],
               capture_output=True, text=True)
    print(str(proc.stdout))


def app_main(app, args):
    tag = tagtools.get_release_tag()
    git_log_options = app.config["changelog"]["git_log_options"]

    print_header(app)
    print_changelog(tag, git_log_options)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.description = __doc__

    app = App(parser)
    return app.run(app_main)


if __name__ == "__main__":
    sys.exit(main())
# vi: ts=4 sw=4 et
