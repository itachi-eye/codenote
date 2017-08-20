def replace_space(s):
    length = len(s)
    for i in range(length):
        if s[i] == ' ':
            s = s[:i] + '%20' + s[i + 1:]
    print(s)


def replace_space_2(s):
    spaces_cnt = 0
    for ch in s:
        if ch == ' ':
            spaces_cnt += 1
    ns = [' '] * (len(s) + 2 * spaces_cnt)
    i = len(s) - 1
    j = len(ns) - 1
    while i >= 0:
        if s[i] == ' ':
            ns[j] = '0'
            ns[j - 1] = '2'
            ns[j - 2] = '%'
            j = j - 3
        else:
            ns[j] = s[i]
            j -= 1
        i -= 1
    print(''.join(ns))
