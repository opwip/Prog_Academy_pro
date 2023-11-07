# Task 1

def geom_progression(start, mul):
    while True:
        yield start
        start *= mul
    # yield start
    # yield from geom_progression(start * mul, mul)


for i in geom_progression(1, 2):
    print(i, end="")
    if input().lower() == "break":
        break


# Task 2
def ranger(start, stop, step):
    yield from range(start, stop, step)


for i in ranger(1, 10, 1):
    print(i)
    # for j in i:
    #     print(j)


# Task 3

def prime(stop):
    if not isinstance(stop, int):
        raise TypeError()
    if stop < 2:
        raise ValueError()

    for n in range(2, stop):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            yield n


for i in prime(1000):
    print(i)

# Task 4
stopper = int(input("Stopper>>>"))
x = list(_ ** 2 for _ in range(2, stopper + 1))
print(x)


# Task 5
def fibanachi(quantity):
    buffer = [0, 1]
    while quantity != 0:
        tmp = buffer[1]
        buffer[1] = buffer[0] + buffer[1]
        buffer[0] = tmp
        yield buffer[0]
        quantity -= 1


for i in fibanachi(2000):
    print(i)


# Task 6


def dates(start: str, stop: str):
    def _0n_and_n_converter(name, maxed):
        if int(name) < maxed + 1:
            return "0" + str(int(name) + 1)
        else:
            return str(int(name) + 1)

    def check_leap_year_additional_day(year):
        if not year % 4 and not year % 100 and year % 400:
            return 0
        elif not year % 400:
            return 1
        elif year % 4 == 0 and year % 100:
            return 1
        else:
            return 0

    day = start[:2]
    month = start[3:5]
    year = start[6:]
    date = f"{day}.{month}.{year}"
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_number = 0
    additional_day = check_leap_year_additional_day(int(year))
    while date != stop:
        day = _0n_and_n_converter(day, 8)
        if int(month) == 2:
            if int(day) == 29 + additional_day:
                month = _0n_and_n_converter(month, 8)
                day = "01"
                month_number += 1
        else:
            if int(day) == months[month_number] + 1:
                month = _0n_and_n_converter(month, 8)
                day = "01"
                month_number += 1
        if int(month) == 13:
            year = str(int(year) + 1)
            additional_day = check_leap_year_additional_day(int(year))
            month = "01"
            month_number = 0
        yield f"{day}.{month}.{year}"
        date = f"{day}.{month}.{year}"


for i in dates("22.05.2007", "22.05.2029"):
    print(i)
