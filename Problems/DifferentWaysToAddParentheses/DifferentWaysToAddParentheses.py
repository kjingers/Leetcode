'''
Base case: If the expression has no symbol, i.e. its a number, then there's nothing to do. Just add to result.
Recursive case: Split the expression at every symbol and evaluate the parts recursively.
Why split at every symbol? Because its analogous to adding parantheses. e.g. 1 + 2 * 3
when split at +, parts are 1 and 2 * 3 which can be written as 1 + (2 * 3)
when split at *, parts are 1 + 2 and 3 which can be written as (1 + 2) * 3
'''

def diff_ways_to_evaluate_expression(input):
  m = {}
  return dfs(m, input)
  
  return result

def dfs(m, input):
  # First check map to see if expression is already solved
  if input in m:
    return m[input]

  # Base Case: Just a number (No more operators)
  if input.isdigit():
    return [int(input)]

  ret = []
  # Now loop though input.
  # If operator, recursively solve left and right expressions
  for i, c in enumerate(input):
    if c in ("+-*"):
      leftParts = dfs(m, input[:i])
      rightParts = dfs(m, input[i+1:])
      for left in leftParts:
        for right in rightParts:
          if c == "+":
            ret.append(left + right)
          elif c == "-":
            ret.append(left - right)
          else:
            ret.append(left * right)
  m[input] = ret
  return ret
    


def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()
