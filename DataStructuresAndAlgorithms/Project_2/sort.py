"""
Project 2: Benchmark sorting algorithms
"""
#import modules
from time import perf_counter
from random import seed, sample

def quicksort(lyst):
    """implement quicksort, return the sorted list"""
    less = []
    equal = []
    greater = []

    if len(lyst) > 1:
        pivot = lyst[0]
        for i in lyst:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                greater.append(i)
        return quicksort(less)+equal+quicksort(greater)

    return lyst

def mergesort(lyst):
    """implement mergesort, return the sorted list"""

    def merge(left, right):
        temp = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                temp.append(left[i])
                i = i + 1
            else:
                temp.append(right[j])
                j = j + 1
        while i < len(left):
            temp.append(left[i])
            i += 1
        while j < len(right):
            temp.append(right[j])
            j += 1
        return temp

    if len(lyst) < 2:
        return lyst
    left = lyst[:len(lyst)//2]
    right = lyst[len(lyst)//2:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left,right)

def selection_sort(lyst):
    """implement selection sort, return sorted list"""
    # Selection sort in Python
    size = len(lyst)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # select the minimum element in each loop
            if lyst[i] < lyst[min_idx]:
                min_idx = i

        # put min at the correct position
        (lyst[step], lyst[min_idx]) = (lyst[min_idx], lyst[step])
    return lyst

def insertion_sort(lyst):
    """implement insertion sort, return sorted list"""
    for i in range(1, len(lyst)):
        value = lyst[i]
        j = i - 1
        while j >= 0 and value < lyst[j]:
            lyst[j + 1] = lyst[j]
            j -= 1
        lyst[j + 1] = value

    return lyst

def timsort(lyst):
    """python built in timsort method"""
    lyst.sort()
    return lyst

def is_sorted(lyst):
    """Returns True is list is sorted, false otherwise."""
    # check sorted list
    if type(lyst) is not list:
        return False
    flag = 0
    i = 1
    while i < len(lyst):
        #check if instance is an integer
        if isinstance(i,int) is False:
            return False
        if lyst[i] < lyst[i - 1]:
            flag = 1
        i += 1
    if not flag :
        return True
    return False

def main():
    """main program"""
    #create data table
    data_size = 10000
    seed(0)
    data = sample(range(data_size * 3), k=data_size)

    #selection result
    print()
    test1 = data.copy() # don’t sort DATA, sort a copy of DATA
    print("starting selection_sort")
    start = perf_counter()
    sorted_list = selection_sort(test1)
    end = perf_counter()
    result = round(end - start,2)
    print(f"selection_sort duration: {result} seconds.")
    print(is_sorted(sorted_list))

    #insertion result
    print()
    test2 = data.copy() # don’t sort DATA, sort a copy of DATA
    print("starting insertion_sort")
    start  =  perf_counter()
    sorted_list = insertion_sort(test2)
    end = perf_counter()
    result = round(end - start,2)
    print(f"insertion_sort duration: {result} seconds.")
    print(is_sorted(sorted_list))

    #mergesort result
    print()
    test3 = data.copy() # don’t sort DATA, sort a copy of DATA
    print("starting mergesort")
    start  =  perf_counter()
    sorted_list = mergesort(test3)
    end = perf_counter()
    result = round(end - start,2)
    print(f"mergesort duration: {result} seconds.")
    print(is_sorted(sorted_list))

    #quicksort result
    print()
    test4 = data.copy() # don’t sort DATA, sort a copy of DATA
    print("starting quicksort")
    start  =  perf_counter()
    sorted_list = quicksort(test4)
    end = perf_counter()
    result = round(end - start,2)
    print(f"quicksort duration: {result} seconds.")
    print(is_sorted(sorted_list))

    #timsort result
    print()
    test5 = data.copy() # don’t sort DATA, sort a copy of DATA
    print("starting timsort")
    start  =  perf_counter()
    sorted_list = timsort(test5)
    end = perf_counter()
    result = round(end - start,2)
    print(f"timsort duration: {result} seconds.")
    print(is_sorted(sorted_list))
    print()

if __name__ == "__main__":
    main()
