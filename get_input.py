import configparser
from pathlib import Path
import urllib.request


def find_config() -> Path:
    path = Path(__file__).resolve()
    for parent in path.parents:
        config_file = parent / "config.ini"
        if config_file.is_file():
            return config_file
    raise FileNotFoundError("No config.ini found")


config = configparser.ConfigParser()
config.read(find_config())
session = config.get("Cookies", "session")


def get_input(year: int, day: int):
    request = urllib.request.Request(
        f"https://adventofcode.com/{year}/day/{day}/input",
        headers={"Cookie": f"session={session}"},
    )

    with urllib.request.urlopen(request) as resp:
        content = resp.read().decode("utf-8").strip()
    return content
