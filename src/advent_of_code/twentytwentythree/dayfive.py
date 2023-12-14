import re
import sys

from . import Puzzle


class PuzzleOne(Puzzle):
    def __init__(self, fh):
        super().__init__(fh)

    def run(self):
        location_number = int()
        data = None

        with self._fh.open("r") as fh:
            data = fh.read().rstrip()

        chunks = data.split("\n\n")
        maps = {
            i: [[int(y) for y in x.split()] for x in m.split("\n")[1:]]
            for i, m in enumerate(data.split("\n\n")[1:])
        }

        for seed in [int(x) for x in chunks[0].split(":")[1].split()]:
            kicker = seed

            for next_map in maps:
                for numbers in maps[next_map]:
                    if numbers[1] <= kicker <= numbers[1] + numbers[2]:
                        kicker = numbers[0] + (kicker - numbers[1])

                        break

            if location_number == 0 or kicker < location_number:
                location_number = kicker

        return location_number


class PuzzleTwo(Puzzle):
    def __init__(self, fh):
        super().__init__(fh)

    def run(self):
        data = None

        with self._fh.open("r") as fh:
            data = fh.read().rstrip()

        data_chunks = data.split("\n\n")

        seed_inputs = [int(x) for x in data_chunks[0].split(":")[1].split()]
        seed_ranges = [
            (seed_inputs[i], seed_inputs[i] + seed_inputs[i + 1])
            for i in range(0, len(seed_inputs), 2)
        ]
        maps = [
            [
                [int(x) for x in numberblock.split()]
                for numberblock in next_map.splitlines()[1:]
            ]
            for next_map in data_chunks[1:]
        ]

        for m in maps:
            new_seed_ranges = []

            while len(seed_ranges):
                start, end = seed_ranges.pop()

                for dest_start, source_start, length in m:
                    overlap_start = max(start, source_start)
                    overlap_end = min(end, source_start + length)

                    if overlap_start < overlap_end:
                        new_seed_ranges.append(
                            (
                                dest_start + (overlap_start - source_start),
                                dest_start + (overlap_end - source_start),
                            )
                        )

                        if start < overlap_start:
                            seed_ranges.append((start, overlap_start))

                        if overlap_end < end:
                            seed_ranges.append((overlap_end, end))

                        break

                else:
                    new_seed_ranges.append((start, end))

            seed_ranges = new_seed_ranges

        return min(seed_ranges)[0]
