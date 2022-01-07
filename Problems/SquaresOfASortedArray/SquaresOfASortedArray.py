'''
Solution:

Sorted array. Two pointer pattern makes sense.

Since we have negative numbers, the largest square is either at the
beginning or the end of the input array.

We can have two pointers, one at each end. Each iteration, we compare
the squares of the number pointed to by each pointer. The larger square
goes to the right most available index of the solution.

Time Complexity: O(n)
Space Complexity: O(n)

'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Left points to start index. Right to end index.
        leftPointer = 0
        rightPointer = len(nums) - 1
        
        # Initialize output array. Set outputIndex to end index.
        squares = [0 for _ in nums]
        outputIndex = len(nums) - 1
        
        # <=. If the point to the same index, then we still have
        # to add that square to the ouput
        while leftPointer <= rightPointer:
            leftSquare = nums[leftPointer] * nums[leftPointer]
            rightSquare = nums[rightPointer] * nums[rightPointer]
            
            # Put the larger square to output
            # Move pointer accordingly
            if rightSquare >= leftSquare:
                squares[outputIndex] = rightSquare
                rightPointer -= 1
            else:
                squares[outputIndex] = leftSquare
                leftPointer += 1
                
            outputIndex -= 1
            
        return squares
                
        
        
