
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def dfs(start, end):
  result = []

  # Base Case:
  # If start > end, then subtree is None
  # Consider start == end. Then each recursive call should return None.
  # So, we will be left with a tree node with None for both left and right subtrees
  if start > end:
    result.append(None)
    return result

  # Now loop through all values, making 'i' the root of the tree
  for i in range(start, end + 1):

    # Get all possible left and right subtrees
    # For left, try each value at root (start, start+1, start+2, ... i-1)
    # Similar for right
    leftSubtrees = dfs(start, i - 1)
    rightSubtrees = dfs(i + 1, end)

    # Create all possible trees with i as root
    # Combine all possible left subtrees with all possible rightsubtrees
    for leftSubtree in leftSubtrees:
      for rightSubtree in rightSubtrees:
        root = TreeNode(i)
        root.left = leftSubtree
        root.right = rightSubtree
        result.append(root)

  return result

def find_unique_trees(n):
  
  return dfs(1, n)




def main():
  print("Total trees: " + str(len(find_unique_trees(2))))
  print("Total trees: " + str(len(find_unique_trees(3))))


main()
