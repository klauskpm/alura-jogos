from random import randrange, randint
from decimal import Decimal

def to_decimal(value):
    return Decimal(str(value))

class Wheel:
    _STRENGTH_RANGES = {
        1: (0, 2),
        2: (3, 7),
        3: (8, 14),
    }
    _PRECISION_FACTOR = (0.9, 1, 1.1)

    def __init__(self, options: [int]):
        self._options = options

    def spin(self):
        rand_position = self._get_position()
        return self._options[rand_position]

    def _get_position(self):
        rand_precision = randrange(0, len(Wheel._PRECISION_FACTOR))
        precision = Wheel._PRECISION_FACTOR[rand_precision]

        print(
            'Nível de força:\n'
            '1 - Fraco\n'
            '2 - Médio\n'
            '3 - Forte'
        )
        strength = int(input('Com que força (número) você quer jogar?'))
        min_placement, max_placement = Wheel._STRENGTH_RANGES.get(strength)
        rand_placement = randint(min_placement, max_placement)

        final_placement = int(to_decimal(rand_placement) * to_decimal(precision))
        return final_placement % 4
