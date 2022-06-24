def is_leap(year):
    leap = False
    if 1900 <= year <= 10_000:

        if year % 100 == 0 and year % 400 == 0:
            leap = True
        elif year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                leap = False
            else:
                leap = True
    return leap


year = int(input())
print(is_leap(year))