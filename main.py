from argparse import ArgumentParser
from glob import iglob
from pathlib import Path

import config
from modifier import Modification, Modifier
from xmp import Xmp


def main():
    parser = ArgumentParser()

    optional_prefix = "--"

    flag_names = []

    for path, flag, xmp_type, flag_type in config.CONFIG:
        parser.add_argument(optional_prefix + flag, type=flag_type)

        flag_names.append((flag, path, xmp_type))

    # add pattern with default

    namespace = parser.parse_args("-h".split())

    modifications = []

    for flag, path, xmp_type in flag_names:
        if not hasattr(namespace, flag):
            continue

        value = getattr(namespace, flag)

        modification = Modification(path, xmp_type, value)

        modifications.append(modification)

    modifier = Modifier(modifications)

    for str_path in iglob(namespace.pattern):
        path = Path(str_path)

        assert path.suffix == Xmp.SUFFIX

        with Xmp.read(path) as xmp:
            modifier.apply(xmp)


if __name__ == '__main__':
    main()
