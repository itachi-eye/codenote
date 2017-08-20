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
10.节点数：所有
11.节点数：度为0（叶子），度为1，度为2
12.节点数：第k层
13.深度（高度）
14.路径：从根节点到某个节点路径
15.路径：两个节点的最低公共祖先节点
16.路径：两个节点的最短距离
17.跨度：二叉树的最大跨度
18.镜像
19.复制
20.镜像复制
21.和为某个值的路径（根-叶）
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
        重建：中序+前序，pre_arr第一个为根，中序分左右
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
        重建：中序+后序，post_arr最后一个为根，中序分左右
        """
        self.root = self._recv_in_post(in_arr, 0, len(in_arr), post_arr, 0, len(post_arr) - 1)

    def _recv_in_post(self, in_arr, inst, inend, post_arr, post, poend):
        if inst <= inend and post <= poend:
            i = in_arr.index(post_arr[poend], inst, inend + 1)  # 找根节点
            node = BTNode(post_arr[poend])
            node.left = self._recv_in_post(in_arr, inst, i - 1, post_arr, post, i - inst + post - 1)
            node.right = self._recv_in_post(in_arr, i + 1, inend, post_arr, i - inst + post, poend - 1)
            return node

    def rebuild_in_layer(self, in_arr, layer_arr):
        """
        重建：中序+层序，in_arr在layer中最前的为根，中序分左右
        """
        lth = len(in_arr)
        pos = [0] * lth
        for i in range(lth):
            pos[i] = layer_arr.index(in_arr[i])
        self.root = self._recv_in_layer(in_arr, 0, len(in_arr) - 1, layer_arr, pos)

    def _recv_in_layer(self, in_arr, st, end, layer_arr, pos):
        if st <= end:
            mi = min(pos[st:end + 1])  # layer中最靠前的为根
            ch = layer_arr[mi]
            i = in_arr.index(ch)  # 根在in_arr中的位置
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

    def _recv_size(self, node: BTNode) -> int:
        if node is None:
            return 0  # 出口
        return self._recv_size(node.left) + self._recv_size(node.right) + 1

    def deep(self):
        """
        深度 = max(左子树深度，右子树深度) + 1
        """
        return self._recv_deep(self.root)

    def _recv_deep(self, node):
        if node is None:
            return 0
        return max(self._recv_deep(node.left), self._recv_deep(node.right)) + 1

    def leaves(self):
        """
        叶子数
        """
        return self._recv_leaf(self.root)

    def _recv_leaf(self, node: BTNode) -> int:
        """
        1. node为空，返回0
        2. node为叶子，返回1
        3. node不是叶子，返回左子树的叶子数+右子树的叶子数
        """
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._recv_leaf(node.left) + self._recv_leaf(node.right)

    def degree_count(self, degree):
        if degree == 0:
            return self.leaves()
        elif degree == 1:
            return self._recv_degree_1(self.root)
        elif degree == 2:
            return self._recv_degree_2(self.root)
        else:
            raise ValueError("illegal arguments")

    def _recv_degree_1(self, node: BTNode) -> int:
        """
        1. node is null, return 0
        2. node has only one child, return the not-null one + 1
        3. node has two children, return left + right
        4. node has no child, return 0
        """
        if node is None:
            return 0
        is_left_null = node.left is None
        is_right_null = node.right is None
        if is_left_null and not is_right_null:
            return self._recv_degree_1(node.right) + 1
        elif not is_left_null and is_right_null:
            return self._recv_degree_1(node.left) + 1
        elif not is_left_null and not is_right_null:
            return self._recv_degree_1(node.left) + self._recv_degree_1(node.right)
        else:
            return 0

    def _recv_degree_2(self, node) -> int:
        if node is None:
            return 0
        if node.left is not None and node.right is not None:
            return self._recv_degree_2(node.left) + self._recv_degree_2(node.right) + 1
        else:
            return self._recv_degree_2(node.left) + self._recv_degree_2(node.right)

    def layer_count(self, layer):
        """
        第layer层的节点数
        """
        return self._recv_layer_count(self.root, 1, layer)

    def _recv_layer_count(self, node, k, layer):
        """
        node节点k=1, k跟踪每一层的高度，k==layer就是要求的层
        """
        if node is None or k < 1:
            return 0
        if k == layer:  # 第layer层，且节点存在
            return 1
        return self._recv_layer_count(node.left, k + 1, layer) + self._recv_layer_count(node.right, k + 1, layer)

    def path_node(self, target_value) -> list:
        """
        从根节点到target的路径
        """
        path = []
        found = self._recv_path_node(self.root, target_value, path)
        if found:
            print([n.val for n in path])
            return path
        else:
            print("not found")
            return []

    def _recv_path_node(self, node: BTNode, target, path: list) -> bool:
        """
        深度优先，左边一直找到头，找不到就找右边，右边找不到退一步
        """
        if node is None:
            return False
        if node.val == target:
            path.append(node)
            return True
        path.append(node)
        found = self._recv_path_node(node.left, target, path)
        if not found:
            found = self._recv_path_node(node.right, target, path)
        if not found:
            path.pop()
        return found

    def find_path_with_sum(self, expect_sum):
        """
        找出和为expect_sum的路径
        """
        path = []
        self._recv_path_total(self.root, path, 0, expect_sum)

    def _recv_path_total(self, node, path, current_sum, except_sum):
        """
        node节点处的路径path，和current_sum
        """
        if node is None:
            return

        path.append(node)  # 更新node节点处的path和sum
        current_sum += int(node.val)

        if BinaryTree.is_leaf(node) and current_sum == except_sum:  # 是否满足条件
            print('ooook', current_sum)
            print('->'.join(map(lambda x: x.val, path)))

        if node.left is not None:  # 开始递归
            self._recv_path_total(node.left, path, current_sum, except_sum)
        if node.right is not None:
            self._recv_path_total(node.right, path, current_sum, except_sum)
        path.pop()  # 左右两边都递归完了，path把node节点去掉

    @staticmethod
    def is_leaf(node):
        return True if node is not None and node.left is None and node.right is None else False

    def least_common_ancestor(self, value1, value2):
        """
        最低公共祖先节点
        """
        path1 = self.path_node(value1)
        path2 = self.path_node(value2)
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i].val != path2[i].val:
                break
            i += 1
        print(path1[i - 1].val)

    def least_distance(self, value1, value2):
        path1 = self.path_node(value1)
        path2 = self.path_node(value2)
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i].val != path2[i].val:
                break
            i += 1
        i = i - 1
        dist = path1[:i:-1] + path2[i:]
        print([n.val for n in dist])

    def max_span(self):
        """
        二叉树的最大跨度
        """
        return self._recv_max_span(self.root)

    def _recv_max_span(self, node: BTNode):
        if node is None:
            return 0, -1
        left_max_dep, left_max_dist = self._recv_max_span(node.left)
        right_max_dep, right_max_dist = self._recv_max_span(node.right)

        max_dep = max(left_max_dep, right_max_dep) + 1
        max_dist = max(max(left_max_dist, right_max_dist), left_max_dep + right_max_dep + 2)
        return max_dep, max_dist

    def mirror(self):
        """
        镜像
        """
        self._recv_mirror(self.root)

    def _recv_mirror(self, node: BTNode):
        """
        镜像，递归
        """
        if node is None:  # node为空
            return
        if node.left is None and node.right is None:  # node是叶子
            return
        node.left, node.right = node.right, node.left  # 左右交换
        if node.left is not None:
            self._recv_mirror(node.left)  # 左边镜像
        if node.right is not None:
            self._recv_mirror(node.right)  # 右边镜像

    def copy(self):
        """
        复制，返回新的根节点
        """
        return self._recv_copy(self.root)

    def _recv_copy(self, node: BTNode):
        """
        复制，递归
        :param node 旧节点
        :return 新节点
        """
        if node is None:  # 出口
            return
        nnode = BTNode(node.val + "2")  # 新节点
        nnode.left = self._recv_copy(node.left)  # 复制左边
        nnode.right = self._recv_copy(node.right)  # 复制右边
        return nnode  # 返回新节点

    def _recv_copy_mirror(self, node: BTNode):
        """
        镜像复制，递归
        :param node: 旧节点 
        :return: 新节点 
        """
        if node is None:
            return
        nnode = BTNode(node.val + "3")
        nnode.left = self._recv_copy_mirror(node.right)  # 新的左边 = 旧右边
        nnode.right = self._recv_copy_mirror(node.left)  # 新的右边 = 旧左边
        return nnode


if __name__ == '__main__':
    btree = BinaryTree()
    btree.rebuild_complete('1234x7x56xxx2')
    btree.preorder()
    btree.inorder()
    btree.postorder()
    btree.tree_print()
    btree.find_path_with_sum(13)
