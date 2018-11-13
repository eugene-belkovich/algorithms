def find(nums):
    precalc_arr = [] * 10000
    maxi = 0
    count = 0

    if len(nums) == 1 and nums[0] == 1:
        return 1
    if len(nums) == 1 and nums[0] == 0:
        return 0

    precalc_arr.insert(0, nums[0])

    for i in range(1, len(nums)):
        current = precalc_arr[i - 1] + nums[i]
        precalc_arr.insert(i, current)
    for i in range(0, len(nums)):
        current = precalc_arr[i]

        prev = precalc_arr[i - 1]
        if i == 0:
            prev = current

        if current > prev or (current == 1 and i == 0):
            count += 1

            if maxi < count:
                maxi += 1
        else:
            count = 0

    return maxi


def main():
    nums = [1, 0, 1, 1, 0, 1]
    print('answer', find(nums))


main()
