from decimal import Decimal, ROUND_HALF_DOWN, ROUND_DOWN, ROUND_HALF_UP


def to_decimal(value):
    return Decimal(str(value))


def round_to(value, decimals=0, strategy=ROUND_HALF_UP):
    precision = Decimal('1.' + '0' * decimals)
    return to_decimal(value).quantize(precision, strategy)


def round_half_to_positive(value, decimals=0):
    value = to_decimal(value)
    rounding_strategy = ROUND_HALF_DOWN
    if value > 0:
        rounding_strategy = ROUND_HALF_UP
    return round_to(value, decimals, rounding_strategy)


def compare_round(value, precision):
    true_half_up = round_half_to_positive(value, precision)
    python_half_up = round_to(value, precision)
    print(f"{value} => {true_half_up} | {python_half_up}")


print('1 decimal')
compare_round(1.23, 1)
compare_round(1.25, 1)
compare_round(1.235, 1)
compare_round(1.245, 1)

print('2 decimals')
compare_round(1.234, 2)
compare_round(1.235, 2)
compare_round(1.2344, 2)
compare_round(1.2345, 2)

print('negative number, 1 decimal')
compare_round(-1.23, 1)
compare_round(-1.25, 1)
compare_round(-1.235, 1)
compare_round(-1.245, 1)

print('negative number, 2 decimals')
compare_round(-1.234, 2)
compare_round(-1.235, 2)
compare_round(-1.2344, 2)
compare_round(-1.2345, 2)
