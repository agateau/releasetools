import re


class VersionUpdater:
    def __init__(self, config):
        version_config = config["version"]
        self.rx = re.compile(version_config["pattern"])
        self.version_file = version_config["file"]
        with open(self.version_file, "rt") as f:
            self.lines = f.readlines()


def read(app):
    updater = VersionUpdater(app.config)
    for line in updater.lines:
        match = updater.rx.search(line)
        if match:
            return match.group(1)
    else:
        raise Exception("Version line not found")


def write(app, version, dry_run=False):
    updater = VersionUpdater(app.config)
    for idx, line in enumerate(updater.lines):
        match = updater.rx.search(line)
        if match:
            start, end = match.span(1)
            updater.lines[idx] = line[:start] + version + line[end:]
            break
    else:
        raise Exception("Version line not found")

    text = "".join(updater.lines)
    if dry_run:
        print(text)
    else:
        with open(updater.version_file, "wt") as f:
            f.write(text)
