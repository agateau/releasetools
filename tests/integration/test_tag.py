import os

from releasetools import rlt_tag
from tests.integration.utils import create_repo


def test_success(tmp_path):
    repo = create_repo(tmp_path)
    os.chdir(repo.working_tree_dir)
    assert rlt_tag.main([]) == 0
    assert [x.name for x in repo.tags] == ["1.2.3"]


def test_wrong_branch(tmp_path):
    repo = create_repo(tmp_path)
    os.chdir(repo.working_tree_dir)
    repo.heads["dev"].checkout()
    assert rlt_tag.main([]) != 0
