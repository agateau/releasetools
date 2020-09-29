import os

from git import Repo

from releasetools import rlt_tag


def create_repo(tmp_path, name="repo", branches=["dev"]):
    repo_path = tmp_path / name
    repo = Repo.init(repo_path)

    cmakelists_path = repo_path / "CMakeLists.txt"
    with open(cmakelists_path, "w") as f:
        f.write("project(test\n    VERSION 1.2.3\n)")
    repo.index.add([str(cmakelists_path)])
    repo.index.commit("Initial commit")

    for branch in branches:
        repo.create_head(branch)
    return repo


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
