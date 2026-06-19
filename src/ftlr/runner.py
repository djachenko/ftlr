from argparse import ArgumentParser
from glob import iglob
from pathlib import Path

from ftlr import config
from ftlr.modification import Modification
from ftlr.xmp import Xmp


def run():
    print("running")

    parser = ArgumentParser()

    for cfg in config.CONFIG:
        parser.add_argument(*cfg.args, **cfg.kwargs)

    # parser.add_argument("pattern", type=Path, nargs="?", default=Path.cwd() / "*")
    parser.add_argument("pattern", nargs="?", default="*")

    namespace = parser.parse_args("-e -1.5 ../../25.*/*.xmp".split())

    modifications = [mod for mod in vars(namespace).values() if isinstance(mod, Modification)]

    for str_path in iglob(namespace.pattern):
        path = Path(str_path)

        assert path.suffix == Xmp.SUFFIX

        with Xmp.read(path) as xmp:
            for modification in modifications:
                modification.apply(xmp)

                # if error:



if __name__ == '__main__':
    run()
