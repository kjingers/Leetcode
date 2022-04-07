'''
Difficult Union Find Problem.

    - Keep dict of {email : firstAccountIndex}
    - If email in dict, then union firstAccountIndex with currentAccountIndex, since we know that currentIndex and firstIndex must be merged
    - Now, for each email in our dict, we dsu.find the root index, to combine all the emails that have the same root
    - Finally, just format the output so we have [Name, sorted(emails)]

'''

class DSU:
    def __init__(self, size):
        self.parents = [x for x in range(size)]
        
    def find(self, x):
        while x != self.parents[x]:
            x = self.parents[x]
        
        return x
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        
        if xr == yr:
            return False
        
        self.parents[yr] = xr

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        numAccounts = len(accounts)
        dsu = DSU(numAccounts)
        
        # emailAddress : accountIndex
        emailGroup = {}
        
        for i in range(numAccounts):
            accountSize = len(accounts[i])
            for j in range(1, accountSize):
                email = accounts[i][j]
                
                if email in emailGroup:
                    dsu.union(emailGroup[email], i)
                else:
                    emailGroup[email] = i
          
        # Build out {index : [emails]}
        components = defaultdict(list)
        
        for email, group in emailGroup.items():
            components[dsu.find(group)].append(email)
            
        mergedAccounts = []
        for group, emails in components.items():
            name = accounts[group][0]
            mergedAccounts.append([name] + sorted(emails))
            
        return mergedAccounts
        
        
        
        
        
