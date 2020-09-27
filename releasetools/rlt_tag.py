#!/usr/bin/env python3
"""
Manipulate the project released and next versions
"""
import argparse
import sys

from releasetools.app import App
from releasetools import tagtools, versiontools


def app_main(app, args):
    next_version = versiontools.read(app)
    tagtools.create_tag(app, next_version)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.description = __doc__

    app = App(parser)
    return app.run(app_main)


if __name__ == "__main__":
    sys.exit(main())
# vi: ts=4 sw=4 et
