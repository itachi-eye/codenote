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
    h = Node(3)
    g = Node(16)
    f = Node(12)
    c = Node(14, f, g)
    d = Node(4, h)
    e = Node(8)
    b = Node(6, d, e)
    a = Node(10, b, c)
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

    left_first, left_last, right_first, right_last = [None] * 4
    if node.left is not None:
        left_first, left_last = recv_trans(node.left)  # 不为空的左子树转换后的头和尾，一直深入到叶子
    if node.right is not None:
        right_first, right_last = recv_trans(node.right)  # 不为空的右子树转换后的头和尾，一直深入到叶子

    if left_last is None:  # node只有右子树
        node.right = right_first
        right_first.left = node
        return node, right_first
    elif right_first is None:  # node只有左子树
        node.left = left_last
        left_last.right = node
        return left_last, node
    else:  # node有左右子树
        left_last.right = node
        node.right = right_first
        right_first.left = node
        node.left = left_last
        return left_first, right_last


if __name__ == '__main__':
    root = init()
    trans_to_bi_linklist(root)
