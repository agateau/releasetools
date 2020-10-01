import os
from pathlib import Path

from releasetools import rlt_version
from tests.integration.utils import create_repo, create_file, commit_file


def test_released(tmp_path, capsys):
    # GIVEN a repo with two version tags
    repo = create_repo(tmp_path)
    os.chdir(repo.working_tree_dir)
    tags = ["1.0.0", "1.1.0"]
    for tag in tags:
        path = Path(repo.working_tree_dir) / tag
        create_file(path)
        commit_file(repo, path)
        repo.create_tag(tag, message=f"Release {tag}")

    # AND a commit after the tag
    path = Path(repo.working_tree_dir) / "new"
    create_file(path)
    commit_file(repo, path)

    # WHEN I call rlt-version --released
    assert rlt_version.main(["--released"]) == 0

    # THEN the latest version is printed
    assert capsys.readouterr().out.strip() == tags[-1]
