def find(nums):
    one_max = -10*10
    two_max = -10*10
    three_max = -10*10

    one_min = 10*10
    two_min = 10*10

    for i in range(0, len(nums)):
        cur = nums[i]
        temp3 = three_max
        three_max = max(three_max, cur)
        temp2 = two_max
        two_max = max(two_max, temp3)
        one_max = max(one_max, temp2)

        temp_min1 = one_min
        one_min = min(one_min, cur)

        temp_min2 = two_min
        two_min = min(two_min, temp_min1)

    print(one_max)
    print(two_max)
    print(three_max)
    
    res1 = temp_min1 * temp_min2
    res2 = one_max * two_max * three_max

    if res1 > res2:
        return res1
    else:
        return res2


def main():
    nums = [-1,-2,-3]
    print('answer', find(nums))


main()
