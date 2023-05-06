from time import perf_counter
from random import seed, sample

def insertion_sort(lyst):
    """implement insertion sort, return sorted list"""
    #todo finish insertion sort  
    # Outer loop to traverse through 1 to len(list1)  
    for i in range(1, len(lyst)):
        value = lyst[i]
        j = i - 1
        while j >= 0 and value < lyst[j]:
            lyst[j + 1] = lyst[j]
            j -= 1
        lyst[j + 1] = value

    return lyst

def is_sorted(lyst):
    """Returns True is list is sorted, false otherwise."""
    # using naive method to 
    # check sorted list
    if isinstance(lyst,list) != True:
        return False
    
    flag = 0
    i = 1
    while i < len(lyst):
        #check if instance is an integer
        if isinstance(i,int) == False:
            return False
        if(lyst[i] < lyst[i - 1]):
            flag = 1
        i += 1

    if (not flag) :
        return True
    else :
        return False

def main():
    #create data table
    DATA_SIZE = 10000
    seed(0)
    DATA = sample(range(DATA_SIZE * 3), k=DATA_SIZE)
    
    #insertion result
    print()
    test2 = DATA.copy() # don’t sort DATA, sort a copy of DATA 
    print("starting insertion_sort")
    start  =  perf_counter() 
    sorted_list = insertion_sort(test2)
    end = perf_counter()
    result = round(end - start,2)
    print(f"insertion_sort duration: {result} seconds.")
    print(is_sorted(sorted_list))

if __name__ == "__main__":
    main()
