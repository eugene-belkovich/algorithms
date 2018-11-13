def find(nums):
    c1 = 0
    c2 = 0
    c3 = 0

    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1

    i = nums[0]
    for j in range(1, len(nums)):
        if i > nums[j]:
            c1 += 1
        if i < nums[j]:
            c2 += 1
        i = nums[j]

    if c1 >= c2:
        return c1
    else:
        return c2


def main():
    nums = [2,2,2,2,2]
    answer = find(nums)

    print('answer', answer)


main()
