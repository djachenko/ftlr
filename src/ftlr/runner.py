import inspect
import typer
from glob import iglob
from pathlib import Path

from ftlr import config
from ftlr.xmp import Xmp

app = typer.Typer()


def _build_run():
    cfg_by_name = {cfg.name: cfg for cfg in config.CONFIG}

    params = [
        inspect.Parameter("pattern", inspect.Parameter.POSITIONAL_OR_KEYWORD,
                          default=typer.Argument("*"), annotation=str),
        *[
            inspect.Parameter(
                cfg.name,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
                default=typer.Option(None, f"-{cfg.name[0]}", f"--{cfg.name}"),
                annotation=cfg.type.python_type | None,
            )
            for cfg in config.CONFIG
        ]
    ]

    def run(**kwargs):
        pattern = kwargs.pop("pattern")
        modifications = [
            cfg_by_name[name].build_modification(value)
            for name, value in kwargs.items()
            if value is not None
        ]

        for str_path in iglob(pattern):
            path = Path(str_path)
            assert path.suffix == Xmp.SUFFIX

            with Xmp.read(path) as xmp:
                for modification in modifications:
                    modification.apply(xmp)

    run.__signature__ = inspect.Signature(params)
    return run


app.command()(_build_run())
