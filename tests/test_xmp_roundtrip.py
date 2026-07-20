import shutil
import pytest
from pathlib import Path

from ftlr.modification import Modification
from ftlr.xmp import Xmp
from ftlr.xmp_types import XmpReal, XmpInteger

FIXTURE = Path(__file__).parent / "fixtures" / "sample.xmp"


def test_roundtrip_exposure(tmp_path):
    xmp_path = tmp_path / "sample.xmp"
    shutil.copy(FIXTURE, xmp_path)

    with Xmp.read(xmp_path) as xmp:
        Modification("crs:Exposure2012", XmpReal(), -0.5, -5.0, 5.0).apply(xmp)

    content = xmp_path.read_text()
    assert 'crs:Exposure2012="-0.5"' in content
    assert 'crs:Contrast2012="+25"' in content


def test_roundtrip_contrast(tmp_path):
    xmp_path = tmp_path / "sample.xmp"
    shutil.copy(FIXTURE, xmp_path)

    with Xmp.read(xmp_path) as xmp:
        Modification("crs:Contrast2012", XmpInteger(), 15, -100, 100).apply(xmp)

    content = xmp_path.read_text()
    assert 'crs:Contrast2012="+40"' in content
    assert 'crs:Exposure2012="0.00"' in content


def test_roundtrip_only_target_line_changes(tmp_path):
    xmp_path = tmp_path / "sample.xmp"
    shutil.copy(FIXTURE, xmp_path)
    original_lines = xmp_path.read_text().splitlines()

    with Xmp.read(xmp_path) as xmp:
        Modification("crs:Exposure2012", XmpReal(), -0.5, -5.0, 5.0).apply(xmp)

    modified_lines = xmp_path.read_text().splitlines()
    changed = [i for i, (a, b) in enumerate(zip(original_lines, modified_lines)) if a != b]
    assert len(changed) == 1
    assert "Exposure2012" in modified_lines[changed[0]]


@pytest.mark.xfail(reason="bug #2: str.replace corrupts key name when value is substring of key")
def test_xmp_setitem_does_not_corrupt_key_name():
    xmp = Xmp(['   crs:Contrast2012="0"\n'])
    xmp["crs:Contrast2012"] = "+15"
    assert 'crs:Contrast2012=' in xmp._Xmp__lines[0]
