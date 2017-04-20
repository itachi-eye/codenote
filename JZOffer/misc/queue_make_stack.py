class QStack(object):
    """
    两个queue => stack
    """

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.active = self.queue1  #
        self.empty = self.queue2  # 总有一个为空

    def push(self, item):
        self.active.append(item)

    def pop(self):
        if len(self.active) == 0:
            raise ValueError("empty QStack")
        lth = len(self.active)
        for i in range(lth - 1):
            self.empty.append(self.active.pop(0))
        v = self.active.pop(0)
        self.active, self.empty = self.empty, self.active  # 每次出栈，队列空满，都要交换
        print(v)
        return v


class SQueue(object):
    """
    两个stack=>queue
    """

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def offer(self, item):
        self.in_stack.append(item)

    def poll(self):
        if len(self.out_stack) == 0:
            lth = len(self.in_stack)
            for i in range(lth):
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()


if __name__ == '__main__':
    squeue = SQueue()
    squeue.offer(1)
    squeue.offer(2)
    squeue.offer(3)
    print(squeue.poll())
    squeue.offer(4)
    print(squeue.poll())
    print(squeue.poll())
    squeue.offer(5)
    print(squeue.poll())
    print(squeue.poll())

