"""
1. 重建：中序+前序
2. 重建：中序+后序
3. 重建：中序+层序
4. 重建：完全二叉树
5. 遍历：前序，递归
6. 遍历：中序，递归
7. 遍历：后序，递归
8. 遍历：层序，递归
9. 打印：树形
10.
11.
12.
13.
"""


class BTNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class BinaryTree(object):
    """
    二叉树
    preorder 前序    infix order 中序    post order 后序
    layer 层
    """

    def __init__(self):
        self.root = None

    def rebuild_pre_in(self, pre_arr, in_arr):
        """
        重建：中序+前序
        """
        self.root = self._recv_pre_in(pre_arr, 0, len(pre_arr) - 1, in_arr, 0, len(in_arr) - 1)

    def _recv_pre_in(self, pre_arr, prest, prend, in_arr, inst, inend):
        if prest <= prend and inst <= inend:
            i = in_arr.index(pre_arr[prest], inst, inend + 1)
            node = BTNode(pre_arr[prest])
            node.left = self._recv_pre_in(pre_arr, prest + 1, i - inst + prest, in_arr, inst, i - 1)
            node.right = self._recv_pre_in(pre_arr, i - inst + prest + 1, prend, in_arr, i + 1, inend)
            return node

    def rebuild_in_post(self, in_arr, post_arr):
        """
        重建：中序+后序 
        """
        self.root = self._recv_in_post(in_arr, 0, len(in_arr), post_arr, 0, len(post_arr) - 1)

    def _recv_in_post(self, in_arr, inst, inend, post_arr, post, poend):
        if inst <= inend and post <= poend:
            i = in_arr.index(post_arr[poend], inst, inend + 1)
            node = BTNode(post_arr[poend])
            node.left = self._recv_in_post(in_arr, inst, i - 1, post_arr, post, i - inst + post - 1)
            node.right = self._recv_in_post(in_arr, i + 1, inend, post_arr, i - inst + post, poend - 1)
            return node

    def rebuild_in_layer(self, in_arr, layer_arr):
        """
        重建：中序+层序
        """
        lth = len(in_arr)
        pos = [0] * lth
        for i in range(lth):
            pos[i] = layer_arr.index(in_arr[i])
        self.root = self._recv_in_layer(in_arr, 0, len(in_arr) - 1, layer_arr, pos)

    def _recv_in_layer(self, in_arr, st, end, layer_arr, pos):
        if st <= end:
            mi = min(pos[st:end + 1])
            ch = layer_arr[mi]
            i = in_arr.index(ch)
            node = BTNode(ch)
            node.left = self._recv_in_layer(in_arr, st, i - 1, layer_arr, pos)
            node.right = self._recv_in_layer(in_arr, i + 1, end, layer_arr, pos)
            return node

    def rebuild_complete(self, arr, placeholder='x'):
        """
        重建：完全二叉树 
        """
        length = len(arr)
        nodes = [None] * length
        for i in range(length):
            if arr[i] != placeholder:
                nodes[i] = BTNode(arr[i])
        m = (length - 3) // 2
        for i in range(m + 1):
            if nodes[i] is not None:
                nodes[i].left = nodes[2 * i + 1]
                nodes[i].right = nodes[2 * i + 2]
        self.root = nodes[0]

    def preorder(self):
        """
        遍历：前序，递归
        """
        rst = []
        self._recv_preorder(self.root, rst)
        print(rst)

    def _recv_preorder(self, node, rst: list):
        if node is not None:
            rst.append(node.val)
            self._recv_preorder(node.left, rst)
            self._recv_preorder(node.right, rst)

    def inorder(self):
        """
        遍历：中序，递归
        """
        rst = []
        self._recv_inorder(self.root, rst)
        print(rst)

    def _recv_inorder(self, node, rst: list):
        if node is not None:
            self._recv_inorder(node.left, rst)
            rst.append(node.val)
            self._recv_inorder(node.right, rst)

    def postorder(self):
        """
        遍历：后序，递归
        """
        rst = []
        self._recv_postorder(self.root, rst)
        print(rst)

    def _recv_postorder(self, node, rst: list):
        if node is not None:
            self._recv_postorder(node.left, rst)
            self._recv_postorder(node.right, rst)
            rst.append(node.val)

    def layerorder(self):
        """
        遍历：层序，递归
        """
        rst = []
        queue = [self.root]
        while len(queue) > 0:
            node = queue.pop(0)
            rst.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print(rst)

    def tree_print(self):
        """
        树形打印
        """
        self._recv_tree_print(self.root, '')

    def _recv_tree_print(self, node, prefix):
        if node is not None:
            print(prefix + node.val)
            if node.left is not None:
                self._recv_tree_print(node.left, '|   ' + prefix)
            elif node.right is not None:
                print(prefix + '\   Ø')
            if node.right is not None:
                self._recv_tree_print(node.right, '|   ' + prefix)
            elif node.left is not None:
                print(prefix + '\   Ø')

    def size(self):
        """
        节点数 = 左子树节点数 + 右子树节点数 + 1
        """
        return self._recv_size(self.root)

    def _recv_size(self, node: BTNode):
        if node is None:
            return 0  # 出口
        return self._recv_size(node.left) + self._recv_size(node.right) + 1


if __name__ == '__main__':
    btree = BinaryTree()
    btree.rebuild_complete('EAGXCXFXXBD', 'X')
    # btree.inorder()
    # btree.postorder()
    btree.tree_print()
    print(btree.size())
