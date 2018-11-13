def find(nums):
    if len(nums) == 1:
        return 1
    if len(nums) == 0:
        return 0
    count = 1
    counts = []
    for i in range(0, len(nums) - 1):

        if nums[i] < nums[i + 1]:
            count = count + 1
        else:
            count = 1
        counts.append(count)

    return max(counts)


def main():
    nums = [1, 1]
    answer = find(nums)

    print('answer', answer)


main()
