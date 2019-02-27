def is_leap(year):
    leap = False
    # Write your logic here
    for i in range(1900, 100000):
        if year in (1900, 2100, 2200, 2300, 2500):
            leap = False
        else:
            if year == i and year % 4 == 0 \
                    or (year % 100 != 0 and year % 400 == 0):
                leap = True
    return leap


if __name__ == '__main__':
    print(is_leap(int(input())))
