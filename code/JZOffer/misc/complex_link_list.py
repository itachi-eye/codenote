"""
复杂链表的复制
"""


class ComplexLNode:
    def __init__(self, val, next=None, sibling=None):
        self.val = val
        self.next = next
        self.sibling = sibling

    def __str__(self):
        nv = self.next.val if self.next is not None else None
        sv = self.sibling.val if self.sibling is not None else None
        return '{val}, next={n}, sibling={s}'.format(val=self.val, n=nv, s=sv)


head = ComplexLNode(0)


def init():
    e = ComplexLNode('E')
    d = ComplexLNode('D', e)
    c = ComplexLNode('C', d)
    b = ComplexLNode('B', c)
    a = ComplexLNode('A', b)
    a.sibling = c
    b.sibling = e
    d.sibling = b
    head.next = a


def lprint(h):
    p = h.next
    while p is not None:
        print(p)
        p = p.next


def find_node(h, val):
    p = h.next
    while p is not None:
        if p.val == val:
            return p
        p = p.next
    return None


def copy1(h):
    """
    最简单复制，先复制next，O(n)，再复制sibling，O(n^2)
    时间复杂度O(n^2)，辅助空间O(1)
    """
    h1 = ComplexLNode(0)

    p = h.next
    r1 = h1
    while p is not None:  # 复制next
        n = ComplexLNode(p.val)
        r1.next = n
        r1 = r1.next
        p = p.next

    p = h.next
    p1 = h1.next
    while p is not None:  # 复制sibling
        if p.sibling is not None:
            sib1 = find_node(h1, p.sibling.val)  # 必须在已存在的链表里面找
            p1.sibling = sib1
        p = p.next
        p1 = p1.next

    return h1


def copy2(h):
    """
    辅助hash表，将<node, node'>的对应关系保存起来，在O(1)时间内找到sibling
    时间复杂度O(n)，辅助空间O(n)
    """
    h2 = ComplexLNode(0)
    aux = dict()  # 辅助hash表

    p = h.next
    r2 = h2
    while p is not None:  # 复制next
        n = ComplexLNode(p.val)
        r2.next = n
        r2 = r2.next
        aux[p] = n  # 将新旧节点的对应关系保存起来
        p = p.next

    p = h.next
    p2 = h2.next
    while p is not None:  # 复制sibling
        if p.sibling is not None:
            p2.sibling = aux[p.sibling]  # 在hash表中获取新的sibling
        p = p.next
        p2 = p2.next

    return h2


def copy3(h):
    """
    1）将新节点插在旧节点的后面，n->n'
    2）n对应n.sibling，n'对应n.sibling'
    3）计数节点是原链表，偶数节点是新链表
    时间复杂度O(n)，辅助空间O(1)
    """
    # 第一步
    p = h.next
    while p is not None:
        n = ComplexLNode(p.val + '2')
        n.next = p.next
        p.next = n
        p = n.next

    # 第二步
    p = h.next
    while p is not None:
        r = p.next
        if p.sibling is not None:
            r.sibling = p.sibling.next
        p = r.next

    # 第三步
    h3 = ComplexLNode(0)
    p = h.next
    r = p.next
    h3.next = r
    while r.next is not None:
        p.next = r.next
        p = p.next
        r.next = p.next
        r = r.next
    p.next = None

    return h3


if __name__ == '__main__':
    init()
    # lprint(head)
    head3 = copy3(head)
    lprint(head3)
