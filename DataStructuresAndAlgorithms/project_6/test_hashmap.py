
import pytest
from hashmap import HashMap

def test_empty_map():
    hm = HashMap()
    assert hm.capacity() == 7
    assert hm.size() == 0

def test_remove():
    hm = HashMap()
    keys = [(r,r) for r in (range(10))]
    values = list(range(1, 11))
    for k,v in zip(keys,values):
        hm.set(k,v)
    hm.remove((3,3))
    print(hm)
    with pytest.raises(KeyError):
        hm.get((3,3))
    assert hm.get((5,5)) == 6

def test_clear():
    hm = HashMap()
    keys = [(r,r) for r in (range(10))]
    values = list(range(1, 11))
    for k,v in zip(keys,values):
        hm.set(k,v)
    hm.clear()
    assert hm.capacity() == 7
    assert hm.size() == 0

def test_keys():
    hm = HashMap()
    keys = [(r,r) for r in (range(10))]
    values = list(range(1, 11))
    for k,v in zip(keys,values):
        hm.set(k,v)
    keys2 = hm.keys()
    keys2.sort()
    assert keys == keys2

def test_get_set():
    hm = HashMap()
    with pytest.raises(KeyError):
        hm.get((0,0))

    keys = [(r,r) for r in (range(10))]
    values = list(range(1, 11))
    for k,v in zip(keys,values):
        hm.set(k,v)
    assert hm.get((5,5)) == 6
    assert hm.get((9,9)) == 10
    hm.set((2,2), 409)
    assert hm.get((2,2)) == 409

def test_rehashing():
    keys = [(r,r) for r in (range(10))]
    values = list(range(1, 11))
    hm = HashMap()
    for k,v in zip(keys,values):
        hm.set(k,v)
    assert hm.size() == 10
    assert hm.capacity() == 13

def test_code_quality():
    from pylint.lint import Run

    results = Run(['hashmap.py'], exit=False)
    expected = 8.5
    actual = results.linter.stats.global_note
    assert actual >= expected
