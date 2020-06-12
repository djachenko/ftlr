from argparse import ArgumentParser
from glob import iglob
from pathlib import Path

from ftlr import config
from ftlr.modifier import Modification, Modifier
from ftlr.xmp import Xmp


def run():
    print("running")

    parser = ArgumentParser()

    short_prefix = "-"
    long_prefix = "--"

    flag_names = []

    for path, flag, xmp_type, flag_type in config.CONFIG:
        parser.add_argument(short_prefix + flag[0], long_prefix + flag, type=flag_type)

        flag_names.append((flag, path, xmp_type))

    parser.add_argument("pattern", type=str, nargs="?", default="*")

    namespace = parser.parse_args()

    modifications = []

    for flag, path, xmp_type in flag_names:
        if flag not in namespace:
            continue

        value = getattr(namespace, flag)

        if value is None:
            continue

        modification = Modification(path, xmp_type, value)

        modifications.append(modification)

    modifier = Modifier(modifications)

    for str_path in iglob(namespace.pattern):
        path = Path(str_path)

        assert path.suffix == Xmp.SUFFIX

        xmp = Xmp.read(path)

        modifier.apply(xmp)

        xmp.write(path)


if __name__ == '__main__':
    run()
