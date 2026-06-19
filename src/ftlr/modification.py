from dataclasses import dataclass

from ftlr.xmp_types import XmpType, ValueType
from ftlr.xmp import Xmp


@dataclass(frozen=True)
class Modification:
    key: str
    xmp_type: XmpType
    value: ValueType

    def apply(self, xmp: Xmp):
        original_str = xmp[self.key]
        original_value = self.xmp_type.from_string(original_str)

        modified_value = original_value + self.value
        modified_str = self.xmp_type.to_string(modified_value)

        xmp[self.key] = modified_str

