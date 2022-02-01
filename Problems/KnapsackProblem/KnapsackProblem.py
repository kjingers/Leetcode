'''
We go through the list of items, calculate price by picking the item and not picking the item.

Can memoize using a (capacity, index) as the key.
- For a given capacity and index, the optimal choices of the remaining items is always the same
'''


# Brute Force Approach

def solveKnapsack(weights, prices, capacity, index):

  # Base Case. Out of capacity or no more objects
  if capacity <= 0 or index >= len(weights):
    return 0

  # If weight of item at current index is > capacity, skip to next item
  if weights[index] > capacity:
    return solveKnapsack(weights, prices, capacity, index + 1)

  # Calculate total by calling recursively two functions
  # 1. Pick item at current index
  # 2. Do not pick item at current index
  doPickItem = prices[index] + solveKnapsack(weights, prices, capacity - weights[index], index + 1)
  dontPickItem = solveKnapsack(weights, prices, capacity, index + 1)

  # We will return the max of picking vs not picking the item
  return max(doPickItem, dontPickItem)

def knapsack(weights, prices, capacity):
  
  return solveKnapsack(weights, prices, capacity, 0)
  
# With Memoization using (capacity, index) as key

def solveKnapsack(weights, prices, capacity, index, memo):

  # Base Case. Out of capacity or no more objects
  if capacity <= 0 or index >= len(weights):
    return 0
  if (capacity, index) in memo:
    return memo[(capacity, index)]


  # If weight of item at current index is > capacity, skip to next item
  if weights[index] > capacity:
    return solveKnapsack(weights, prices, capacity, index + 1, memo)

  # Calculate total by calling recursively two functions
  # 1. Pick item at current index
  # 2. Do not pick item at current index
  doPickItem = prices[index] + solveKnapsack(weights, prices, capacity - weights[index], index + 1, memo)
  dontPickItem = solveKnapsack(weights, prices, capacity, index + 1, memo)

  # We will return the max of picking vs not picking the item
  memo[(capacity, index)] = max(doPickItem, dontPickItem)
  return max(doPickItem, dontPickItem)

def knapsack(weights, prices, capacity):
  memo = {}
  return solveKnapsack(weights, prices, capacity, 0, memo)
