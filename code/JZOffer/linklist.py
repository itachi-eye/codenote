"""
1. 链表长度
2. 列表初始化
3. 结尾插入
4. 结尾弹出
5. 开头弹出
6. 插入
7. 删除
8. 反转，三指针，递归
9. 定位中间，倒数第k个
10.是否有环
"""


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

    def __len__(self):
        p = self.head.next
        lth = 0
        while p is not None:
            lth += 1
            p = p.next
        return lth

    def initlist(self, data):
        """
        列表初始化
        """
        p = self.head
        for d in data:
            p.next = LNode(d)
            p = p.next

    def print(self):
        """
        打印
        """
        arr = []
        p = self.head.next
        while p:
            arr.append(p.val)
            p = p.next
        print(' -> '.join(map(lambda x: str(x), arr)))

    def empty(self):
        """
        是否为空
        """
        return True if self.head.next is None else False

    def clear(self):
        """
        清除所有元素
        """
        self.head.next = None

    def append(self, item):
        """
        结尾插入一个
        """
        p = self.head
        if p.next is None:
            p.next = LNode(item)
        else:
            while p.next is not None:
                p = p.next
            p.next = LNode(item)

    def pop(self):
        """
        结尾弹出一个，O(n)
        """
        if self.empty():
            return
        q = None
        p = self.head
        while p.next is not None:
            q = p
            p = p.next
        q.next = None
        return p.val

    def popleft(self):
        """
        开头弹出一个，O(1)
        """
        if self.empty():
            return
        p = self.head.next
        self.head.next = p.next
        p.next = None
        return p.val

    def insert(self, index, item):
        """
        在位置index处插入一个元素
        """
        if index < 0 or index > self.__len__():
            raise ValueError("index error")
        q, p, r = self._qpr(index)
        node = LNode(item)
        if q is None:
            self.head.next = node
        else:
            q.next = node
        node.next = p

    def delete(self, index):
        """
        在index位置插入一个元素
        """
        if index < 0 or index >= self.__len__():
            raise ValueError("index error")
        if self.empty():
            return
        q, p, r = self._qpr(index)
        if q is None:
            self.head.next = r
        else:
            q.next = r
        p.next = None
        del p

    def _qpr(self, index):
        """
        index指向的节点 p，前节点q，后节点r
        q == None, p指向头节点
        r == None, p指向尾节点
        :param index: index of p
        :return: (q, p, r)
        """
        q, p, r = None, None, None
        if self.empty() or index < -1 or index > len(self):
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

    def __reversed__(self):
        """
        反转链表，使用三个指针，q, p, r
        """
        if self.empty():
            return
        q = self.head.next
        p = q.next
        if p is None:
            return  # 只有一个节点
        r = p.next
        q.next = None  # 第一个节点next为空
        while p is not None:
            p.next = q
            q = p
            p = r
            r = r.next if r is not None else None
        self.head.next = q

    def recv_reverse(self):
        """
        反转链表，递归
        """
        tail = self._recv_reverse(self.head.next)
        tail.next = None

    def _recv_reverse(self, node):
        """
        递归求反转链表
        """
        if node.next is None:
            self.head.next = node
            return node
        pn = self._recv_reverse(node.next)
        pn.next = node
        return node

    def print_reverse(self):
        """
        倒序打印
        """
        stack = []
        p = self.head.next
        while p is not None:
            stack.append(p.val)
            p = p.next
        print(' -> '.join(stack[::-1]))

    def fetch_middle(self):
        """
        定位中间，快慢指针
        """
        q, p = self.head, self.head
        while p is not None:
            q = q.next
            p = p.next
            if p is not None:
                p = p.next
            else:
                break
        print(q.val)

    def fetch_lastk(self, k):
        """
        倒数第k个，考虑k的各种取值
        :param k: 位置
        """
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

    def has_circle(self):
        """
        是否有环，快慢指针
        """
        q, p = self.head, self.head.next
        # a = LNode('A')
        # b = LNode('B')
        # c = LNode('C')
        # d = LNode('D')
        # a.next = b
        # b.next = c
        # c.next = d
        # d.next = a
        # head = LNode(0)
        # head.next = a
        # q, p = head, head.next
        while q is not None:
            if p is q:
                return True
            q = q.next
            p = p.next
            if p is not None:
                p = p.next
            else:
                return False


if __name__ == '__main__':
    link = LinkList()
    link.initlist('abcd')
    link.insert(4, 'A')
    link.print()
    print(len(link))
