import pytest
from search import linear_search, binary_search, jump_search
from random import seed, sample
from time import perf_counter
from math import sqrt
import time
DATA_SIZE = 1000000
def make_data():
    seed(0)
    data = sample(range(DATA_SIZE * 3), k=DATA_SIZE)
    data.sort()
    while True:
        yield data
def test_search_at_end():
    gen = make_data()
    data = next(gen)
    start = time.perf_counter()
    result = binary_search(data, data[-1])
    fastest = time.perf_counter() - start
    assert result
    start = time.perf_counter()
    result = linear_search(data, data[-1])
    slowest = time.perf_counter() - start
    assert result
    assert fastest * 10000 < slowest * 10000
    start = time.perf_counter()
    result = jump_search(data, data[-1])
    fastest = time.perf_counter() - start
    assert result
    assert fastest * 10000 < slowest * 10000
def test_search_at_beginning():
    gen = make_data()
    data = next(gen)
    result = linear_search(data, data[0])
    assert result
    result = binary_search(data, data[0])
    assert result
    result = jump_search(data, data[0])
    assert result
def test_search_at_middle():
    gen = make_data()
    data = next(gen)
    result = linear_search(data, data[(DATA_SIZE // 2) - 1])
    assert result
    result = binary_search(data, data[(DATA_SIZE // 2) - 1])
    assert result
    result = jump_search(data, data[(DATA_SIZE // 2) - 1])
    assert result
def test_search_not_found():
    gen = make_data()
    data = next(gen)
    result = linear_search(data, DATA_SIZE * 4)
    assert not result
    result = binary_search(data, DATA_SIZE * 4)
    assert not result
    result = jump_search(data, DATA_SIZE * 4)
    assert not result
def test_code_style():
    from pylint.lint import Run
    results = Run(['search.py'], exit=False)
    expected = 8.5
    actual = results.linter.stats.global_note
    assert actual >= expected
