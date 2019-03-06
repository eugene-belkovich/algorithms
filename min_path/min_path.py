# task
# https://acmp.ru/index.asp?main=task&id_task=120

array = []
sum = 0
cache = []


def find_min_path(x, y):
    global array
    global cache
    global sum


    if (cache[x][y] != None):
        return cache[x][y]

    if(x == 0 and y == 0):
        value = array[x][y]
        cache[x][y] = array[x][y]
        return value
    if(x == 0):
        value = array[x][y] + find_min_path(x, y-1)
        cache[x][y] = value
        return value
    if(y == 0):
        value = array[x][y] + find_min_path(x - 1, y)
        cache[x][y] = value
        return value

    value = array[x][y] + min(find_min_path(x-1, y), find_min_path(x, y-1))
    cache[x][y] = value

    return value


def main():
    global array

    max_X, max_Y = input().split()
    max_X = int(max_X)
    max_Y = int(max_Y)

    for i in range(max_X):
        b = input().split()
        for j in range(max_Y):
            b[j] = int(b[j])
        array.append(b)

    for i in range(max_X):
        cache.append([None] * max_Y)

    print(find_min_path(max_X - 1, max_Y - 1))

main()
