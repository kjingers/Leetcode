'''
For minute hand: 360 / 60 = 6 degrees per minute
For hour hand: 360 / 12 = 30 degrees per hour + 30 / 60 = 0.5 degrees per minute
'''

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        minDeg = minutes * 6
        hourDeg = (hour % 12) * 30.0 + minutes * 0.5
        
        diff = abs(minDeg - hourDeg)

        return diff if diff <= 180 else (360 - diff)
        
