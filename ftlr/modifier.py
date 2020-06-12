from typing import List

from ftlr.xmp_types import XmpType, ValueType
from ftlr.xmp import Xmp


class Modification:
    def __init__(self, path: str, xmp_type: XmpType, value: ValueType) -> None:
        assert path is not None
        assert xmp_type is not None
        assert value is not None

        self.path = path
        self.xmp_type = xmp_type
        self.value = value

    def __hash__(self):
        return hash(self.path)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Modification):
            return False

        return self.path == o.path

    def apply(self, xmp: Xmp):
        original_str = xmp[self.path]
        original_value = self.xmp_type.from_string(original_str)

        modified_value = original_value + self.value
        modified_str = self.xmp_type.to_string(modified_value)

        xmp[self.path] = modified_str


class Modifier:
    def __init__(self, modifications: List[Modification]) -> None:
        super().__init__()

        assert len(set(modifications)) == len(modifications)

        self.__modifications = modifications

    def apply(self, xmp: Xmp):
        for modification in self.__modifications:
            modification.apply(xmp)
