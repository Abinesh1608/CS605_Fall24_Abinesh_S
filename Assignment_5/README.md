## Description:
This project implements a Binary Search Tree (BST) that stores names (as keys) and phone numbers (as values). 

## It supports the following functionalities:

Inserting a new name and phone number.

Searching for a phone number given a name.

Inorder traversal to display names and phone numbers in lexicographical (sorted) order.

Deleting a node from the tree by name, while handling all edge cases.


## Features:
Create the binary search Tree
Code : bst = BinarySearchTree()

### Insert 

Adds a new node with a name and phone number in the correct lexicographical position.

code : bst.insert(name, phone_number)

### Search

Retrieves a phone number based on the name.

code : phone_number = bst.search(name)

### Inorder Traversal 

Displays all names and their associated phone numbers in sorted order.

code : bst.inorder_traversal()

### Delete 

Removes a node from the tree based on the name, handling nodes with zero, one, or two children.

code: bst.delete(name)
