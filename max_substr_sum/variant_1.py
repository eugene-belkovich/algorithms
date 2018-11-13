# найти максимальный сумму элементов подмассива

import sys

mini = sys.maxsize
maxi = -sys.maxsize - 1

precalc_arr = [] * 50000
max_sum = 0


# sums of i and i+1 elements
def precalc(nums):
    global precalc_arr

    precalc_arr.insert(0, nums[0])
    for i in range(1, len(nums)):
        precalc_arr.insert(i, precalc_arr[i - 1] + nums[i])


def find(nums):
    x = 0
    mini = 0
    for r in range(0, len(nums)):
        x = precalc_arr[r] - mini
        print('precalc_arr[r]', precalc_arr[r])
        print('mini', mini)
        print('x', x)
        minii = min(precalc_arr[r], mini)
        print('minii', minii)



    return 0


def max_substr(nums):
    if len(nums) <= 1:
        return nums[0]

    precalc(nums)

    print('init', nums)
    print('pref', precalc_arr)
    return find(nums)


def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    answer = max_substr(nums)

    print('answer', answer)


main()
