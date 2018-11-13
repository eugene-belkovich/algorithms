# найти максимальный сумму элементов подмассива

def find(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)


def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    answer = find(nums)

    print('answer', answer)


main()
