import re


class Puzzle:
    def __init__(self, fh):
        self._fh = fh


class PuzzleOne(Puzzle):
    def __init__(self, fh):
        super().__init__(fh)

    def run(self, red: int = 12, green: int = 13, blue: int = 14):
        games = {}

        with self._fh.open("r") as fh:
            for _ in fh.readlines():
                line = _.rstrip()

                game, subsets = line.split(":")
                game_id = re.match("^Game.(?P<id>[0-9]+).*", game)["id"]

                if game_id not in games:
                    games[game_id] = {}

                for subset in subsets.split(";"):
                    for mix in re.findall(
                        r"(?P<num>[0-9]+).(?P<color>red|green|blue)", subset
                    ):
                        if mix[1] not in games[game_id]:
                            games[game_id][mix[1]] = 0

                        if games[game_id][mix[1]] < int(mix[0]):
                            games[game_id][mix[1]] = int(mix[0])

        id_sum = 0

        for game in games:
            if games[game]["red"] > red:
                continue

            if games[game]["blue"] > blue:
                continue

            if games[game]["green"] > green:
                continue

            id_sum += int(game)

        return id_sum


class PuzzleTwo(Puzzle):
    def __init__(self, fh):
        super().__init__(fh)

    def run(self, red: int = 12, green: int = 13, blue: int = 14):
        games = {}

        with self._fh.open("r") as fh:
            for _ in fh.readlines():
                line = _.rstrip()

                game, subsets = line.split(":")
                game_id = re.match("^Game.(?P<id>[0-9]+).*", game)["id"]

                if game_id not in games:
                    games[game_id] = {}

                for subset in subsets.split(";"):
                    for mix in re.findall(
                        r"(?P<num>[0-9]+).(?P<color>red|green|blue)", subset
                    ):
                        if mix[1] not in games[game_id]:
                            games[game_id][mix[1]] = int(mix[0])

                        if int(mix[0]) > games[game_id][mix[1]]:
                            games[game_id][mix[1]] = int(mix[0])

        return sum(
            [
                games[game]["red"] * games[game]["green"] * games[game]["blue"]
                for game in games
            ]
        )
