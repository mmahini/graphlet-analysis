from utils.singleton import singleton


@singleton
class Utils():

    def isEqualTuple(self, a: tuple, b: tuple) -> bool:
        return sorted(a) == sorted(b)
