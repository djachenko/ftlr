from abc import abstractmethod
from functools import lru_cache

ValueType = float


class XmpType:
    @abstractmethod
    def from_string(self, value: str) -> ValueType:
        pass

    @abstractmethod
    def to_string(self, value: ValueType) -> str:
        pass


class XmpReal(XmpType):
    def from_string(self, value: str) -> ValueType:
        float_value = float(value)

        return float_value

    def to_string(self, value: ValueType) -> str:
        modifier = "+" if value > 0 else "-"

        value = round(value, ndigits=2)

        return modifier + str(value)


class XmpInteger(XmpType):
    def from_string(self, value: str) -> ValueType:
        float_value = int(value)

        return float_value

    def to_string(self, value: ValueType) -> str:
        modifier = "+" if value > 0 else "-"

        value = int(round(value))

        return modifier + str(value)


class Factory:
    __instance = None

    @classmethod
    def instance(cls) -> 'Factory':
        if Factory.__instance is None:
            Factory.__instance = Factory()

        return Factory.__instance

    @lru_cache()
    def real(self) -> XmpType:
        return XmpReal()

    @lru_cache()
    def integer(self) -> XmpType:
        return XmpInteger()
