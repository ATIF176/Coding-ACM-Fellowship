class Node:
    def __init__(self, vlaue):
        self.left = None
        self.data = vlaue
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)
    

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        return node
    
    def traverseInorder(self, root):
        if root is not None:
            self.traverseInorder(root.left)
            print(root.data, end=" --> ")
            self.traverseInorder(root.right)
    
    def traversePreorder(self, root):
        if root is not None:
            print(root.data, end=" --> ")
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self, root):
        if root is not None:
            self.traversePostorder(root.left)
            self.traversePostorder(root.right)
            print(root.data, end=" --> ")

    def traverseLevelorder(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while(len(queue) > 0):
            print(queue[0].data, end="-->")
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    
    def search(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        if data < root.data:
            return self.search(root.left, data)
        else:
            return self.search(root.right, data)
        
    def findMin(self, root):
        if root is None:
            return None
        if root.left is None:
            return root.data
        return self.findMin(root.left)
    
    def findMax(self, root):
        if root is None:
            return None
        if root.right is None:
            return root.data
        return self.findMax(root.right)
    
    def findHeight(self, root):
        if root is None:
            return -1
        return max(self.findHeight(root.left), self.findHeight(root.right)) + 1
    
    def delete(self, root, data):
        if root is None:
            return root
        elif data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None and root.right is None:
                del root
                root = None
            elif root.left is None:
                temp = root
                root = root.right
                del temp
            elif root.right is None:
                temp = root
                root = root.left
                del temp
            else:
                temp = self.findMin(root.right)
                root.data = temp
                root.right = self.delete(root.right, temp)
        return root
    

tree = Tree()
root = tree.createNode(5)
tree.insert(root, 10)
tree.insert(root, 3)
tree.insert(root, 4)
tree.insert(root, 1)
tree.insert(root, 11)
# tree.insert(root, 2)
# tree.insert(root, 6)
# tree.insert(root, 7)
# tree.insert(root, 8)
print("Inorder traversal ")
tree.traverseInorder(root)

print("\nPreorder traversal ")
tree.traversePreorder(root)

print("\nPostorder traversal ")
tree.traversePostorder(root)

print("\nLevelorder traversal ")
tree.traverseLevelorder(root)

print("\nSearch 4")
print(tree.search(root, 4))

print("\nSearch 10")
print(tree.search(root, 10))

print("\nFind Min")
print(tree.findMin(root))

print("\nFind Max")
print(tree.findMax(root))

print("\nHeight of tree")
print(tree.findHeight(root))

print("\nDelete 8")
tree.delete(root, 8)

