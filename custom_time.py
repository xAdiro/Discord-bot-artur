import datetime


def __delta(delta_minutes=0) -> datetime.datetime:
    now = datetime.datetime.now()
    return now + datetime.timedelta(minutes=delta_minutes)


def full(delta_minutes=0) -> str:
    return __delta(delta_minutes).strftime("%d-%m-%Y %H:%M")


def time(delta_minutes=0) -> str:
    return __delta(delta_minutes).strftime("%H:%M")


def date(delta_minutes=0) -> str:
    return __delta(delta_minutes).strftime("%d-%m-%Y")

