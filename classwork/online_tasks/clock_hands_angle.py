from math import pi


def hand_angle(hours, minutes):
    result = abs((hours * 30 + (minutes/2)) - (minutes * 6))
    return result * pi/180 if result < 180 else 360 - result


print(hand_angle(6, 5))