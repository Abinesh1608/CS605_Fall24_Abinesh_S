class TreeNode:
    def __init__(self,key,value):
        # creating a TreeNode with name , phonenumber , right , left will be useful to create nodes in BST
        self.name = key
        self.phone_number = value
        self.right = None
        self.left = None
        # right , left are initialized with NONE

class BinarySearchTree:
    def __init__(self):
        # we are initializing a empty binary search tree
        self.root = None
    
    def insert(self,name,phone_number):
        if self.root == None:
            self.root = TreeNode(name,phone_number) # Creating a node in root , if root is empty
        else:
            self._insert(self.root,name,phone_number) # if root is not empty we are calling _insert which is a private method 
            
    def _insert(self,node: TreeNode,name,phone_number): #it looks for location where we can insert based on name size
        if name < node.name: # if name is small go towards left node
            if node.left == None:
                node.left = TreeNode(name,phone_number) 
            else :
                self._insert(node.left,name,phone_number) # we do recession to keep on loking for place to insert
        elif name > node.name : # name is big go towards right
            if node.right == None:
                node.right = TreeNode(name,phone_number)
            else:
                self._insert(node.right,name,phone_number) # same as left
        else:
            node.value =phone_number
            
    def search(self,name): 
        return self._search(self.root,name) # we are calling protected function _search and passing root node

    def _search(self, node: TreeNode,name): 
        if node is None:
            return None
        elif name == node.name: # return the phone number if node name matches 
            return node.phone_number
        elif name < node.name: # same as above surf through to find the name with help of size
            return self._search(node.left,name)
        else:
            return self._search(node.right,name)
            
    def delete(self,name):
        self.root = self._delete(self.root,name) # delete node with given key
    def _delete(self, node: TreeNode,name):
        if name < node.name: # same as before surf through with size to find the target node
            node.left = self._delete(node.left,name)
        elif name > node.name:
            node.right = self._delete(node.right,name)
        else: # after target is found if it has one child we delete and return the child node
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
                            #if  it has two childs return  the smallest node in the right subtree
            min_large_node = self._min(node.right)
            # once we find the sucessor we copy its value to replace the deleted target node
            node.name = min_large_node.name
            node.phone_number = min_large_node.phone_number
            node.right = self._delete(node.right, min_large_node.name)

        return node

    def _min(self, node: TreeNode): #used to find the smallest node in the right subtree
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):  #used to retrive the whole tree inorder
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node): 
        if node:
            self._inorder_traversal(node.left) # by recurssion goes througth the tree from left next right for each node from lowest
            print(f"{node.name}: {node.phone_number}")
            self._inorder_traversal(node.right)

# Create an instance of BinarySearchTree
bst = BinarySearchTree()

# Test 1: Insert multiple nodes into the BST
bst.insert("Abhi", "123-456-7890")
bst.insert("Anand", "234-567-8901")
bst.insert("Shivam", "345-678-9012")
print("Test Case 1: Inserted nodes.")

# Test 2: Search for an existing node by name
result_search_existing = bst.search("Anand")
print(f"Test Case 2: Search for 'Anand': {result_search_existing}")

# Test 3: Search for a non-existent node by name
result_search_non_existing = bst.search("David")
print(f"Test Case 3: Search for 'David': {result_search_non_existing}")

# Test 4: Inorder traversal of the tree
print("Test Case 4: Inorder Traversal:")
bst.inorder_traversal()

# Test 5: Delete a leaf node
bst.delete("Shivam")
print("Test Case 5: Deleted 'Shivam'. Inorder Traversal after deletion:")
bst.inorder_traversal()

# Test 6: Delete a node with one child
bst.delete("Anand")
print("Test Case 6: Deleted 'Anand'. Inorder Traversal after deletion:")
bst.inorder_traversal()

# Test 7: Delete a node with two children
bst.delete("Abhi")
print("Test Case 7: Deleted 'Abhi'. Inorder Traversal after deletion:")
bst.inorder_traversal()