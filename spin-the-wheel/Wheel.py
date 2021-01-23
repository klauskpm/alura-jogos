from random import randrange


class Wheel:
    def __init__(self, options: [int]):
        self._options = options

    def spin(self):
        rand_position = randrange(0, len(self._options) - 1)
        return self._options[rand_position]

