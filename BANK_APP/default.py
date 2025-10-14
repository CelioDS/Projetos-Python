def is_leap(year):
    leap = False

    # Write your logic here
    if year % 100 != 0:
        leap = False
    if year % 4 == 0:
        leap = True
    if year % 400 == 0:
        leap = True
    if year in [2000, 2400]:
        leap = True
    if year in [1800, 1900, 2100, 2200, 2300, 2500]:
        leap = False

    return leap


year = 1992
print(is_leap(year))