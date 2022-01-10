


def find_letter_case_string_permutations(str):
  permutations = []
  n = len(str)

  def dfs(index, curr):

    # Base Case
    if index == len(str):
      permutations.append(''.join(curr))
      return
    
    # Appending current Character as is
    dfs(index + 1, curr + [str[index]])

    # If character is alphanumeric, then append the other case
    if str[index].isalpha():
      dfs(index + 1, curr + [str[index].swapcase()])
  
  dfs(0, [])

  return permutations


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()
