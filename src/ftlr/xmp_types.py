from abc import abstractmethod
from functools import cache
from typing import Type

ValueType = float | int


class XmpType:
    @property
    @abstractmethod
    def python_type(self) -> Type[ValueType]:
        pass

    def from_string(self, value: str) -> ValueType:
        return self.python_type(value)

    @abstractmethod
    def prepare_value(self, value: ValueType) -> ValueType:
        pass

    def to_string(self, value: ValueType) -> str:
        if value > 0:
            sign = "+"
        elif value < 0:
            sign = "-"
        else:
            sign = ""

        value = abs(self.prepare_value(value))

        return sign + str(value)


class XmpReal(XmpType):
    @property
    def python_type(self) -> Type[ValueType]:
        return float

    def prepare_value(self, value: ValueType) -> ValueType:
        return round(value, ndigits=2)


class XmpInteger(XmpType):
    @property
    def python_type(self) -> Type[ValueType]:
        return int

    def prepare_value(self, value: ValueType) -> ValueType:
        return int(round(value))


class Factory:
    __instance = None

    @classmethod
    @cache
    def instance(cls) -> "Factory":
        return Factory()

    @cache
    def real(self) -> XmpType:
        return XmpReal()

    @cache
    def integer(self) -> XmpType:
        return XmpInteger()
