import os
import sys

from pathlib import Path

import mergedeep
import toml

from git import Repo

from releasetools.errors import ReleaseToolsError


DEFAULT_CONFIG = {
    "version": {
        "file": "CMakeLists.txt",
        "pattern": r"^\s*VERSION (.*)$",
    },
    "changelog": {
        "git_log_options": "--pretty=format:- %s (%an)"
    },
    "git": {
        "work_branch": "dev",
        "main_branch": "master",
    }
}

CONFIG_FILE_NAME = "releasetools.toml"


def _load_config(project_path):
    config_path = project_path / CONFIG_FILE_NAME
    if not config_path.exists():
        return DEFAULT_CONFIG

    try:
        toml_config = toml.load(config_path)
    except toml.TomlDecodeError as e:
        raise ReleaseToolsError(f"Invalid configuration file: {e}")

    try:
        return mergedeep.merge({}, DEFAULT_CONFIG, toml_config,
                               strategy=mergedeep.Strategy.TYPESAFE_REPLACE)
    except TypeError as e:
        raise ReleaseToolsError(f"Invalid value in configuration file: {e}")


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

    def run(self, app_main, argv=None):
        if argv is None:
            argv = sys.argv[1:]
        args = self._parser.parse_args(argv)
        try:
            _cd_project_root()
            project_path = Path.cwd()
            self.repo = Repo(".")
            self.project_name = project_path.name
            self.config = _load_config(project_path)

            return app_main(self, args)
        except ReleaseToolsError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 1
