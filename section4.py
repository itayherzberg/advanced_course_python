def gen_secs():
    return (x for x in range(60))


def gen_minutes():
    return (x for x in range(60))


def gen_hours():
    return (x for x in range(24))


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "{:02d}:{:02d}:{:02d}".format(hour, minute, second)


def gen_years(start=2023):
    while True:
        yield start
        start += 1


def gen_months():
    return (x for x in range(1, 13))


def gen_days(month, leap_year=True):
    days = 29 if month == 2 and leap_year else 28 if month == 2 else 30 if month % 2 == 0 else 31
    return (x for x in range(1, days + 1))


def gen_date():
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month, year % 4 == 0):
                for time in gen_time():
                    yield "{:02d}/{:02d}/{} ".format(day, month, year) + time


def main():
    date = gen_date()
    x = 0
    while True:
        if x % 1000000 == 0 and x:
            print(next(date))
        else:
            next(date)
        x += 1


if __name__ == "__main__":
    main()
