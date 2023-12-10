import pathlib

from advent_of_code.twentytwentythree import dayone, daythree, daytwo, dayfour


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


def test_dayThree_puzzleOne():
    p = daythree.PuzzleOne(pathlib.Path("data/2023/3/example-input.txt"))

    assert p.run() == 4361


def test_dayThree_puzzleTwo():
    p = daythree.PuzzleTwo(pathlib.Path("data/2023/3/example-input.txt"))

    assert p.run() == 467835

def test_dayFour_puzzleOne():
    p = dayfour.PuzzleOne(pathlib.Path("data/2023/4/example-input.txt"))

    assert p.run() == 13

    p = dayfour.PuzzleOne(pathlib.Path("data/2023/4/input.txt"))

    assert p.run() == 25174


def test_dayFour_puzzleTwo():
    p = dayfour.PuzzleTwo(pathlib.Path("data/2023/4/example-input.txt"))

    assert p.run() == 30

    p = dayfour.PuzzleTwo(pathlib.Path("data/2023/4/input.txt"))

    assert p.run() == 6420979
