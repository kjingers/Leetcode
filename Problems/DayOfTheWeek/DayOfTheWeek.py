'''
Solution without knowing any formulas or imported programs.

Using knowledge of today's day and the day of the week

Using: 18, 03, 2022 is a Friday
'''

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        mons = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        isLeapYear = lambda x : 1 if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0) else 0
        
        # Calculates days since 12/31/1970
        def daysSinceStart(day, month, year):
            numDays = 0
            
            for y in range(year - 1, 1970, -1):
                numDays += 365 + isLeapYear(y)
                
            numDays += sum(mons[:month - 1])
            
            if month > 2:
                numDays += isLeapYear(year)
            
            numDays += day
            
            return numDays
        
        
        d = daysSinceStart(day, month, year)
        today = daysSinceStart(18, 3, 2022)
        day = days[(d - today) % 7]
        return day
        

        
        
    
    
        
