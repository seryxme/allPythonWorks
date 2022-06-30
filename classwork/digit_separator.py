def get_digit(number: int, position: int) -> int:
    """
    Pass in a number and the position of the digit you wish to extract.
    Returns the digit at that position.
    :param number:
    :param position:
    :return:
    """
    return number//(10 ** position) % 10

print(get_digit(45637, 3))