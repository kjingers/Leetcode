'''
We can use 3 pointers. red = 0, white = 0, blue = n - 1
    - If num == 0, swap nums[red], num. Iterate red and white.
    - If num == 1, swap nums[white], num. Iterate white.
    - If num == 2, swap nums[blue], num. Decrement blue
    
Basically, we want to iterate through and move all 0 to left and 2 to right. We essentially ignore white. If we move all 0 to left and 2 to right, then 1 will naturally fall into middle.
    
[1, 2, 0, 1, 0]
[1, 0, 0, 1, 2]
[0, 1, 0, 1, 2]
'''



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        red, white, blue = 0, 0, n - 1
        

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -= 1
            
        
