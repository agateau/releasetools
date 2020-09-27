from subprocess import run


def apply_prefix(app, version):
    # TODO implement
    return version


def remove_prefix(app, version):
    # TODO implement
    return version


def get_release_tag():
    proc = run(["git", "describe", "--abbrev=0"], capture_output=True,
               text=True)
    return str(proc.stdout).strip()


def get_released_version(app):
    return remove_prefix(app, get_release_tag())


def create_tag(app, version):
    tag = apply_prefix(app, version)
    run(["git", "tag", "--annotate", tag, "--message",
         f"{app.project_name} {version}"])
