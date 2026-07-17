from dataclasses import dataclass

from ftlr.modification import Modification
from ftlr.xmp_types import XmpType, Factory, ValueType

__types = Factory.instance()

__descriptions = [
    ("crs:Exposure2012", "exposure", __types.real(), -5, 5),
    ("crs:Contrast2012", "contrast", __types.integer(), -100, 100)
]


@dataclass(frozen=True)
class Config:
    key: str
    name: str
    type: XmpType
    min: float
    max: float

    def build_modification(self, value: ValueType) -> Modification:
        return Modification(self.key, self.type, value, self.min, self.max)


CONFIG = [Config(*desc) for desc in __descriptions]
