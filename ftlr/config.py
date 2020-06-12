from typing import Dict, Iterable, Tuple, Type

from ftlr.xmp_types import XmpType, Factory
from ftlr.xmp import Xmp

__types = Factory.instance()

__dict_mapping = {
    "x:xmpmeta": {
        "rdf:RDF": {
            "rdf:Description": {
                "@crs:Exposure2012": ("exposure", __types.real(), float),
                "@crs:Contrast2012": ("contrast", __types.integer(), int)
            },
        },
    },
}


def __flatten_dict(d: Dict) -> Iterable[Tuple[str, str, XmpType, Type]]:
    result = []

    for key, value in d.items():
        if not isinstance(value, Dict):
            result.append((key, *value))

            continue

        tuples = __flatten_dict(value)

        for path, *rest in tuples:
            result.append((
                Xmp.SEPARATOR.join([key, path]),
                *rest
            ))

    # noinspection PyTypeChecker
    return result


CONFIG = __flatten_dict(__dict_mapping)
