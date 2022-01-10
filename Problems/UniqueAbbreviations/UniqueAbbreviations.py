def generate_generalized_abbreviation(word):
  result = []

  def dfs(curr, index, abbrCount):

    # Base Case: If index = len(word), append result
    if index == len(word):
      if abbrCount != 0:
        curr.append(str(abbrCount))
      result.append(''.join(curr))
      return
    
    # Continue Abbreviating
    dfs(list(curr), index + 1, abbrCount + 1)

    # Finish previous abbreviation. Append current letter
    newWord = list(curr)
    if abbrCount != 0:
      newWord.append(str(abbrCount))

    dfs(newWord + [word[index]], index + 1, 0)

  dfs([], 0, 0)
  return result


def main():
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))


main()
