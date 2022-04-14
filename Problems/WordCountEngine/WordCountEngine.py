'''
First, convert document to  a list of lowercase words without punction.
Create a map of {word : firstOccurance}
Counter to get freqs.
Also map each word with earliest index. 

'''
from collections import Counter

def word_count_engine(document):

  l = []
  
  # Keep Characters and spaces, put into list
  for c in document:
    if c.lower().isalpha() or c == ' ':
      l.append(c.lower())
  
  # Combine list into string. Remove 
  s = ''.join(l).split()
  
  # First Index of each word
  word_idx = {}
  for i in range(len(s)):
    if s[i] not in word_idx:
      word_idx[s[i]] = i
      
  # Create Dictionary with Counts of each word
  c = Counter(s)
  
  # Bucket Sort
  buckets = [[] for _ in range(len(s))]
  for word, count in c.items():
    buckets[count].append(word)
    
  
  # Sort each bucket by words that came first
  for bucket in buckets:
    bucket.sort(key=lambda x: word_idx[x])
  
  # Iterate backwards through buckets and add to output array
  res = []
  for i in range(len(buckets)-1, -1, -1):
    if buckets[i] is None:
      continue
    
    for word in buckets[i]:
      res.append([word, str(i)])
    
  return res

  #a = sorted(c.items(), key=lambda item: (-item[1], word_idx[item[0]] ))
  
#word_count_engine("Practice makes perfect. you'll only get Perfect by practice. just practice!")
