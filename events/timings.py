class Timeout(object):
    __SECONDS = 7200  # 2 hours = 7200 seconds

    @staticmethod
    def miliseconds() -> int:
        return int(Timeout.__SECONDS*1000)

    @staticmethod
    def seconds() -> int:
        return Timeout.__SECONDS

    @staticmethod
    def minutes() -> int:
        return int(Timeout.__SECONDS/60)

    @staticmethod
    def hours() -> int:
        return int(Timeout.__SECONDS/3600)


class Queue(object):
    def __init__(self, time_seconds=900):  # 15 minutes = 900 seconds
        self.seconds = time_seconds

    @property
    def miliseconds(self) -> int:
        return int(self.seconds*1000)

    @property
    def minutes(self) -> int:
        return int(self.seconds/60)

    @property
    def hours(self) -> int:
        return int(self.seconds/3600)
