# Task 1
import checkouts


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


for i in fibanachi(10):
    print(i)


# Task 6


def dates(start: str, stop: str):

    def check_leap_year_additional_day(year):
        if not year % 4 and not year % 100 and year % 400:
            return 0
        elif not year % 400:
            return 1
        elif year % 4 == 0 and year % 100:
            return 1
        else:
            return 0

    day = int(start[:2])
    month = int(start[3:5])
    year = int(start[6:])
    date = f"{day}.{month}.{year}"
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    yield f"{'' if day > 9 else '0'}{day}.{'' if month > 9 else '0'}{month}.{year}"
    while date != stop:
        day += 1
        if month == 2 and day == 29 and check_leap_year_additional_day(year):
            pass
        elif months[month - 1] < day:
            day = 1
            month += 1
        if month == 13:
            month = 1
            year += 1
        yield f"{'' if day > 9 else '0'}{day}.{'' if month > 9 else '0'}{month}.{year}"
        date = f"{'' if day > 9 else '0'}{day}.{'' if month > 9 else '0'}{month}.{year}"
        # day = _0n_and_n_converter(day, 8)
        # if int(month) == 2:
        #     if int(day) == 29 + additional_day:
        #         month = _0n_and_n_converter(month, 8)
        #         day = "01"
        #         month_number += 1
        # else:
        #     if int(day) == months[month_number] + 1:
        #         month = _0n_and_n_converter(month, 8)
        #         day = "01"
        #         month_number += 1
        # if int(month) == 13:
        #     year = str(int(year) + 1)
        #     additional_day = check_leap_year_additional_day(int(year))
        #     month = "01"
        #     month_number = 0
        # yield f"{day}.{month}.{year}"
        # date = f"{day}.{month}.{year}"


def feb_29(year):
    if not year % 4 and not year % 100 and year % 400:
        return False
    elif not year % 400:
        return True
    elif year % 4 == 0 and year % 100:
        return True
    else:
        return False


def all_dates_between(start: str, finish: str) -> str:
    month_durations = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d, m, y = (int(x) for x in start.split("."))
    fd, fm, fy = (int(x) for x in finish.split("."))
    while y < fy or m < fm or d < fd:
        yield f"{'' if d > 9 else '0'}{d}.{'' if m > 9 else '0'}{m}.{y}"
        if m == 2 and d == 28 and feb_29(y):
            d += 1
            continue
        if d < month_durations[m - 1]:
            d += 1
        elif m < 12:
            d = 1
            m += 1
        else:
            d = 1
            m = 1
            y += 1
    if y == fy and m == fm and d == fd:
        yield finish


# for date in all_dates_between("02.01.2028", "02.02.2028"):
#     print(date)

start_date = "28.02.2028"
end_date = "29.02.2031"

for i, j in zip(dates(start_date, end_date), all_dates_between(start_date, end_date)):
    if i != j:
        print(i, j)
