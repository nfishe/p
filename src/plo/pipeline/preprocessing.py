from sklearn.preprocessing import scale
import pandas as pd

from ..datasets import load_poker_hand
from ..utils import fs, parser


@parser.command(args=[])
def preprocess(*args):
    poker_hand = load_poker_hand()
    data = scale(poker_hand.data)

    prepared = fs.data() / "prepared"
    if not prepared.exists():
        prepared.mkdir()

    df = pd.DataFrame(data)
    df.to_csv(prepared.joinpath("train.csv"))
