from pathlib import Path

import xmltodict


# todo: add context management
class Xmp:
    SEPARATOR = "/"
    SUFFIX = ".xmp"

    def __init__(self, d: dict) -> None:
        super().__init__()

        self.__dict = d

    def __getitem__(self, key: str) -> str:
        parts = key.split(Xmp.SEPARATOR)

        value = self.__dict

        for part in parts:
            assert part in value

            value = value[part]

        assert isinstance(value, str)

        return value

    def __setitem__(self, key: str, value: str):
        parts = key.split(Xmp.SEPARATOR)

        dst = self.__dict

        for part in parts[:-1]:
            assert part in dst

            dst = dst[part]

        assert parts[-1] in dst

        dst[parts[-1]] = value

    @classmethod
    def read(cls, path: Path) -> 'Xmp':
        with path.open() as xmp_file:
            data = xmp_file.read()

        res = xmltodict.parse(data)

        xmp = cls(res)

        return xmp

    def write(self, path: Path):
        data = xmltodict.unparse(self.__dict, pretty=True, indent=" ")

        with path.open("w") as xmp_file:
            xmp_file.write(data)
