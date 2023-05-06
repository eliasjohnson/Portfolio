'''
Project Name: Project 2: Sort Test Code
Author: George Rudolph
Date: 3 Jul 2020
Purpose:
This test code **verifies** certain expected properties and behavior of students code solution submissions
for this project, and is used to automate grading. The fact that a submission passes all these tests
means that some properites have been verified--it does **not** mean that the code is **TESTED**,
industrial-strength code.

This test code purposely avoids using requiring unit testing modules like pytest and unitttest,
because built-in assertions are sufficient here.
However, this file **can** be run without modification using pytest, to take advantage of
reporting capabilities.

This file should be made available to students so that they can test the code
in their copy of search.py. They should not modify this file test_search.py.

To run test_search from command line:
python -m pytest test_sort.py
'''

from sort import selection_sort, insertion_sort, mergesort, quicksort, is_sorted
from random import seed, sample
from time import perf_counter

def test_sort_times():
    data_size = 1000
    seed(42)
    data = sample(range(data_size * 3), k=data_size)

    # selection sort
    test = data.copy()
    start = perf_counter()
    test = selection_sort(test)
    selection_elapsed_time = perf_counter() - start
    assert is_sorted(test)

    # insertion sort
    test = data.copy()
    start = perf_counter()
    test = insertion_sort(test)
    insertion_elapsed_time = perf_counter() - start
    assert is_sorted(test)

    # merge sort
    test = data.copy()
    start = perf_counter()
    test = mergesort(test)
    merge_elapsed_time = perf_counter() - start
    assert is_sorted(test)

    # quick sort
    test = data.copy()
    start = perf_counter()
    test = quicksort(test)
    quick_elapsed_time = perf_counter() - start
    assert is_sorted(test)

    # tim sort
    test = data.copy()
    start = perf_counter()
    test.sort()
    tim_elapsed_time = perf_counter() - start

    assert merge_elapsed_time < insertion_elapsed_time
    assert quick_elapsed_time < selection_elapsed_time
    assert tim_elapsed_time < merge_elapsed_time

def test_sorted_list():
    data_size = 1000
    seed(42)
    orig_data = sample(range(data_size * 3), k=data_size)

    assert not is_sorted(orig_data)
    test_data = selection_sort(orig_data.copy())
    assert is_sorted(test_data)
    test_data = insertion_sort(orig_data.copy())
    assert is_sorted(test_data)
    test_data = mergesort(orig_data.copy())
    assert is_sorted(test_data)
    test_data = quicksort(orig_data.copy())
    assert is_sorted(test_data)

def test_code_quality():
    from pylint.lint import Run

    results = Run(['sort.py'], exit=False)
    expected = 8.5
    actual = results.linter.stats['global_note']
    assert actual >= expected


if __name__ == "__main__":
    ''' this code only executes if run as a standalone program.'''
    test_sort_times()
    test_sorted_list()
    test_code_quality()
    print("All tests pass.")
