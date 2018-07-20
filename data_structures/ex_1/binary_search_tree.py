class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    if cb(self.value) is not 0:
      if self.left:
        self.left.depth_first_for_each(cb)
      if self.right:
        self.right.depth_first_for_each(cb)
    return  

  def breadth_first_for_each(self, cb):
    new_list = [self.left, self.right]
    cb(self.value)
    while len(new_list) > 0:
      cb(new_list[0].value)
      if new_list[0].left:
        new_list.append(new_list[0].left)
      if new_list[0].right:
        new_list.append(new_list[0].right)

      new_list.pop(0)





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
