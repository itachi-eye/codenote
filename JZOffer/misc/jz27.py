"""
二叉搜索树 -> 双向链表
"""


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def init():
    e = Node(4)
    d = Node(2)
    b = Node(3, d, e)
    c = Node(6)
    a = Node(5, b, c)
    return a


def trans_to_bi_linklist(root):
    """
    将二叉搜索树转换为双向链表
    """
    first, last = recv_trans(root)
    print(first, last)
    p = first
    while p is not None:
        print(p.val, end='->')
        p = p.right
    print()
    p = last
    while p is not None:
        print(p.val, end='->')
        p = p.left


def is_leaf(node: Node):
    return True if node is not None and node.left is None and node.right is None else False


def recv_trans(node: Node):
    """
    递归，将node为节点的二叉树转换为双向链表
    :param node: 遍历到某子树的根
    :return: 转换为双向链表之后的头和尾节点，(first, last)
    """
    if is_leaf(node):  # 如果是叶子节点，转换后的头尾就是本身
        return node, node

    lhead, ltail, rhead, rtail = [None] * 4
    if node.left is not None:
        lhead, ltail = recv_trans(node.left)  # 不为空的左子树转换后的头和尾，一直深入到叶子
    if node.right is not None:
        rhead, rtail = recv_trans(node.right)  # 不为空的右子树转换后的头和尾，一直深入到叶子

    if rhead is None:  # node只有左子树
        node.left = ltail
        ltail.right = node
        return lhead, node
    elif ltail is None:  # node只有右子树
        node.right = rhead
        rhead.left = node
        return node, rtail
    else:  # node有左右子树
        ltail.right = node
        node.right = rhead
        rhead.left = node
        node.left = ltail
        return lhead, rtail


if __name__ == '__main__':
    root = init()
    trans_to_bi_linklist(root)
