from copy import deepcopy

from releasetools.app import _load_config, DEFAULT_CONFIG, CONFIG_FILE_NAME


def test_no_config_file(tmp_path):
    config = _load_config(tmp_path)
    assert config == DEFAULT_CONFIG


def test_config_file(tmp_path):
    version_file = "version.txt"

    config_path = tmp_path / CONFIG_FILE_NAME
    with open(config_path, "w") as f:
        f.write(f"[version]\nfile = \"{version_file}\"\n")

    config = _load_config(tmp_path)

    expected_config = deepcopy(DEFAULT_CONFIG)
    expected_config["version"]["file"] = version_file
    assert config["version"]["file"] == version_file
    assert config == expected_config
