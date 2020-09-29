import os
import sys

from pathlib import Path

from git import Repo

from releasetools.errors import ReleaseToolsError


DEFAULT_CONFIG = {
    "version": {
        "file": "CMakeLists.txt",
        "pattern": "^\s*VERSION (.*)$",
    },
    "changelog": {
        "git_log_options": "--pretty=format:- %s (%an)"
    },
    "git": {
        "work_branch": "dev",
        "main_branch": "master",
    }
}


def _load_config():
    # TODO parse releasetools.conf
    return DEFAULT_CONFIG


def _cd_project_root():
    project_dir = Path.cwd()
    while not (project_dir / ".git").exists():
        if len(project_dir.parts) == 1:
            raise ReleaseToolsError("Can't find project root")
        project_dir = project_dir.parent
    os.chdir(project_dir)


class App:
    def __init__(self, parser):
        self._parser = parser

    def run(self, app_main):
        args = self._parser.parse_args()
        try:
            _cd_project_root()
            self.repo = Repo(".")
            self.project_name = Path.cwd().name
            self.config = _load_config()

            return app_main(self, args)
        except ReleaseToolsError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 1
