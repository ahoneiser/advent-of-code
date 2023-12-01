import pathlib

from advent_of_code.twentytwentythree import dayone


def test_dayOne_puzzleOne():
    p = dayone.PuzzleOne(pathlib.Path("data/2023/1/a-example-input.txt"))

    assert p.run() == 142


def test_dayOne_puzzleTwo():
    p = dayone.PuzzleTwo(pathlib.Path("data/2023/1/b-example-input.txt"))

    assert p.run() == 281
