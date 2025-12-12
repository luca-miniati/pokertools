import os
from pokertools.data.hud.coinpoker.parser import CoinPokerParser


ROOT_DIR = os.path.join(os.path.dirname(__file__), 'data')


def test_parse_mtt():
    parser = CoinPokerParser()
    path = os.path.join(ROOT_DIR, 'nlh1.txt')
    with open(path) as f:
        hh = f.read()
        hh = next(parser(hh))
    return hh


hh = test_parse_mtt()