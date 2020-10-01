#!/usr/bin/env python3
"""
Manipulate the project released and next versions
"""
import argparse
import sys

from releasetools.app import App
from releasetools import tagtools, versiontools


def app_main(app, args):
    if args.set_next:
        versiontools.write(app, args.set_next, dry_run=args.dry_run)
    elif args.next:
        print(versiontools.read(app))
    elif args.released:
        print(tagtools.get_released_version(app))

    return 0


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.description = __doc__

    parser.add_argument("--dry-run", action="store_true",
                        help="Print file to stdout instead of updating it")
    parser.add_argument("--released", action="store_true",
                        help="Get released version")
    parser.add_argument("--next", action="store_true",
                        help="Get next version")
    parser.add_argument("-s", "--set-next", help="Set version to VERSION",
                        metavar="VERSION")

    app = App(parser)
    return app.run(app_main, argv)


if __name__ == "__main__":
    sys.exit(main())
# vi: ts=4 sw=4 et
