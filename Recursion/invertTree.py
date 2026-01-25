from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 将数组转换为二叉树
def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


# 将二叉树转回数组
def tree_to_array(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # 去掉末尾连续的None(优化输出，和常规测试用例格式一致)
    while result and result[-1] is None:
        result.pop()
    return result


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 递归结束条件
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root


if __name__ == '__main__':
    # 测试用例1
    root1 = build_tree([4, 2, 7, 1, 3, 6, 9])
    print(tree_to_array(Solution().invertTree(root1)))  # 输出：[4,7,2,9,6,3,1]

    # 测试用例2
    root2 = build_tree([2, 1, 3])
    print(tree_to_array(Solution().invertTree(root2)))  # 输出：[2,3,1]

    # 测试用例3
    root3 = build_tree([])
    print(tree_to_array(Solution().invertTree(root3)))  # 输出：[]
