from random import seed, sample
from time import perf_counter
"""
Project 2: Benchmarking Sorting Algoritms
"""

def quicksort(lyst):
    #quicksort_helper(lyst,0,len(lyst)-1)

    return lyst

def quicksort_helper(lyst,low,high):
    if low > high:
        return False
    else:
        high_index = partitioner(lyst,low,high)
        quicksort_helper(lyst,low,high_index)
        quicksort_helper(lyst,high_index +1, high)

def mergesort(lyst):
    pass

def selection_sort(lyst):
    pass


def insertion_sort(lyst):
    
    
    return lyst

def partitioner(lyst,low_index,high_index):
    mid = (low_index + high_index) // 2
    pivot_value = lyst[mid]
    
    while True:
        while lyst[low_index] < pivot_value:
            low_index += 1

        while lyst[high_index] > pivot_value:
            low_index -= 1

        if low_index > high_index:
            break
        else:
            # swap
            lyst[low_index], lyst[high_index] = lyst[high_index], lyst[low_index]
            low_index += 1
            high_index -= 1

def is_sorted(lyst):
	if type(lyst) is not list:
		return False
	for i in range(len(lyst)-1):
		if type(lyst[i]) is not int:
			return False
		if lyst[i] > lyst[i+1]:
			return False

def main():
    DATA_SIZE = 100000
    seed(0)
    DATA = sample(range(DATA_SIZE * 3),k=DATA_SIZE)
    test = DATA.copy() # dont sort DATA, sort the copy of data
    print()
    print("Starting selection_sort")
    start = perf_counter()
    test = selection_sort(test)
    stop = perf_counter()
    print("Selection_sort durtion: ",round(stop-start,4),"seconds.")
    print()
    print("starting insertion sort")
    start = perf_counter()
    test = insertion_sort(test)
    stop = perf_counter()
    print("Insertion_sort duration: ",round(stop-start,4),"seconds.")
    print()
    print("starting selection sort")

if __name__ == "__main__":
    main()
