
import sys

def get_max(lst):
    # Don't use the max function
    max_val = -sys.maxint

    for val in lst:
        if val > max_val: max_val = val

    return max_val

def get_median(lst):
    lst.sort()
    n = len(lst)
    print(lst)

    if n % 2 == 0:
        return (lst[n/2-1] + lst[n/2]) / 2.0
    else:
        return (lst[n/2])

def get_first_uniq(lst):
    first_uniq = None
    flagger = set()

    for val in lst[::-1]:
        if val not in flagger:
            flagger.add(val)
            first_uniq = val

    return first_uniq

def get_most_freq(lst):
    most_freq_num, max_freq = None, 0
    counter = dict()

    for val in lst:
        counter[val] = counter.get(val, 0) + 1
        if counter[val] > max_freq:
            most_freq_num = val
            max_freq = counter[val]

    return most_freq_num


if __name__ == '__main__':
    # print get_max([4,5,2,1,6,8,9,10,3,2,1,2,6])
    # print get_median([4,5,2,1,6,8,9,10,3,2,1,2,6])
    # print get_median([4, 5, 2, 1, 6, 8, 9, 10, 3, 2, 1, 2, 6, 7])
    # print get_first_uniq([4,5,2,1,6,8,9,10,3,2,1,5,4,2,6])
    print get_most_freq([4,5,2,1,6,8,9,10,3,2,1,5,4,2,6])