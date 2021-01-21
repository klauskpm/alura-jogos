from decimal import Decimal, ROUND_HALF_DOWN, ROUND_DOWN, ROUND_HALF_UP


def to_decimal(value):
    return Decimal(str(value))


def round_to(value, decimals=0, strategy=ROUND_HALF_UP):
    precision = Decimal('1.' + '0' * decimals)
    return to_decimal(value).quantize(precision, strategy)


def round_half_up(value, decimals=0):
    value = to_decimal(value)
    if value > 0:
        value = _aux_round_up(value, decimals)
    return round_to(value, decimals, ROUND_HALF_DOWN)


def _aux_round_up(value, decimals):
    multiplier = 10 ** decimals
    multiplied_value = (value * multiplier).normalize()

    _, extra_decimals = str(multiplied_value).split('.')
    extra_decimals = len(extra_decimals)

    aux_value = '0.' + ('5' * extra_decimals)
    aux_value = Decimal(aux_value)

    return (multiplied_value + aux_value).quantize(Decimal('1.'), ROUND_DOWN) / multiplier


print('1 decimal')
print(round_half_up(1.23, 1), round_to(1.23, 1))
print(round_half_up(1.25, 1), round_to(1.25, 1))
print(round_half_up(1.235, 1), round_to(1.235, 1))
print(round_half_up(1.245, 1), round_to(1.245, 1))

print('2 decimals')
print(round_half_up(1.234, 2), round_to(1.234, 2))
print(round_half_up(1.235, 2), round_to(1.235, 2))
print(round_half_up(1.2344, 2), round_to(1.2344, 2))
print(round_half_up(1.2345, 2), round_to(1.2345, 2))

print('negative number, 1 decimal')
print(round_half_up(-1.23, 1), round_to(-1.23, 1))
print(round_half_up(-1.25, 1), round_to(-1.25, 1))
print(round_half_up(-1.235, 1), round_to(-1.235, 1))
print(round_half_up(-1.245, 1), round_to(-1.245, 1))

print('negative number, 2 decimals')
print(round_half_up(-1.234, 2), round_to(-1.234, 2))
print(round_half_up(-1.235, 2), round_to(-1.235, 2))
print(round_half_up(-1.2344, 2), round_to(-1.2344, 2))
print(round_half_up(-1.2345, 2), round_to(-1.2345, 2))
