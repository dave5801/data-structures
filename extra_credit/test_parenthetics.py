"""Test valid parenthesis"""


def test_is_balanced():
    """Test is Balanced."""
    from balanced_parens import is_balanced
    assert is_balanced("()") == "balanced"


def test_broken():
    """Test if broken."""
    from balanced_parens import is_balanced
    assert is_balanced("))") == "broken"


def test_is_open():
    """Test is open."""
    from balanced_parens import is_balanced
    assert is_balanced("((") == "open"


def test_string_1():
    """Test from CodeWars."""
    from balanced_parens import is_balanced
    assert is_balanced(" (") == "open"


def test_string_2():
    """Test from CodeWars."""
    from balanced_parens import is_balanced
    assert is_balanced(")test") == "broken"


def test_string_3():
    """Test from CodeWars."""
    from balanced_parens import is_balanced
    assert is_balanced("") == "balanced"


def test_string_4():
    """Test from CodeWars."""
    from balanced_parens import is_balanced
    assert is_balanced("hi())(") == "broken"


def test_string_5():
    """Test from CodeWars."""
    from balanced_parens import is_balanced
    assert is_balanced("hi(hi)()") == "balanced"