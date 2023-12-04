import pathlib

from advent_of_code.twentytwentythree import dayone, daytwo


def test_dayOne_puzzleOne():
    p = dayone.PuzzleOne(pathlib.Path("data/2023/1/a-example-input.txt"))

    assert p.run() == 142


def test_dayOne_puzzleTwo():
    p = dayone.PuzzleTwo(pathlib.Path("data/2023/1/b-example-input.txt"))

    assert p.run() == 281


def test_dayTwo_puzzleOne():
    p = daytwo.PuzzleOne(pathlib.Path("data/2023/2/example-input.txt"))

    assert p.run() == 8


def test_dayTwo_puzzleTwo():
    p = daytwo.PuzzleTwo(pathlib.Path("data/2023/2/example-input.txt"))

    assert p.run() == 2286
