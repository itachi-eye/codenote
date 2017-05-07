class MinMaxStack(object):
    """
    包含max, min函数的栈，时间复杂度O(1)
    """

    def __init__(self):
        self.data = []
        self.min_stack = []
        self.max_stack = []
        self.cur_min = float('+inf')
        self.cur_max = float('-inf')

    def push(self, item):
        self.data.append(item)
        if self.cur_min > int(item):
            self.cur_min = item
        self.min_stack.append(self.cur_min)
        if self.cur_max < int(item):
            self.cur_max = item
        self.max_stack.append(self.cur_max)

    def pop(self):
        self.min_stack.pop()
        self.max_stack.pop()
        return self.data.pop()

    def min(self):
        return self.min_stack[-1]

    def max(self):
        return self.max_stack[-1]


class Stack(object):
    pass


def is_stack_seq_legal(push_seq, pop_seq):
    aux = []
    i, j = 0, 0  # i->push_seq, j->pop_seq
    while True:
        if len(aux) > 0 and aux[-1] == pop_seq[j]:  # 辅助栈顶元素与pop相同，出栈
            aux.pop()
            j += 1  # pop前进一个
            if j == len(pop_seq):  # pop到头
                if len(aux) == 0:  # 辅助栈空，满足条件
                    return True
                else:
                    return False
        else:  # 辅助栈顶元素与pop当前不同，从push当前开始找到相同的，中间的都压栈，找不到返回False
            while i < len(push_seq):
                t = push_seq[i]
                aux.append(t)
                i += 1
                if t == pop_seq[j]:  # 找到
                    break
            else:
                return False  # 找不到


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = [4, 5, 3, 2, 1]
    r = is_stack_seq_legal(a, b)
    print(r)
