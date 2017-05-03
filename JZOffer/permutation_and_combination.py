def permutation(arr):
    recv_permutation(arr, 0, len(arr))


def recv_permutation(arr, k, m):
    if k == m:
        print(arr)
    else:
        for i in range(k, m):
            arr[k], arr[i] = arr[i], arr[k]
            recv_permutation(arr, k + 1, m)
            arr[k], arr[i] = arr[i], arr[k]


def check(arr):
    f1 = (arr[0] + arr[1] + arr[2] + arr[3]) == (arr[4] + arr[5] + arr[6] + arr[7])
    f2 = (arr[1] + arr[2] + arr[5] + arr[6]) == (arr[0] + arr[3] + arr[4] + arr[7])
    f3 = (arr[2] + arr[3] + arr[6] + arr[7]) == (arr[0] + arr[1] + arr[4] + arr[5])
    return f1 and f2 and f3


if __name__ == '__main__':
    a = [1, 3, 5, 5]
    permutation(a)
