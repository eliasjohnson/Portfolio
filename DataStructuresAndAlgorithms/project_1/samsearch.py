import math
import time
import random

def linear_search(lyst, target):
    for i in range(len(lyst)):
        if lyst[i] == target:
            return 1
    return -1

def binary_search(lyst, target):
    low = 0
    high = len(lyst) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if lyst[mid] < target:
            low = mid + 1
        elif lyst[mid] > target:
            high = mid - 1
        else:
            return 1
        return -1

def jump_search(lyst, target):
    n = len(lyst)
    jump = int(math.sqrt(n))
    left, right = 0, 0

    while left < n and lyst[left] >= target:
        right = min(n - 1, left + jump)
        if lyst[left] <= target and lyst[right] >= target:
            break
        left += jump
    if left >= n or lyst[left] > target:
        return -1
    right = min(n - 1, right)
    temp = left
    while temp <= right and lyst[temp] <= target:
        if lyst[temp] == target:
            return 1
        temp += 1
    return -1

def Execute(lyst,target):
    t1=time.perf_counter()
    linear_search(lyst,target)
    t2 = time.perf_counter()
    execution_time=t2-t1
    print("Execution time for linear search is", execution_time)

    t1=time.perf_counter()
    binary_search(lyst,target)
    t2 = time.perf_counter()
    execution_time=t2-t1
    print("Execution time for binary search is", execution_time)

    t1=time.perf_counter()
    jump_search(lyst,target)
    t2 = time.perf_counter()
    execution_time=t2-t1
    print("Execution time for jump search is", execution_time)

if __name__ == "__main__":
        random.seed(1)
        lyst=random.sample(range(10000000),k=100000)
        lyst.sort()

        print("#1. Execution time of searching first element of the sorted array")
        target=lyst[0]
        Execute(lyst,target)

        print("#2. Execution time of searching middle element of the sorted array ")
        n=len(lyst)
        n//=2
        target=lyst[n]
        Execute(lyst,target)

        print("#3. Execution time of searching end element of the sorted array")
        target=lyst[-1]
        Execute(lyst,target)

        print("#4. Execution time of searching an element when number is not in sorted array")
        target=lyst[0]-1
        Execute(lyst,target)