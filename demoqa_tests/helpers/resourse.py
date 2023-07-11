from pathlib import Path


def get_file(filename: str):
    return str(Path(__file__).parent.parent.parent.joinpath("resourses", filename))