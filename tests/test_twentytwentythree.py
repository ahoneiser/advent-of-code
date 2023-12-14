import pathlib
from unittest import TestCase

from advent_of_code.twentytwentythree import (
    dayfive,
    dayfour,
    dayone,
    daysix,
    daythree,
    daytwo,
)


class TestDayOne(TestCase):
    def test_puzzle_one_example(self):
        p = dayone.PuzzleOne(pathlib.Path("data/2023/1/a-example-input.txt"))

        assert p.run() == 142

    def test_puzzle_one(self):
        p = dayone.PuzzleOne(pathlib.Path("data/2023/1/input.txt"))

        assert p.run() == 57346

    def test_puzzle_two_example(self):
        p = dayone.PuzzleTwo(pathlib.Path("data/2023/1/b-example-input.txt"))

        assert p.run() == 281

    def test_puzzle_two(self):
        p = dayone.PuzzleTwo(pathlib.Path("data/2023/1/input.txt"))

        assert p.run() == 57345


class TestDayTwo(TestCase):
    def test_puzzle_one_example(self):
        p = daytwo.PuzzleOne(pathlib.Path("data/2023/2/example-input.txt"))

        assert p.run() == 8

    def test_puzzle_one(self):
        p = daytwo.PuzzleOne(pathlib.Path("data/2023/2/input.txt"))

        assert p.run() == 2101

    def test_puzzle_two_example(self):
        p = daytwo.PuzzleTwo(pathlib.Path("data/2023/2/example-input.txt"))

        assert p.run() == 2286

    def test_puzzle_two(self):
        p = daytwo.PuzzleTwo(pathlib.Path("data/2023/2/input.txt"))

        assert p.run() == 58269


class TestDayThree(TestCase):
    def test_puzzle_one_example(self):
        p = daythree.PuzzleOne(pathlib.Path("data/2023/3/example-input.txt"))

        assert p.run() == 4361

    def test_puzzle_one(self):
        p = daythree.PuzzleOne(pathlib.Path("data/2023/3/input.txt"))

        assert p.run() == 550934

    def test_puzzle_two_example(self):
        p = daythree.PuzzleTwo(pathlib.Path("data/2023/3/example-input.txt"))

        assert p.run() == 467835

    def test_puzzle_two(self):
        p = daythree.PuzzleTwo(pathlib.Path("data/2023/3/input.txt"))

        assert p.run() == 81997870


class TestDayFour(TestCase):
    def test_puzzle_one_example(self):
        p = dayfour.PuzzleOne(pathlib.Path("data/2023/4/example-input.txt"))

        assert p.run() == 13

    def test_puzzle_one(self):
        p = dayfour.PuzzleOne(pathlib.Path("data/2023/4/input.txt"))

        assert p.run() == 25174

    def test_puzzle_two_example(self):
        p = dayfour.PuzzleTwo(pathlib.Path("data/2023/4/example-input.txt"))

        assert p.run() == 30

    def test_puzzle_two(self):
        p = dayfour.PuzzleTwo(pathlib.Path("data/2023/4/input.txt"))

        assert p.run() == 6420979


class TestDayFive(TestCase):
    def test_puzzle_one_example(self):
        p = dayfive.PuzzleOne(pathlib.Path("data/2023/5/example-input.txt"))

        assert p.run() == 35

    def test_puzzle_one(self):
        p = dayfive.PuzzleOne(pathlib.Path("data/2023/5/input.txt"))

        assert p.run() == 57075758

    def test_puzzle_two_example(self):
        p = dayfive.PuzzleTwo(pathlib.Path("data/2023/5/example-input.txt"))

        assert p.run() == 46

    def test_puzzle_two(self):
        p = dayfive.PuzzleTwo(pathlib.Path("data/2023/5/input.txt"))

        assert p.run() == 31161857


class TestDaySix(TestCase):
    def test_puzzle_one_example(self):
        p = daysix.PuzzleOne(pathlib.Path("data/2023/6/example-input.txt"))

        assert p.run() == 288

    def test_puzzle_one(self):
        p = daysix.PuzzleOne(pathlib.Path("data/2023/6/input.txt"))

        assert p.run() == 160816

    def test_puzzle_two_example(self):
        p = daysix.PuzzleTwo(pathlib.Path("data/2023/6/example-input.txt"))

        assert p.run() == 71503

    def test_puzzle_two(self):
        p = daysix.PuzzleTwo(pathlib.Path("data/2023/6/input.txt"))

        assert p.run() == 46561107
