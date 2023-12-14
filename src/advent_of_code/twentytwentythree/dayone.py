import re

from . import Puzzle


class PuzzleOne(Puzzle):
    def __init__(self, fh):
        super().__init__(fh)

    def run(self):
        result = 0

        for line in self._data.splitlines():
            digits = []

            for char in line.rstrip():
                if char.isdigit():
                    digits.append(char)

            result += int(f"{digits[0]}{digits[-1]}")

        return result


class PuzzleTwo(Puzzle):
    __map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    def __init__(self, fh):
        super().__init__(fh)

    def run(self):
        numbers = []

        for line in self._data.splitlines():
            digits = []

            pattern = re.compile(
                r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
            )

            for match in pattern.findall(line.rstrip()):
                if match.isdigit():
                    digits.append(int(match))

                else:
                    digits.append(self.__map[match])

            numbers.append(int(f"{digits[0]}{digits[-1]}"))

        return sum(numbers)
