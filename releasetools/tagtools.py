def apply_prefix(app, version):
    # TODO implement
    return version


def remove_prefix(app, version):
    # TODO implement
    return version


def get_release_tag(app):
    return app.repo.git.describe(abbrev=0)


def get_released_version(app):
    return remove_prefix(app, get_release_tag(app))


def create_tag(app, version):
    tag = apply_prefix(app, version)
    app.repo.create_tag(tag, message=f"{app.project_name} {version}")
    return tag
