class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, sum):
  all_paths = []

  def find_path(node, current_sum, path):
      _sum = node.val + current_sum
      path += str(node.val) + "--"
      print("what is the path", path)
      if _sum > sum: 
        return 

      if _sum == sum:
          all_paths.append(path)
          return 
    
      if node.left:
          find_path(node.left, _sum, path)
 
      if node.right:
          find_path(node.left, _sum, path)
  find_path(root, 0, "")

  return all_paths 


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))

main()

