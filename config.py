from typing import Dict, Iterable, Tuple, Type

from xmp_types import XmpType, Factory
from xmp import Xmp

__xmp_type_factory = Factory.instance()

__dict_mapping = {
    "x:xmpmeta": {
        "rdf:RDF": {
            "rdf:Description": {
                "@crs:ColorNoiseReduction": ("noise_reduction", __xmp_type_factory.integer(), int),
                "@crs:Exposure2012": ("exposure", __xmp_type_factory.real(), float),
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
