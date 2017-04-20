class LNode(object):
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def __str__(self):
        return str(self.val)


class LinkList(object):
    """
    Linked List with head
    """

    def __init__(self):
        self.head = LNode(0)
        self.__length = 0

    def __len__(self):
        return self.__length

    def initlist(self, data):
        p = self.head
        for d in data:
            self.__length += 1
            p.next = LNode(d)
            p = p.next

    def print(self):
        arr = []
        p = self.head.next
        while p:
            arr.append(p.val)
            p = p.next
        print(' -> '.join(map(lambda x: str(x), arr)))

    def lastk(self, k):
        """倒数第k个，考虑k的各种取值"""
        if k <= 0:
            return
        p = self.head
        q = p
        for i in range(k):
            p = p.next
            if p is None:
                return
        while p:
            p = p.next
            q = q.next
        return q.val

    def empty(self):
        return True if self.head.next is None else False

    def clear(self):
        self.head.next = None

    def append(self, item):
        p = self.head
        if p.next is None:
            p.next = LNode(item)
        else:
            while p.next is not None:
                p = p.next
            p.next = LNode(item)
        self.__length += 1

    def pop(self):
        if self.empty():
            return
        q = None
        p = self.head
        while p.next is not None:
            q = p
            p = p.next
        self.__length -= 1
        q.next = None
        return p.val

    def popleft(self):
        if self.empty():
            return
        p = self.head.next
        self.head.next = p.next
        self.__length -= 1
        p.next = None
        return p.val

    def insert(self, index, item):
        if index < 0 or index > self.__len__():
            raise ValueError("index error")
        q, p, r = self._qpr(index)
        node = LNode(item)
        if q is None:
            self.head.next = node
        else:
            q.next = node
        node.next = p
        self.__length += 1

    def delete(self, index):
        if index < 0:
            raise ValueError("index error")
        if self.empty() or index >= self.__length:
            return
        q, p, r = self._qpr(index)
        if q is None:
            self.head.next = r
        else:
            q.next = r
        p.next = None
        del p
        self.__length -= 1

    def _qpr(self, index):
        """
        index指向的节点 p，前节点q，后节点r
        q == None, p指向头节点
        r == None, p指向尾节点
        :param index: index of p
        :return: (q, p, r)
        """
        q, p, r = None, None, None
        if self.empty() or index < -1 or index > self.__length:
            return q, p, r
        elif index == -1:
            return q, p, self.head.next
        else:
            p = self.head.next
            r = p.next
            for _ in range(index):
                q = p
                p = p.next
                r = p.next if p is not None else None
            return q, p, r

    def print_reverse(self):
        stack = []
        p = self.head.next
        while p is not None:
            stack.append(p.val)
            p = p.next
        print(' -> '.join(stack[::-1]))

if __name__ == '__main__':
    link = LinkList()
    link.initlist(['A'])
    link.insert(1, 'B')
    link.insert(1, 'C')
    link.insert(3, 'D')
    link.print()
    link.print_reverse()