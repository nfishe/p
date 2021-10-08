import pytest
import numpy as np

from .datasets import Dataset
from . import datasets


@pytest.mark.parametrize("split", [None, "train", "test"])
def test_load_poker_hand(split):
    poker_hand = datasets.load_poker_hand(split)
    assert isinstance(poker_hand, Dataset)
    assert np.unique(poker_hand.targets).size == len(poker_hand.target_names)


def test_load():
    X_train, X_test = datasets.load()
    assert X_train.data.shape[1] == X_test.data.shape[1]
