import os

from releasetools import rlt_tag
from tests.integration.utils import create_repo


def get_tag_set(repo):
    return {x.name for x in repo.tags}


def test_success(tmp_path):
    # GIVEN a remote repo
    remote_repo = create_repo(tmp_path, name="remote")

    # AND a local clone
    repo = remote_repo.clone(tmp_path / "local")
    os.chdir(repo.working_tree_dir)

    # WHEN I call rlt-tag
    assert rlt_tag.main([]) == 0

    # THEN a tag is created in the local repo
    assert get_tag_set(repo) == {"1.2.3"}

    # AND the remote repo does not have the tag
    assert get_tag_set(remote_repo) == set()


def test_wrong_branch(tmp_path):
    repo = create_repo(tmp_path)
    os.chdir(repo.working_tree_dir)
    repo.heads["dev"].checkout()
    assert rlt_tag.main([]) != 0


def test_tag_push(tmp_path):
    # GIVEN a remote repo
    remote_repo = create_repo(tmp_path, name="remote")

    # AND a local clone
    repo = remote_repo.clone(tmp_path / "local")
    os.chdir(repo.working_tree_dir)

    # WHEN I call rlt-tag --push
    assert rlt_tag.main(["--push"]) == 0

    # THEN a tag is created in the local repo
    assert get_tag_set(repo) == {"1.2.3"}

    # AND the remote repo also has the tag
    assert get_tag_set(remote_repo) == {"1.2.3"}
