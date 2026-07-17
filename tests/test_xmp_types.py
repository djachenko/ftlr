from ftlr.xmp_types import XmpReal, XmpInteger


def test_real_from_string_negative():
    assert XmpReal().from_string("-1.50") == -1.5


def test_real_from_string_positive():
    assert XmpReal().from_string("+1.50") == 1.5


def test_real_to_string_negative():
    assert XmpReal().to_string(-1.5) == "-1.5"


def test_real_to_string_positive():
    assert XmpReal().to_string(1.5) == "+1.5"


def test_real_to_string_zero():
    assert XmpReal().to_string(0.0) == "0.0"


def test_real_prepare_rounds_up():
    assert XmpReal().prepare_value(1.556) == 1.56


def test_real_prepare_rounds_down():
    assert XmpReal().prepare_value(1.554) == 1.55


def test_integer_from_string_positive():
    assert XmpInteger().from_string("+25") == 25


def test_integer_from_string_negative():
    assert XmpInteger().from_string("-100") == -100


def test_integer_to_string_negative():
    assert XmpInteger().to_string(-100) == "-100"


def test_integer_to_string_positive():
    assert XmpInteger().to_string(50) == "+50"


def test_integer_prepare_rounds():
    assert XmpInteger().prepare_value(1.7) == 2


def test_integer_prepare_rounds_negative():
    assert XmpInteger().prepare_value(-1.7) == -2
