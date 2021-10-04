from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, Dict, Iterator, List, NewType, Optional, Tuple

import dvc.api
import numpy as np
from numpy.typing import NDArray


@dataclass
class Dataset(object):
    data: NDArray
    targets: NDArray
    target_names: str
    feature_names: str


Key = NewType("Key", str)

Example = Dict[Key, Any]


def load():
    def _gen():
        for split in ["train", "test"]:
            yield load_poker_hand()

    return tuple(_gen())


def load_poker_hand(split=None):
    data_path = _get_data(split)
    return _load_poker_hand(data_path)


def _download(path: str) -> Any:
    return dvc.api.open(
        f"archive.ics.uci.edu/ml/machine-learning-databases/poker/{path}",
        remote="uci",
    )


def _get_data(split: Optional[str] = None):
    if split is None or split == "train":
        return "poker-hand-training-true.data"
    elif split == "test":
        return "poker-hand-testing.data"

    raise ValueError("Not a valid split")


def _load_poker_hand(path: str) -> Dataset:
    with _download(path) as f:
        dataset = np.genfromtxt(f, delimiter=",")

        data = dataset[:, :-1]
        targets = dataset[:, -1]

        return Dataset(
            data=data,
            targets=targets,
            target_names=[
                "Nothing",
                "One pair",
                "Two pair",
                "Three of a kind",
                "Straigh",
                "Flush",
                "Full house",
                "Four of a kind",
                "Straight flush",
                "Royal flush",
            ],
            feature_names=[
                "C1",
                "S1",
                "C2",
                "S2",
                "C3",
                "S3",
                "C4",
                "C5",
            ],
        )
