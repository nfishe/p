import sys

from os import PathLike
from pathlib import Path
from typing import Optional, Union


_DATA_DIR = "data"


StrPath = Union[str, Union[PathLike[str]]]


def get_project_root():
    return Path(sys.path[0])


def get_cwd(cwd: Optional[Path] = None) -> Path:
    if cwd is None:
        return Path.cwd()

    return cwd


def join(*other: StrPath, parent: Optional[Path] = None) -> Path:
    """Join the other paths to the parent."""
    parent = get_project_root()

    return parent.joinpath(*other)


def data() -> Path:
    """Returns the"""
    parent = get_project_root()
    data_dir = get_cwd(parent) / _DATA_DIR
    if not data_dir.exists():
        data_dir.mkdir()

    return data_dir.resolve()
