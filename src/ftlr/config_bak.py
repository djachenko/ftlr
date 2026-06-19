from dataclasses import dataclass
from functools import cache
from pathlib import Path
from typing import Dict, Iterable, List

from ftlr.modifier import Modification
from ftlr.xmp_types import XmpType, Factory

__types = Factory.instance()

__dict_mapping = {
    "x:xmpmeta": {
        "rdf:RDF": {
            "rdf:Description": {
                "crs:Exposure2012": ("exposure", __types.real()),
                "crs:Contrast2012": ("contrast", __types.integer())
            },
        },
    },
}


@dataclass(frozen=True)
class Config:
    path: Path
    name: str
    type: XmpType

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

        return Modification(self.path, self.type, self.type.python_type(value))


def __flatten_dict(d: Dict, path: Path) -> Iterable[Config]:
    result = []

    for key, value in d.items():
        key_path = path / key

        if isinstance(value, tuple):
            name, type_ = value

            result.append(Config(key_path, name, type_))
        elif isinstance(value, dict):
            result += __flatten_dict(value, key_path)
        else:
            assert False

    return result


CONFIG = __flatten_dict(__dict_mapping, Path())
