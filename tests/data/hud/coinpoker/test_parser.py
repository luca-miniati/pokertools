import os
from decimal import Decimal
from pokertools.data.hud.coinpoker.parser import CoinPokerParser


ROOT_DIR = os.path.join(os.path.dirname(__file__), 'data')


def test_parse_mtt():
    parser = CoinPokerParser()

    path = os.path.join(ROOT_DIR, 'mtt1.txt')
    with open(path) as f:
        hh = f.read()
        hh = next(parser(hh))

    n = len(hh.players)
    assert n == 6
    assert hh.starting_stacks == [2544, 15368, 29142, 11552, 5505, 9443]
    assert hh.antes == [63] * n
    assert max(hh.winnings) == 2128
    assert sum(hh.winnings) == 2128


    path = os.path.join(ROOT_DIR, 'mtt2.txt')
    with open(path) as f:
        hh = f.read()
        hh = next(parser(hh))

    n = len(hh.players)
    assert n == 6
    assert hh.starting_stacks == [8793, 2994, 15418, 29192, 11602, 5555]
    assert hh.antes == [50] * n
    assert max(hh.winnings) == 1500
    assert sum(hh.winnings) == 1500


def test_parse_nlh():
    parser = CoinPokerParser()

    path = os.path.join(ROOT_DIR, 'nlh1.txt')
    with open(path) as f:
        hh = f.read()
        hh = next(parser(hh))

    n = len(hh.players)
    assert n == 5
    assert hh.starting_stacks == [Decimal('1.98'), 3, Decimal('2.56'), Decimal('2.96'), Decimal('2.04')]
    assert hh.antes == [0] * n
    assert max(hh.winnings) == Decimal('0.90')
    assert sum(hh.winnings) == Decimal('0.90')


    path = os.path.join(ROOT_DIR, 'nlh2.txt')
    with open(path) as f:
        hh = f.read()
        hh = next(parser(hh))

    n = len(hh.players)
    assert n == 7
    assert hh.starting_stacks == [Decimal('2.12'), Decimal('1.93'), Decimal('2.06'), Decimal('6.64'), Decimal('0.94'), Decimal('1.27'), Decimal('2.16')]
    assert hh.antes == [0] * n
    assert max(hh.winnings) == Decimal('0.24')
    assert sum(hh.winnings) == Decimal('0.24')


    path = os.path.join(ROOT_DIR, 'nlh3.txt')
    with open(path) as f:
        hh = f.read()
        hh = next(parser(hh))

    n = len(hh.players)
    assert n == 6  # ironheart is sitting out
    assert hh.starting_stacks == [Decimal('1.93'), Decimal('0.8'), 2, Decimal('3.79'), Decimal('3.21'), Decimal('1.97')]
    assert hh.antes == [0] * n
    assert max(hh.winnings) == Decimal('3.78')
    assert sum(hh.winnings) == Decimal('3.78')