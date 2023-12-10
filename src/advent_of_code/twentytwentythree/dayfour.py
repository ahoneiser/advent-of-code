import re
import sys

from . import Puzzle


class PuzzleOne(Puzzle):
    def __init__(self, fh):
        super().__init__(fh)

    def run(self):
        total_points = 0

        with self._fh.open("r") as fh:
            for line in fh.readlines():
                card, numbers = line.rstrip().split(":")
                winning_numbers, numbers = numbers.split("|")

                winners = []
                points = 0

                for number in numbers.split():
                    if number in winning_numbers.split():
                        winners.append(number)

                for winner in winners:
                    if points == 0:
                        points = 1

                    else:
                        points = points * 2

                total_points += points

            return total_points


class PuzzleTwo(Puzzle):
    def __init__(self, fh):
        super().__init__(fh)

    def run(self):
        original_scratchcards = {}

        wins = {}

        with self._fh.open("r") as fh:
            for line in fh.readlines():
                card, numbers = line.rstrip().split(":")
                winning_numbers, numbers = numbers.split("|")

                card_number = int(re.search(r"(?P<number>\d+)$", card).group("number"))

                original_scratchcards[card_number] = {
                    "winning_numbers": winning_numbers.split(),
                    "numbers": numbers.split(),
                    "winners": [],
                }

                for number in original_scratchcards[card_number]["numbers"]:
                    if number in original_scratchcards[card_number]["winning_numbers"]:
                        original_scratchcards[card_number]["winners"].append(number)

        iteration = 0
        wins[iteration] = []

        for card in original_scratchcards:
            wins[iteration].append(
                {"card": card, "winners": len(original_scratchcards[card]["winners"])}
            )

        while any([card["winners"] > 0 for card in wins[iteration]]):
            iteration += 1
            wins[iteration] = []

            for card in wins[iteration - 1]:
                for i in range(card["winners"]):
                    x = card["card"] + i + 1

                    if x <= len(original_scratchcards):
                        wins[iteration].append(
                            {
                                "card": x,
                                "winners": len(original_scratchcards[x]["winners"]),
                            }
                        )

        return sum([len(wins[iteration]) for iteration in wins])
