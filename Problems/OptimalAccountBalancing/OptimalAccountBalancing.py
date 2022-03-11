'''
Need to make a dictionary of debt[i] for the ith person. Need to remove any of them that already have debt of 0.

For the Backtracking DFS, we basically want to try all combinations of paying off people starting from the left. 
    - Starting from index 0, try paying off index 1, then recursively solve. 
    - Reset payment to index 1 and try index 2. Recursively solve
        - This works, because out next recursive solve has person_id + 1, so we don't actually skip that             person's debt
    

'''

from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        # Create a dictionary of debts
        
        bals = defaultdict(int)
        
        for sender, receiver, amount in transactions:
            bals[sender] -= amount
            bals[receiver] += amount
            
        debts = [i for i in bals.values() if i != 0]
        print(debts)
        
        return self.recursive_solve(debts, 0, 0)
        
    
    def recursive_solve(self, debts, person_id, n_trans):
        
        # Skip debts that are already settled
        while person_id < len(debts) and debts[person_id] == 0:
            person_id += 1
            
        if person_id == len(debts):
            return n_trans
        
        minTrans = float('inf')
        
        
        for i in range(person_id + 1, len(debts)):
            # Only try if debts have opposite signs
            if debts[person_id] * debts[i] < 0:
                debts[i] += debts[person_id]
                candidate_min = self.recursive_solve(debts, person_id + 1, n_trans + 1)
                minTrans = min(minTrans, candidate_min)
                debts[i] -= debts[person_id]
            
        return minTrans
        
        
            
            
        
        
        
