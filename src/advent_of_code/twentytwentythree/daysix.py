import re

from . import Puzzle


class PuzzleOne(Puzzle):
    def __init__(self, input_file):
        super().__init__(input_file)

    def run(self):
        durations, records = self._data.splitlines()

        durations = list(map(int, re.findall(r"\d+", durations)))
        records = list(map(int, re.findall(r"\d+", records)))

        result = 1

        for d, r in zip(durations, records):
            wins = 0

            for a in range(1, d):
                t = a * (d - a)

                if t > r:
                    wins += 1

            result *= wins

        return result


class PuzzleTwo(Puzzle):
    def __init__(self, input_file):
        super().__init__(input_file)

    def run(self):
        durations, records = self._data.splitlines()

        duration = int("".join(re.findall(r"\d+", durations)))
        record = int("".join(re.findall(r"\d+", records)))

        wins = 0

        for a in range(1, duration):
            t = a * (duration - a)

            if t > record:
                wins += 1

        return wins
