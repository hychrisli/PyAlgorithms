import sys



"""
Write a function that returns the elements on odd positions (0 based) in a list
"""
def get_odds(input):
    #code goes here
    output = []
    for i in xrange(1, len(input), 2):
        output.append(input[i])
    print (output)
    return output


"""
Write a function that returns the cumulative sum of elements in a list
"""

def get_cumulative_sum(input):

    output = []
    csum = 0
    for val in input:
        csum += val
        output.append(csum)
    print output
    return output


"""
Write a function that takes a number and returns a list of its digits
"""

def get_digits(input):
    output = []
    while input:
        output.append(input % 10)
        input /= 10

    print output
    return output[::-1]


"""
From: http://codingbat.com/prob/p126968
Return the "centered" average of an array of ints, which we'll say is
the mean average of the values, except ignoring the largest and
smallest values in the array. If there are multiple copies of the
smallest value, ignore just one copy, and likewise for the largest
value. Use int division to produce the final average. You may assume
that the array is length 3 or more.
"""

def get_center_avg(input):
    minval, maxval, sumval, n = sys.maxint, -sys.maxint,0,len(input) - 2

    for val in input:
        minval = min(minval, val)
        maxval = max(maxval, val)
        sumval += val

    return (sumval - minval - maxval ) / n



if __name__ == '__main__':

    assert get_odds([0,1,2,3,4,5]) == [1,3,5]
    assert get_odds([1,-1,2,-2]) == [-1,-2]

    assert get_cumulative_sum([1, 1, 1]) == [1, 2, 3]
    assert get_cumulative_sum([1, -1, 3]) == [1, 0, 3]

    assert get_digits(123) == [1, 2, 3]
    assert get_digits(400) == [4, 0, 0]

    assert get_center_avg([2,3,1,3,5,5]) == 3
    assert get_center_avg([2, 4, 5]) == 4