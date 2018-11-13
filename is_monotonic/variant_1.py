def is_monotonic(A):
    c1 = 0
    c2 = 0

    i = A[0]
    for j in range(1, len(A)):
        if i >= A[j]:
            c1 += 1
        if i <= A[j]:
            c2 += 1
        i = A[j]

    if c1 == len(A) - 1 or c2 == len(A) - 1:
        return True
    else:
        return False


def main():
    nums = [1, 1, 1, 2]
    print('answer', is_monotonic(nums))


main()
