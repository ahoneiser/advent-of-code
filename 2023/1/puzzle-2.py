import pathlib
import re

# INPUT = pathlib.Path("puzzle-2-example-input.txt")
INPUT = pathlib.Path("input.txt")
MAP = {
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

with INPUT.open("r") as fh:
    numbers = []

    for line in fh.readlines():
        digits = []

        pattern = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")

        for match in pattern.findall(line.rstrip()):
            if match.isdigit():
                digits.append(int(match))

            else:
                digits.append(MAP[match])

        numbers.append(int(f"{digits[0]}{digits[-1]}"))

    print(sum(numbers))
