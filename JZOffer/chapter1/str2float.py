def str2int(s):
    """字符串转为整数"""
    if not s or not s.strip():
        return 0
    s = s.strip()
    sign = 1
    rst = 0
    if s[0] == '-':
        sign = -1
        s = s[1:]
    for ch in s:
        c = ord(ch) - ord('0')
        if c < 0 or c > 10:
            raise ValueError("illegal character")
        rst = rst * 10 + c
    return sign * rst


def str2decimal(s):
    """字符串转为纯小数"""
    if not s or not s.strip():
        return 0.0
    s = s.strip()
    sign, rst = 1, 0.0
    if s[0] == '-':
        sign = -1
        s = s[1:]
    if s[0] == '.':
        s = s[1:]
    if s[0:2] == '0.':
        s = s[2:]
    for i in range(len(s) - 1, -1, -1):
        c = ord(s[i]) - ord('0')
        rst = rst * 0.1 + c
    return 0.1 * sign * rst


def str2float(s):
    """字符串转为浮点数"""
    if not s or not s.strip():
        return 0.0
    s = s.strip()
    sign, rst, st = 1, 0.0, 0
    z, p, e = '', '', ''
    if s[0] == '-':
        sign = -1
        s = s[1:]
    for i in range(len(s)):
        ch = s[i]
        if ch == '.':
            z = s[:i]
            st = i + 1
        if ch == 'e' or ch == 'E':
            p = s[st:i]
            st = i + 1
        e = s[st:]
    z = str2int(z)
    p = str2decimal(p)
    e = str2int(e)
    rst = z + p
    return sign * rst * 10 ** e


if __name__ == '__main__':
    print(str2float('-123.45678E4 '))
