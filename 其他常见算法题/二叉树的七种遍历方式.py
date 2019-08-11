class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class btree(object):
    def front_traversal_recursive(self, root_node):
        if root_node is None:
            return
        print(root_node.data, end=' ')
        self.front_traversal_recursive(root_node.left)
        self.front_traversal_recursive(root_node.right)

    def front_traversal_loop(self, root_node):
        if root_node is None:
            return
        my_stack = []
        node = root_node
        while node or my_stack:
            while node:  # search the left child tree from the root node
                print(node.data, end=' ')
                my_stack.append(node)
                node = node.left
                # when the last node has no left child, jump out of the while loop
            node = my_stack.pop()
            node = node.right  # begin to search the right child

    def middle_traversal_recursive(self, root_node):
        if root_node is None:
            return
        self.middle_traversal_recursive(root_node.left)
        print(root_node.data, end=' ')
        self.middle_traversal_recursive(root_node.right)

    def middle_traversal_loop(self, root_node):
        if root_node is None:
            return
        my_stack = []
        node = root_node
        while node or my_stack:
            while node:
                my_stack.append(node)
                node = node.left
            node = my_stack.pop()
            print(node.data, end=' ')
            node = node.right

    def last_traversal_recursive(self, root_node):
        if root_node is None:
            return
        self.last_traversal_recursive(root_node.left)
        self.last_traversal_recursive(root_node.right)
        print(root_node.data, end=' ')

    def last_traversal_loop(self, root_node):
        """
        借助my_stack1找出后序遍历的逆序，即根节点 -> 右子节点 -> 左子节点，存在my_stack2中。
        每遍历到一个节点，就把其左右节点加入my_stack1，当前节点加入my_stack2。接下来访问stack1的最近加进去的节点（右节点）...
        """
        if root_node is None:
            return
        node = root_node
        my_stack1 = []
        my_stack2 = []
        my_stack1.append(node)
        while my_stack1:  # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = my_stack1.pop()
            if node.left:
                my_stack1.append(node.left)  # 先加左子节点
            if node.right:
                my_stack1.append(node.right)  # 再加右子节点
            my_stack2.append(node)
        while my_stack2:  # 将myStack2中的元素出栈，即为后序遍历次序
            print(my_stack2.pop().data, end=' ')

    def level_queue(self, root_node):
        """
        Implements level traversal using queue
        """
        if root_node is None:
            return
        my_queue = []
        node = root_node
        my_queue.append(node)
        while my_queue:
            node = my_queue.pop(0)
            print(node.data, end=' ')
            if node.left is not None:
                my_queue.append(node.left)
            if node.right is not None:
                my_queue.append(node.right)

    def houxuxunhuan(self, root_node):
        my_stack_1 = []  # 用于中间变量
        my_stack_2 = []  # 用于存放逆序结果
        result = []
        if root_node is None:
            return []
        node = root_node
        while node or my_stack_1:
            while node:
                my_stack_1.append(node)
                my_stack_2.append(node)
                node = node.right
            node = my_stack_1.pop()
            node = node.left
        while my_stack_2:
            result.append(my_stack_2.pop().data)
        return result

    def qianxuxunhuan(self, root_node):
        if root_node is None:
            return []
        my_stack = []
        result = []
        node = root_node
        while node or my_stack:
            while node:
                result.append(node.data)
                my_stack.append(node)
                node = node.left
            node = my_stack.pop()
            node = node.right
        return result

    def cenxu(self, root_node):
        if root_node is None:
            return []
        queue = []
        res = []
        node = root_node
        queue.append(node)
        while queue:
            node = queue.pop(0)
            res.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res




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

s = btree()
print(s.houxuxunhuan(n1))
s.last_traversal_loop(n1)
print(s.qianxuxunhuan(n1))
s.front_traversal_loop(n1)
print(s.cenxu(n1))
s.level_queue(n1)