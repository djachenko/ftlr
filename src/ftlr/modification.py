from dataclasses import dataclass

from ftlr.xmp import Xmp
from ftlr.xmp_types import XmpType, ValueType


@dataclass(frozen=True)
class Modification:
    @dataclass(frozen=True)
    class BoxError:
        start_value: ValueType
        boxed_value: ValueType
        range: tuple[ValueType, ValueType]

    key: str
    xmp_type: XmpType
    value: ValueType

    min: ValueType
    max: ValueType

    def apply(self, xmp: Xmp) -> "Modification.BoxError | None":
        message = None

        original_str = xmp[self.key]
        original_value = self.xmp_type.from_string(original_str)

        modified_value = original_value + self.value
        non_boxed_value = modified_value

        modified_value = max(modified_value, self.min)
        modified_value = min(modified_value, self.max)

        if non_boxed_value != modified_value:
            message = Modification.BoxError(
                non_boxed_value,
                modified_value,
                (self.min, self.max)
            )

        modified_str = self.xmp_type.to_string(modified_value)

        xmp[self.key] = modified_str

        return message

