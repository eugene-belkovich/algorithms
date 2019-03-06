def find(nums):
    arr = set(nums)
    print(arr)

    sorted(arr)
    v1 = arr.pop()
    v2 = arr.pop()
    v3 = arr.pop()

    return v1 * v2 * v3

def main():
    nums = [-1, -2, -3]
    print('answer', find(nums))


main()
