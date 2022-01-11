class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Instead of passing in (start, end), we can just pass in n
# Since (end - start) is all that matters for determining the number
# of unique subtrees
def count_trees_rec(m, n):
  # First check map
  if n in m:
    return m[n]

  # Base case: If just one value, then only one possibility
  # In this case, one root with no children
  if n <= 1:
    return 1

  count = 0
  for i in range(1, n + 1):
    leftCount = count_trees_rec(m, i - 1)
    rightCount = count_trees_rec(m, n - i)
    count += leftCount * rightCount
  
  m[n] = count
  return count


def count_trees(n):
  
  # Pass in empty map to store / reuse same calculations
  return count_trees_rec({}, n)
  


def main():
  print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))


main()
