import random 
import math
import time

random.seed(0)
number_range = 1000000
lyst_size= 1000000
lyst = random.sample(range(number_range),lyst_size)
#sort the list
lyst.sort()

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
            print("True")
        index += 1            
        print("false")


target = lyst[0]
t1_start = time.perf_counter()
linear_search(lyst,target)
t1_stop = time.perf_counter()
print("total elapsed time for first index element for linear search:"
        ,round((t1_stop-t1_start),10),"seconds")