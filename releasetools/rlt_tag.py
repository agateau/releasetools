#!/usr/bin/env python3
"""
Manipulate the project released and next versions
"""
import argparse
import sys

from releasetools import tagtools, versiontools
from releasetools.app import App
from releasetools.errors import ReleaseToolsError


def app_main(app, args):
    next_version = versiontools.read(app)
    main_branch = app.config["git"]["main_branch"]
    if app.repo.active_branch.name != main_branch:
        raise ReleaseToolsError(f"Tag must be created on the '{main_branch}' branch")
    tag = tagtools.create_tag(app, next_version)
    print(f"Created tag {tag}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.description = __doc__

    app = App(parser)
    return app.run(app_main, argv)


if __name__ == "__main__":
    sys.exit(main())
# vi: ts=4 sw=4 et
