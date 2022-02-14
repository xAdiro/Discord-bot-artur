

class Timeout(object):
    __TIMEOUT_TIME_SECONDS = 7200  # 2 hours = 7200 seconds

    @property
    def miliseconds(self) -> int:
        return int(self.__TIMEOUT_TIME_SECONDS*1000)

    @property
    def seconds(self) -> int:
        return self.__TIMEOUT_TIME_SECONDS

    @property
    def minutes(self) -> int:
        return int(self.__TIMEOUT_TIME_SECONDS/60)

    @property
    def hours(self) -> int:
        return int(self.__TIMEOUT_TIME_SECONDS/3600)


class Queue(object):
    __QUEUE_TIME_SECONDS = 5  # 15 minutes = 900 seconds

    @property
    def miliseconds(self) -> int:
        return int(self.__QUEUE_TIME_SECONDS*1000)

    @property
    def seconds(self) -> int:
        return self.__QUEUE_TIME_SECONDS

    @property
    def minutes(self) -> int:
        return int(self.__QUEUE_TIME_SECONDS/60)

    @property
    def hours(self) -> int:
        return int(self.__QUEUE_TIME_SECONDS/3600)
