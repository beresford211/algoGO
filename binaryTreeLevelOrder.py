from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(node):
  result = []
  queue = [node]
  while (len(queue)):
    level = []
    for tnode in queue:
      level.append(tnode.val)

      if tnode.left is not None:
        queue.append(tnode.left)
      
      if tnode.right is not None:
        queue.append(tnode.right)
    
    result.append(level)
  # TODO: Write your code here
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))

main()

