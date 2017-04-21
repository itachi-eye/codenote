"""
用数组表示n位数，进行减1操作
"""

nums = [0, 0, 1, 0, 1]

n = len(nums)
cnt = 0
j = 0
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

print(cnt)
