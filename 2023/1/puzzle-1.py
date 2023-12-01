import pathlib

INPUT = pathlib.Path("input.txt")
SUM = 0

with INPUT.open("r") as fh:
    for line in fh.readlines():
        digits = []

        for char in line.rstrip():
            if char.isdigit():
                digits.append(char)

        SUM += int(f"{digits[0]}{digits[-1]}")

print(SUM)
