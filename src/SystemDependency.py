from sys import platform as _platform
from pathlib import Path


def get_os():
    if _platform == "darwin":
        return "Mac OS"
    elif _platform == "win32":
        return "Windows"


def get_root_path() -> Path:
    this_path = Path().resolve()
    root_path = this_path.parent

    return root_path


def get_image_path() -> Path:
    image_path = get_root_path() \
        .joinpath("Images")

    return image_path


def get_xml_path() -> Path:
    xml_path = get_root_path() \
        .joinpath("src") \
        .joinpath("Qrala_Config.xml")

    return xml_path


def get_settings_path() -> Path:
    settings_path = get_root_path() \
        .joinpath("src") \
        .joinpath("Settings.xml")

    return settings_path
