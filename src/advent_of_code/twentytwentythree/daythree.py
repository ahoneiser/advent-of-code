import math
import re

from . import Puzzle


class PuzzleOne(Puzzle):
    def __init__(self, fh):
        super().__init__(fh)

    def run(self):
        board = self._data.splitlines()
        chars = {}

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[y][x] not in "0123456789.":
                    chars[(y, x)] = []

        for y, row in enumerate(board):
            for n in re.finditer(r"[0-9]+", row):
                edge = set()

                for r in (y - 1, y, y + 1):
                    for c in range(n.start() - 1, n.end() + 1):
                        edge.add((r, c))

                for o in edge & chars.keys():
                    chars[o].append(int(n.group()))

        return sum(sum(p) for p in chars.values())


class PuzzleTwo(Puzzle):
    def __init__(self, fh):
        super().__init__(fh)

    def run(self):
        board = self._data.splitlines()
        chars = {}

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[y][x] not in "0123456789.":
                    chars[(y, x)] = []

        for y, row in enumerate(board):
            for n in re.finditer(r"\d+", row):
                edge = set()

                for r in (y - 1, y, y + 1):
                    for c in range(n.start() - 1, n.end() + 1):
                        edge.add((r, c))

                for o in edge & chars.keys():
                    chars[o].append(int(n.group()))

        return sum(math.prod(p) for p in chars.values() if len(p) == 2)
