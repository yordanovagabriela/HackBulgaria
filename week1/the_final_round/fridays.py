from datetime import date


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def friday_years(start, end):
    sum = 0
    for i in range(start, end + 1):
        if is_leap_year(i) and (date(i, 1, 1).weekday() == 5 or date(i, 1, 2).weekday() == 5):
            sum += 1
        elif date(i, 1, 1).weekday() == 5:
            sum += 1
    return sum
print(friday_years(1753, 2000))
