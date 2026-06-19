from contextlib import contextmanager
from pathlib import Path
from typing import Any, Generator, Self, List


# todo: add context management
class Xmp:
    SEPARATOR = "/"
    SUFFIX = ".xmp"

    def __init__(self, lines: List[str]) -> None:
        super().__init__()

        self.__lines = lines

    @staticmethod
    def __value(s: str) -> (str, str):
        s = s.strip()

        key, value = s.split("=")

        value = value.strip("\"")

        return value

    def __getitem__(self, key: str) -> str:
        good_lines = [line for line in self.__lines if key in line]

        assert len(good_lines) == 1

        line = good_lines[0]

        value = Xmp.__value(line)

        return value

    def __setitem__(self, key: str, new_value: str):
        good_lines = [(index, line) for index, line in enumerate(self.__lines) if key in line]

        assert len(good_lines) == 1

        index, line = good_lines[0]

        old_value = Xmp.__value(line)

        line = line.replace(old_value, new_value)

        self.__lines[index] = line

    @classmethod
    @contextmanager
    def read(cls, path: Path) -> Generator[Self, Any, None]:
        with path.open() as xmp_file:
            lines = xmp_file.readlines()

        xmp = cls(lines)

        yield xmp

        with path.open("w") as xmp_file:
            xmp_file.writelines(xmp.__lines)
