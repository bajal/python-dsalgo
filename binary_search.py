def binary_search(t, value):
    low = 0
    high = len(t) - 1
    while low < high:
        # Any of these work , 2&3 are to avoid overflow
        #mid = (low + high)//2
        #mid = (low + high)>>1
        mid = low + ((high - low) / 2)
        if t[mid] < value:
            low = mid + 1
        else:
            high = mid
    # at this point 'low' should point at the place
    # where the value of 'key' is possibly stored.
    return low if t[low] == value else -1

test_list = [1,3,9,11,15,19,29]
#test_list = [1,2,3]
test_val1 = 25
test_val2 = 15
test_val3 = 2

print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
print binary_search(test_list, test_val3)
