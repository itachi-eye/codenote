"""
第 6 题
根据上排给出十个数，在其下排填出对应的十个数，要求下排每个数都是先前上排那十个数在下排出现的次数。
举一个例子，
上排: 0,1,2,3,4,5,6,7,8,9
下排: 6,2,1,0,0,0,1,0,0,0
"""

result = []


def check(arr, brr):
    s1 = ''.join(map(lambda x: str(x), sorted(brr, reverse=True)))
    s2 = ''
    for j in range(len(arr)):
        s2 += str(arr[j]) * brr[j]
    return True if s1 == s2 else False


def solve(arr, brr, n, idx, s, mul):
    if idx == n and s == n and mul == n:
        if check(arr, brr):
            # print(brr, idx)
            result.append(brr.copy())
    if idx >= n:
        return
    for i in range(n + 1):
        t1 = s + i
        t2 = mul + arr[idx] * i
        if idx >= n or t1 > n or t2 > n:
            break
        else:
            brr[idx] = i
            solve(arr, brr, n, idx + 1, t1, t2)


def partition(arr, p, r, order):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] > x:
            arr[i + 1], arr[j] = arr[j], arr[i + 1]
            order[i + 1], order[j] = order[j], order[i + 1]
            i += 1
    i += 1
    arr[i], arr[r] = arr[r], arr[i]
    order[i], order[r] = order[r], order[i]
    return i


def quick_sort(arr, p, r, order):
    if p < r:
        m = partition(arr, p, r, order)
        quick_sort(arr, p, m - 1, order)
        quick_sort(arr, m + 1, r, order)


if __name__ == '__main__':
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(a)
    order = [i for i in range(len(a))]  # order记录排序之后的数字在原数组中的顺序
    quick_sort(a, 0, len(a) - 1, order)  # 倒序性能更好

    b = [0] * len(a)
    solve(a, b, len(a), 0, 0, 0)
    if result:
        for res in result:
            tmp = [0] * len(a)
            for k in order:
                tmp[order[k]] = res[k]
            print(tmp)
    else:
        print("No Answer!")
