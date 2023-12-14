import pathlib


class Puzzle:
    _data = None

    def __init__(self, input_file):
        with pathlib.Path(input_file).open("r") as fh:
            self._data = fh.read().rstrip()
