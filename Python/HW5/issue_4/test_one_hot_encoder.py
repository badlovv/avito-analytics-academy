from one_hot_encoder import fit_transform
import pytest


def test_simple_list():
    test_list = ['abc', 'bca', 'abc']
    actual = fit_transform(test_list)
    expected = [('abc', [0, 1]),
                ('bca', [1, 0]),
                ('abc', [0, 1])]
    assert actual == expected


def test_empty():
    with pytest.raises(TypeError) as cm:
        fit_transform()
    error = cm.value
    assert isinstance(error, TypeError)


def test_string():
    test_str = 'test'
    actual = fit_transform(test_str)
    expected = [('test', [1])]
    assert actual == expected


def test_empty_list():
    empty_list = []
    actual = fit_transform(empty_list)
    expected = []
    assert actual == expected
