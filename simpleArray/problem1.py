def buildArray(nums):
    ans = [0] * len(nums)
    for i in range(len(nums)):
        ans[i] = nums[nums[i]]
    return ans


nums = [5, 0, 1, 2, 3, 4]
buildArray(nums)


def getConcatenation(nums):
    n = len(nums)
    ans = [0] * (2 * n)
    for i in range(n):
        ans[i] = nums[i]
        ans[i + n] = nums[i]

    return ans


nums = [1, 2, 1]
getConcatenation(nums)


def shuffle(nums, n):
    ans = [0] * len(nums)
    i = 0
    j = n
    k = 0
    while (j <= len(nums)-1):
        ans[k] = nums[i]
        ans[k+1] = nums[j]
        i = i+1
        j = j+1
        k = k+2
    return ans


nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
shuffle(nums, n)


def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    after_adding_candies = [0] * len(candies)
    for i in range(len(candies)):
        nums_of_candies_after_adding = candies[i] + extraCandies
        after_adding_candies[i] = nums_of_candies_after_adding

    result = [False] * len(after_adding_candies)

    for j in range(len(after_adding_candies)):
        if after_adding_candies[j] >= max_candies:
            result[j] = True
    return result

candies = [4,2,1,1,2]
extraCandies = 1
kidsWithCandies(candies, extraCandies)




def decode(encoded, first):
    arr = [first] * (len(encoded) + 1)
    for i in range(len(encoded)):
         arr[i+1] = encoded[i] ^ arr[i]

    return arr    

encoded = [1,2,3]
first = 1
decode(encoded, first)