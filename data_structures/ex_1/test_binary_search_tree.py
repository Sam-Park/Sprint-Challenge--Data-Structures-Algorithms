import unittest
from binary_search_tree import BinarySearchTree

class BinarySearchTreeTests(unittest.TestCase):
  def setUp(self):
    self.bst = BinarySearchTree(5) # init binaryseachtree node with value of 5
    #between every test you get a single binary search tree node with 5

  def test_depth_first_for_each_executes_callback(self):
    arr = []
    cb = lambda x: arr.append(x) #callback taking x input and 
    #appending it to current array

    self.bst.insert(2)
    self.bst.insert(3)
    self.bst.insert(7)
    self.bst.insert(9)
    self.bst.depth_first_for_each(cb)
    # cb starts at root(5) is going to 
    # traverse the tree goes left side to the bottom of the tree first, then right
    self.assertEqual(arr, [5, 2, 3, 7, 9]) #expected output

  def test_breadth_first_for_each_executes_callback(self):
    arr = []
    cb = lambda x: arr.append(x)
    # goes level by level
    self.bst.insert(3)
    self.bst.insert(4)
    self.bst.insert(10)
    self.bst.insert(9)
    self.bst.insert(11)
    self.bst.breadth_first_for_each(cb)

    self.assertEqual(arr, [5, 3, 10, 4, 9, 11])

if __name__ == '__main__':
  unittest.main()