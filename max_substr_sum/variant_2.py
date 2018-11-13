def find(nums):
    ans = nums[0]
    sum = 0
    min_sum = 0

    for r in range(0, len(nums)):
        sum += nums[r]
        ans = max(ans, sum - min_sum)
        min_sum = min(min_sum, sum)

    return ans


def max_substr(nums):
    answ = find(nums)
    print('answ', answ)
    return answ


def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    max_substr(nums)


main()
