'''
project 1: searching
Due date: september 10, 2022
author: Elias Johnson

project description: This project will benchmark the speed difference between
linear search, recursive binary search, and jump search.
'''
# import modules needed
import random
import math
import time

def linear_search(lyst,target):
    '''Linear search Algorithm
    Args:
        lyst (array): we are importing
        target (int): the target we are searching for

    Returns: boolean value true or false
    '''
    index = 0
    for i in lyst:
        if i == target:
            return 1
        index += 1
    return -1

def binary_search(lyst,target):
    '''Binary Search Algorithm'''
    low = 0
    high = len(lyst) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == lyst[mid]:
            return 1
        if target < lyst[mid]:
            high = mid - 1
        low = mid + 1
    return -1


def jump_search(lyst,target):
    """Jump search Algorithm

    Args:
        lyst (string): the array we are working with
        target (int): the parameter we are searching for

    Returns:
        Boolean: returns true or false
    """
    #determine best jumping block size,
    list_length = len(lyst)
    #square root of the length of the list for block size
    jump = int(math.sqrt(list_length))
    left,right = 0,0
    while left < list_length and lyst[left] >= target:
        right = min(list_length-1, left + jump)
        if lyst[left] <= target:
            break
        if lyst[right] >= target:
            break
        left += jump
    if left >= list_length or lyst[left] > target:
        return -1
    right = min(list_length-1,right)
    temp = left
    while temp <= right and lyst[temp] <= target:
        if lyst[temp] == target:
            return 1
        temp += 1
    return -1

def main():
    '''Main program where we put it all together to print results.
       We also generate the random list here.
    '''
    # creating the random number list/array
    random.seed(0)
    number_range = 1000000
    lyst_size= 1000000
    lyst = random.sample(range(number_range),lyst_size)
    
    #sort the list
    lyst.sort()
    #space for readability
    print()

    #searching for first index as target
    target = lyst[0]
    t1_start = time.perf_counter()
    linear_search(lyst,target)
    t1_stop = time.perf_counter()
    print("total elapsed time for first index element for linear search:"
          ,round((t1_stop-t1_start),2),"seconds")

    #middle index as target
    target = (len(lyst) // 2) -1
    t1_start = time.perf_counter()
    linear_search(lyst,target)
    t1_stop = time.perf_counter()
    print("total elapsed time for middle index element for linear search:"
          ,round((t1_stop-t1_start),2),"seconds")

    #last index as target
    target = lyst[-1]
    t1_start = time.perf_counter()
    linear_search(lyst,target)
    t1_stop = time.perf_counter()
    print("total elapsed time for last index element for linear search:",
          round((t1_stop-t1_start),2),"seconds")

    #a number not in the list
    target = -1
    t1_start = time.perf_counter()
    linear_search(lyst,target)
    t1_stop = time.perf_counter()
    print("total elapsed time for element not in list for linear search:",
          round((t1_stop-t1_start),2),"seconds")

    print() # to make space between the algorithms

    #now starting jump search
    #searching for first index as target
    target = lyst[0]
    t1_start = time.perf_counter()
    jump_search(lyst,target)
    t1_stop = time.perf_counter()
    print("total elapsed time for first element in list for jump search:",
          round((t1_stop-t1_start),2),"seconds")

    #searching for middle index for jump search
    target = (len(lyst) //2) -1
    t1_start = time.perf_counter()
    jump_search(lyst,target)
    t1_stop = time.perf_counter()
    print("total elapsed time for middle element in list for jump search:",
          round((t1_stop-t1_start),2),"seconds")

    #search for last index for jump search
    target = lyst[-1]
    t1_start = time.perf_counter()
    jump_search(lyst,target)
    t1_stop = time.perf_counter()
    print("total elapsed time for last index element in list for jump search:",
          round((t1_stop-t1_start),2),"seconds")

    #search for element not in list for jump search
    target = -1
    t1_start = time.perf_counter()
    jump_search(lyst,target)
    t1_stop = time.perf_counter()
    print("total elapsed time for element not in list for jump search:",
          round((t1_stop-t1_start),2),"seconds")

    #space for readability
    print()

    #search for first index for binary search
    target = lyst[1]
    t1_start = time.perf_counter()
    binary_search(lyst,target)
    t1_stop = time.perf_counter()
    print("total elapsed time for first element in list for binary search:",
          round((t1_stop-t1_start),2),"seconds")

    #search for middle index for binary search
    target = (len(lyst) //2) -1
    t1_start = time.perf_counter()
    binary_search(lyst,target)
    t1_stop = time.perf_counter()
    print("total elapsed time for middle element in list for binary search:",
          round((t1_stop-t1_start),2),"seconds")

    #search for last index for binary search
    target = lyst[-1]
    t1_start = time.perf_counter()
    binary_search(lyst,target)
    t1_stop = time.perf_counter()
    print("total elapsed time for last element in list for binary search:",
          round((t1_stop-t1_start),2),"seconds")

    #search for target not in list for binary search
    target = -1
    t1_start = time.perf_counter()
    binary_search(lyst,target)
    t1_stop = time.perf_counter()
    print("total elapsed time for element not in list for binary search:",
          round((t1_stop-t1_start),2),"seconds")

    #space for readability
    print()

#type python3 -m pytest to test code
if __name__ == "__main__":
    main()
