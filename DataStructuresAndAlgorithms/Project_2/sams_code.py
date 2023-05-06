from random import seed, sample
import time


def quicksort(lyst):
    result = []
    low = []
    high = []
    temp_lyst = []

    def sort_lyst(s_lyst):
        low = []
        high = []
        pivot = 0
        i = 1
        while i < len(s_lyst):
            if s_lyst[i] > s_lyst[pivot]:
                high.append(s_lyst[i])
            else:
                low.append(s_lyst[i])
            i += 1

        low.append(s_lyst[pivot])

        if is_sorted(low):
            temp_lyst.append(low)
        else:
            sort_lyst(low)
        if is_sorted(high):
            temp_lyst.append(high)
        else:
            sort_lyst(high)

        # if is_sorted(low):
        #     if is_sorted(high):
        #         return high
        #     else:
        #         temp_lyst.append(sort_lyst(high))
        #     return low
        # else:
        #     temp_lyst.append(sort_lyst(low))

    sort_lyst(lyst)

    i = 0
    while i < len(temp_lyst):
        j = 0
        while j < len(temp_lyst[i]):
            result.append(temp_lyst[i][j])
            j += 1
        i += 1

    return result


def mergesort(lyst):
    split_lyst = []

    def half_lyst(h_lyst):
        lyst_len = len(h_lyst) // 2
        if lyst_len > 0:
            half_lyst(h_lyst[:lyst_len])
            half_lyst(h_lyst[lyst_len:])
        else:
            split_lyst.append(h_lyst)

    def sort_lyst(s_lyst):
        result = []
        if len(s_lyst) == 1:
            return s_lyst[0]
        else:
            if len(s_lyst) % 2 == 1:
                s_lyst.append([])
            i = 1
            while i < len(s_lyst):
                first_value = 0
                second_value = 0
                temp_lyst = []
                while first_value < len(s_lyst[i - 1]) or second_value < len(s_lyst[i]):
                    if len(s_lyst[i]) != 0:
                        if len(s_lyst[i - 1]) != 0:
                            if s_lyst[i - 1][first_value] < s_lyst[i][second_value]:
                                temp_lyst.append(s_lyst[i - 1][first_value])
                                if first_value + 1 < len(s_lyst[i - 1]):
                                    first_value += 1
                                else:
                                    s_lyst[i - 1] = []
                            else:
                                temp_lyst.append(s_lyst[i][second_value])
                                if second_value + 1 < len(s_lyst[i]):
                                    second_value += 1
                                else:
                                    s_lyst[i] = []
                        else:
                            temp_lyst.append(s_lyst[i][second_value])
                            if second_value + 1 < len(s_lyst[i]):
                                second_value += 1
                            else:
                                s_lyst[i] = []
                    else:
                        if first_value + 1 < len(s_lyst[i - 1]):
                            if s_lyst[i - 1][first_value] < s_lyst[i - 1][first_value + 1]:
                                temp_lyst.append(s_lyst[i - 1][first_value])
                                first_value += 1
                            else:
                                temp_lyst.append(
                                    s_lyst[i - 1][first_value + 1])
                        else:
                            temp_lyst.append(s_lyst[i - 1][first_value])
                            first_value += 1
                            s_lyst[i - 1] = []
                result.append(temp_lyst)
                i += 2
            result = sort_lyst(result)
            return result

    half_lyst(lyst)
    return sort_lyst(split_lyst)


def selection_sort(lyst):
    # Selection sort in Python
    size = len(lyst)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
        
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if lyst[i] < lyst[min_idx]:
                min_idx = i
        
        # put min at the correct position
        (lyst[step], lyst[min_idx]) = (lyst[min_idx], lyst[step])

def insertion_sort(lyst):
    result = []

    while len(lyst) > 0:
        num = lyst[0]
        i = 0

        while num == lyst[0]:
            if i == len(result):
                result.append(lyst.pop(0))
            if result[i] > num:
                result.insert(i, lyst.pop(0))
            if len(lyst) == 0:
                return result
            i += 1

def is_sorted(lyst):
    unsorted_lyst = lyst.copy()
    if not isinstance(lyst, list):
        return False

    for i in range(len(lyst)):
        if i + 1 < len(lyst):
            if not isinstance(lyst[i], int):
                return False

    for i in range(len(lyst)):
        if i + 1 < len(lyst):
            if lyst[i] > lyst[i + 1]:
                return False

    for i in range(len(lyst)):
        if lyst[i] is not unsorted_lyst[i]:
            return False
    return True

def make_data():
    data_size = 10_000
    seed(0)
    data = sample(range(data_size * 3), k=data_size)
    while True:
        yield data

def timsort(lyst):
    result = lyst.sort()
    return result

def main():
    data = make_data()
    lyst = next(data)

    test_lyst = lyst.copy()
    print("-- Quick Sort --")
    start = time.perf_counter()
    result = quicksort(test_lyst)
    end = time.perf_counter()
    run_time = end - start
    sort_result = is_sorted(result)

    print(run_time)
    print(sort_result)

    test_lyst = lyst.copy()
    print("-- Merge Sort --")
    start = time.perf_counter()
    result = mergesort(test_lyst)
    end = time.perf_counter()
    run_time = end - start
    sort_result = is_sorted(result)

    print(run_time)
    print(sort_result)

    test_lyst = lyst.copy()
    print("-- Selection Sort --")
    start = time.perf_counter()
    result = selection_sort(test_lyst)
    end = time.perf_counter()
    run_time = end - start
    sort_result = is_sorted(result)

    print(run_time)
    print(sort_result)

    test_lyst = lyst.copy()
    print("-- Insertion Sort --")
    start = time.perf_counter()
    result = insertion_sort(test_lyst)
    end = time.perf_counter()
    run_time = end - start
    sort_result = is_sorted(result)

    print(run_time)
    print(sort_result)

    test_lyst = lyst.copy()
    print("-- Tim Sort --")
    start = time.perf_counter()
    test_lyst.sort()
    end = time.perf_counter()
    run_time = end - start
    sort_result = is_sorted(test_lyst)

    print(run_time)
    print(sort_result)


if __name__ == "__main__":
    main()
