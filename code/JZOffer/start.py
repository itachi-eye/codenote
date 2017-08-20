def reverse_list(arr, st, end):
    while st < end:
        arr[st], arr[end] = arr[end], arr[st]
        st += 1
        end -= 1


def reverse_sentence(s):
    sl = list(s)
    lth = len(sl)
    reverse_list(sl, 0, lth - 1)
    p, r = 0, 0
    while p < lth:
        if sl[p] == ' ':
            p, r = p + 1, r + 1
        elif (r < lth and sl[r] == ' ') or (r >= lth):
            reverse_list(sl, p, r - 1)
            p, r = r + 1, r + 1
        else:
            r = r + 1
    print(''.join(sl))


if __name__ == '__main__':
    reverse_sentence('student.')
