class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
            
        z = sorted(zip(username, timestamp, website), key = lambda x : (x[0], x[1]))
        
        users = defaultdict(list)
        
        for user, time, site in z:
            users[user].append(site)
            

        patterns = Counter()
    
        # Get 3 site combinations for each user
        for user, sites in users.items():
            three_combo = set(combinations(sites, 3))
            three_combo = Counter(three_combo)
            patterns.update(three_combo)
        
        
        # First sort decending by count. Then ascending by combination lexicographically
        sorted_dict = sorted(patterns, key = lambda x : (-patterns[x], x))
        
        return sorted_dict[0]
        
        
        
