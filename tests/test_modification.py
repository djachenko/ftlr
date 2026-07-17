from ftlr.config import CONFIG
from ftlr.modification import Modification
from ftlr.xmp import Xmp
from ftlr.xmp_types import XmpReal


def _xmp(value: str) -> Xmp:
    return Xmp([f'   crs:Exposure2012="{value}"\n'])


def test_apply_no_clamp_returns_none():
    mod = Modification("crs:Exposure2012", XmpReal(), -1.5, -5.0, 5.0)
    assert mod.apply(_xmp("0.00")) is None


def test_apply_modifies_xmp():
    mod = Modification("crs:Exposure2012", XmpReal(), -1.5, -5.0, 5.0)
    xmp = _xmp("0.00")
    mod.apply(xmp)
    assert xmp["crs:Exposure2012"] == "-1.5"


def test_apply_clamps_to_max():
    mod = Modification("crs:Exposure2012", XmpReal(), 10.0, -5.0, 5.0)
    error = mod.apply(_xmp("0.00"))
    assert error is not None
    assert error.start_value == 10.0
    assert error.boxed_value == 5.0
    assert error.range == (-5.0, 5.0)


def test_apply_clamps_to_min():
    mod = Modification("crs:Exposure2012", XmpReal(), -10.0, -5.0, 5.0)
    error = mod.apply(_xmp("0.00"))
    assert error is not None
    assert error.boxed_value == -5.0


def test_build_modification_passes_range():
    cfg = next(c for c in CONFIG if c.name == "exposure")
    mod = cfg.build_modification(-1.5)
    assert mod.key == "crs:Exposure2012"
    assert mod.value == -1.5
    assert mod.min == -5
    assert mod.max == 5


def test_build_modification_contrast():
    cfg = next(c for c in CONFIG if c.name == "contrast")
    mod = cfg.build_modification(20)
    assert mod.key == "crs:Contrast2012"
    assert mod.min == -100
    assert mod.max == 100
