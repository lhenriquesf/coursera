import sys
import calendar as cl


def is_leap(year):
    if year.isnumeric():
        year = int(year)
        return cl.isleap(year)
    return cl.isleap(year)


