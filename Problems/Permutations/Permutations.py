'''
This is permutations of a string, but very similar to permutations of a list.

Time Complexity: O(N!)
- For a string with len of 3, we have 3 calls, each with 2 calls, each with 1 call. So 3x2x1 = 3!
'''

def permutations(str):
  
  output = []
  permutations_rec(str, [], output)
  
  return output

def permutations_rec(str, currPerm, output):

  # Base Case: Empty String
  if str == "":
    output.append(''.join(currPerm))
    return
  
  # For each character in string, "DFS" to get all permutations
  # Of remaining characters after current character
  # We are passing in copy of currPerm, so no backtracking necessary
  for i in range(len(str)):
    permutations_rec(str[:i] + str[i+1:], currPerm + [str[i]], output)


