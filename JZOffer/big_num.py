def array_num_cnt(nums: list):
    """
    用数组表示n位数，进行减1操作
    """
    n = len(nums)
    cnt = 0
    while True:
        nums[0] -= 1
        if nums[0] == -1:  # 某位是-1，表示要借位了
            i = 1
            while i < n:  # 从位置1开始找，最近一个不是0的位
                if nums[i] > 0:
                    nums[i] -= 1
                    nums[0:i] = [9] * i
                    break
                i += 1
            else:  # 找到最后一位都没有大于0的，全是0，结束
                break
        cnt += 1
    return cnt


def array_num_add(num1: list, num2: list):
    """
    数组表示是两个任意数相加
    """
    lth1, lth2 = len(num1), len(num2)
    rst = [0] * (max(lth1, lth2) + 1)
    i, carry = 0, 0
    while i < lth1 or i < lth2:
        a = num1[i] if i < lth1 else 0  # 超过了就用0代替
        b = num2[i] if i < lth2 else 0  # 超过了就用0代替
        t = a + b + carry
        if t >= 10:
            carry = 1
            rst[i] = t - 10
        else:
            carry = 0
            rst[i] = t
        i += 1
    rst[i] = carry
    return rst


def array_num_sub(num1, num2):
    """
    数组表示是两个任意数相减
    """
    sign = 1
    lth1, lth2 = len(num1), len(num2)
    if lth1 < lth2:
        sign = -1
        num1, num2 = num2, num1
    elif lth1 == lth2:
        for i in range(lth1 - 1, -1, -1):
            if num1[i] < num2[i]:
                sign = -1
                num1, num2 = num2, num1
                break
    else:
        pass
    rst = [0] * max(lth1, lth2)
    i, borrow = 0, 0
    while i < lth1 or i < lth2:
        a = num1[i] if i < lth1 else 0
        b = num2[i] if i < lth2 else 0
        t = a - b - borrow
        if t < 0:
            borrow = 1
            rst[i] = t + 10
        else:
            borrow = 0
            rst[i] = t
        i += 1
    return sign, rst


def multiply_one(nums: list, n, st, rst: list):
    carry = 0
    i = 0
    for i in range(len(nums)):
        a = nums[i] * n + carry
        carry = a // 10
        rst[i + st] += a % 10
        if rst[i + st] >= 10:
            rst[i + st] -= 10
            rst[i + st + 1] += 1
    if carry > 0:
        rst[i + st + 1] += carry
    return rst


def array_num_multiply(num1, num2):
    lth1, lth2 = len(num1), len(num2)
    rst = [0] * (lth1 + lth2)
    for i in range(lth2):
        multiply_one(num1, num2[i], i, rst)
    print(rst)


def array_num_divmod(num1, num2):
    pass


if __name__ == '__main__':
    arr1 = [1, 9, 9, 1, 0, 9]
    arr2 = [0, 0, 9, 9, 9, 9, 8, 9]
    print(array_num_multiply(arr1, arr2))
