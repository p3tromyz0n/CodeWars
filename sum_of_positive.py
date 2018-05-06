def task():
    '''
    You get an array of numbers, return the sum of all of the positives ones.

    xample [1,-4,7,12] => 1 + 7 + 12 = 20

    Note: array may be empty, in this case return 0.
    '''
    return task.__doc__

def positive_sum_long(arr):
    a = []
    if len(arr) == 0:
        return 0
    else:
        for i in arr:
            if i >= 0:
                a.append(i)
    return sum(a)

def positive_sum_short(arr):
    if len(arr) == 0:
        return 0
    else:
        return sum(i for i in arr if i >= 0)



