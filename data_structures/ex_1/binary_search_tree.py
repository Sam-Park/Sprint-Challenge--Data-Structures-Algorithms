class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # Sprint test solution lecture
    # left side first then right is standard
    # it is right then left in code because then left is the last thing put
    # so it is the first thing called in recursion
    ##########################
    ####### Iterative ########
    ##########################
      # stack(cache)
      #last in first out
      # got to bottom and pop each node
    stack = []
    #append the root node of our BST
    stack.append(self)
    #iterate through the elements in the stack
    while len(stack):
      current_node = stack.pop()
      #gets our most recent node and pops it
      #check to see if this node has a right child.
      if current_node.right:
        stack.append(current_node.right)
        #check to see if this node has a left child
        # if it does we add the left
      if current_node.left:
        stack.append(current_node.left)
          # dont forget to invoke CB
      cb(current_node.value) 


    ###########################  
    ######## Recursive ########
    ###########################  
    # call the CB on the current BST node
    """cb(self.value)
    if self.left:
      self.left.depth_first_for_each(cb)
      #goes to the bottom, once it reaches the bottom, invoke right side
    if self.right:
      self.right.depth_first_for_each(cb)
     """
      #as it traverses up checks if there is a right side as it moves up the left side
      # bubbles up left side via recursion
      # boxes inside box example put boxes inside box until base case is reached
      # then you have to take each box out and check it one at a time
      # unwinding of stack needs something concrete(base case)in order
      # to calculate each box(node) on the way back up(bubbling) the stack

    #############################################  
    ############ Sprint test code ##############
    #############################################  

    """if cb(self.value) is not 0:""" # this was not needed.
    """ 
      if self.left:
        self.left.depth_first_for_each(cb)
      if self.right:
        self.right.depth_first_for_each(cb)
    return  """

  def breadth_first_for_each(self, cb):
    # queue instead of stack
    # First in first out ordering
    q = []
    q.append(self)
    while len(q):
      current_node = q.pop(0)
      # popping first item in queue because we are passing in index of 0
      if current_node.left:
        #checking left side first because FIFO
        # also left to right is standard here
        # same as depth first
        q.append(current_node.left)
      if current_node.right:
        q.append(current_node.right)
      cb(current_node.value)

      #5, 3, 10, 4, 9, 11 is expected result
      
    
    
    """new_list = [self.left, self.right]
    cb(self.value)
    while len(new_list) > 0:
      cb(new_list[0].value)
      if new_list[0].left:
        new_list.append(new_list[0].left)
      if new_list[0].right:
        new_list.append(new_list[0].right)

      new_list.pop(0)
    """




  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
