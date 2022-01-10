def generate_valid_parentheses(num):
  result = []
  

  def dfs(curr, openCount, closedCount):

    # Base Case
    # If openCount + closedCount = 2*N, append
    if openCount == num and closedCount == num:
      result.append(''.join(curr))
      return
    
    # If haven't maxed out our openCount, append open
    if openCount < num:
      dfs(curr + ['('], openCount + 1, closedCount)

    # If we have more open than closed, then append closed
    if openCount > closedCount:
      dfs(curr + [')'], openCount, closedCount + 1)

  dfs([], 0, 0)

  return result


def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()
