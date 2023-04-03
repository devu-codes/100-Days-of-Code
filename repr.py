# Define Tree Node
class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None

class Tree:
    # traversal
    def preorder_Rec(self, root):
        if not root:
            return None 
        print(root.val)
        self.preorder_Rec(root.left)
        self.preorder_Rec(root.right)
    # Append right root first then left
    def preorder_Iter(self, root):
        if not root:
            return None 
        stack = []
        stack.append(root)

        while stack:
            temp = stack.pop()
            print(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
    
    # left, root, right
    def inorder_Rec(self, root): 
        if not root:
            return None
        self.inorder_Rec(root.left)
        print(root.val)
        self.inorder_Rec(root.right)
    
    def inorder_Iter(self, root):
        if not root:
            return None
        temp = root 
        stack = []
        while True:
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                if not stack: break
                temp = stack.pop()
                print(temp.val)
                temp = temp.right

    # BFS 
    def level_order(self, root):
        if root:
            queue = []
            queue.append(root)
            while queue:
                tmp = queue[0]
                queue.pop(0)
                print(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
    
    def postorder_rec(self, root):
        if root:
            self.postorder_rec(root.left)
            self.postorder_rec(root.right)
            print(root.val)
    
    def postorder_Iter(self, root):
        if root:
            stack1, stack2 = [], []
            stack1.append(root)
            while stack1:
                temp = stack1.pop()
            


















