class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 把数组转成二叉树的工具函数
def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        # 处理左孩子
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        # 处理右孩子
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    # 递归
    # def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    #     if not root:
    #         return False
    #     # 叶子节点
    #     if not root.left and not root.right:
    #         return root.val == targetSum
    #     targetSum -= root.val
    #     return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

    # BFS
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # 空树直接返回False
        if not root:
            return False

        # 栈：存储（当前节点，到当前节点的路径和）
        # stack = [(root, root.val)]
        #
        # while stack:
        #     curr_node, curr_sum = stack.pop()
        #     # 叶子节点
        #     if not curr_node.left and not curr_node.right:
        #         if curr_sum == targetSum:
        #             return True
        #     # 先压右孩子
        #     if curr_node.right:
        #         stack.append((curr_node.right, curr_sum + curr_node.right.val))
        #     # 再压左孩子
        #     if curr_node.left:
        #         stack.append((curr_node.left, curr_sum + curr_node.left.val))

        # 队列
        queue = [(root, root.val)]

        while queue:
            curr_node, curr_sum = queue.pop(0)
            if not curr_node.left and not curr_node.right:
                if curr_sum == targetSum:
                    return True
            if curr_node.left:
                queue.append((curr_node.left, curr_sum + curr_node.left.val))
            if curr_node.right:
                queue.append((curr_node.right, curr_sum + curr_node.right.val))

        return False


if __name__ == '__main__':
    # 测试用例1：[5,4,8,11,None,13,4,7,2,None,None,None,None,1]，target=22
    root1 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 1])
    print(Solution().hasPathSum(root1, 22))  # 输出：True

    # 测试用例2：[1,2,3]，target=5
    root2 = build_tree([1, 2, 3])
    print(Solution().hasPathSum(root2, 5))  # 输出：False
