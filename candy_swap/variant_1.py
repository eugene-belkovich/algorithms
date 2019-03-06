def sum(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]

    return sum


def find(A, B):
    sum_a = sum(A)
    sum_b = sum(B)

    if sum_a > sum_b:
        high_to_b = True
        high_to_a = False
    else:
        high_to_a = True
        high_to_b = False

    if high_to_a:
        diff = (sum_b - sum_a) / 2

        for i in range(0, len(A)):
            for j in range(0, len(B)):

                if B[j] - A[i] == diff:
                    return [A[i], B[j]]

    if high_to_b:
        diff = (sum_a - sum_b) / 2

        for i in range(0, len(A)):
            for j in range(0, len(B)):
                if A[i] - B[j] == diff:
                    return [A[i], B[j]]


def main():
    print('answer 1', find([1, 1], [2, 2]))

    print('answer 2', find([1, 2], [2, 3]))

    print('answer 3', find([2], [1, 3]))

    print('answer 4', find([1, 2, 5], [2, 4]))

    print('answer 5', find([20, 35, 22, 6, 13], [31, 57]))


main()
