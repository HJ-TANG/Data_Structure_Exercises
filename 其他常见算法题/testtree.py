class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        res = []

        def core(root):
            if not root:
                return
            core(root.left)
            res.append(root.val)
            core(root.right)

        core(pRoot)
        if k > len(res) or k <= 0:
            return None
        else:
            return res[k - 1]


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)


n1.left = n2
n1.right = n5
n2.left = n3
n2.right = n4
n3.right = n6
n4.left = n7
n5.right = n8
n6.right = n9

s = Solution()
string = s.KthNode(n1, 5)
# print(string)
# s.Mirror(n1)

# sss = [1]
# print(sss[:-1])