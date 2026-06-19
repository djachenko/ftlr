from dataclasses import dataclass
from functools import cache
from typing import List

from ftlr.modification import Modification
from ftlr.xmp_types import XmpType, Factory

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

    @property
    @cache
    def args(self) -> List[str]:
        short_name = f"-{self.name[0]}"
        long_name = f"--{self.name}"

        return [
            short_name,
            long_name,
        ]

    @property
    @cache
    def kwargs(self):
        return {
            "type": self.build_modification
        }

    def build_modification(self, value: str) -> Modification:
        assert value.startswith("+") or value.startswith("-")

        return Modification(self.key, self.type, self.type.python_type(value))


CONFIG = [Config(*desc) for desc in __descriptions]
