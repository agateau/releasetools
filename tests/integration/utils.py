from git import Repo


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


