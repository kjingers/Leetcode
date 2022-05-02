'''
Want to protect most amount of damage. Using against the max value is the best.
We need 1 + damage taken health

Input: damage = [2,7,4,3], armor = 4
Output: 13

[2, 7 - 4, 4, 3] -> sum = 12 damage taken. So need 13 health

So, damage taken = sum(damage) - max(maxVal - armor, 0)
'''

class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        
        total_damage = sum(damage)
        max_damage = max(damage)
        
        # We save "armor" damage if max_damage >= armor
        # Else, we save "max_damage" damage if armor > max_damage
        health_needed = total_damage - min(armor, max_damage) + 1
        return health_needed
        
        
