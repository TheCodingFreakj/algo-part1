# computing the sum of elements in a range [i, j]
# is equivalent to calculating
# prefix_sum[j] - prefix_sum[i-1] if i > 0,
# or just prefix_sum[j] if i = 0

def runningSum(nums):
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
        nums[i] = sum
    return nums


nums = [1, 1, 1, 1, 1]
runningSum(nums)


def largestAltitude(gain):
    sum = 0
    altitutes = [0] * (len(gain) + 1)

    for i in range(len(gain)):
        sum = sum + gain[i]
        altitutes[i+1] = sum

    return max(altitutes)


gain = [-5, 1, 5, 0, -7]
largestAltitude(gain)


def prefix_sum_left(nums):
    prefix_sums = []
    prefix_sum = 0
    
    for num in nums:
        prefix_sum += num
        prefix_sums.append(prefix_sum)
    
    return prefix_sums

def suffix_sum_right(nums):
    suffix_sums = []
    suffix_sum = 0
    
    for num in reversed(nums):
        suffix_sum += num
        suffix_sums.insert(0, suffix_sum)
    
    return suffix_sums

def pivotIndex(nums):
    left = prefix_sum_left(nums)
    right = suffix_sum_right(nums)


    for k in range(len(nums)):
        if (left[k] == right[k]):
            return k
    return -1


# nums = [1,2,3]
# nums = [2,1,-1]
nums = [1, 7, 3, 6, 5, 6]
# nums = [-1, -1, -1, -1, -1, -1]
pivotIndex(nums)
