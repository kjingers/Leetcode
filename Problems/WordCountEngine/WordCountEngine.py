'''
First, convert document to  a list of lowercase words without punction.
Counter to get freqs.
Also map each word with earliest index. 

'''

import re
from collections import OrderedDict, Counter

def word_count_engine(document):
  print(document)
  #words = re.findall(r'\w+', document.lower())
  #print(words)
  l = []
  for c in document:
    if c.lower().isalpha() or c == ' ':
      l.append(c.lower())
     
  s = ''.join(l).split()
  word_idx = {}
  for i in range(len(s)):
    if s[i] not in word_idx:
      word_idx[s[i]] = i
      
    
      
  print(s)
  c = Counter(s)  
  a = sorted(c.items(), key=lambda item: (-item[1], word_idx[item[0]] ))
  print(a)
  return [[t[0], str(t[1])] for t in a]
  #return sorted(c.items(), key=lambda item: (-item[1], word_idx[item[0]] ))
  
#word_count_engine("Practice makes perfect. you'll only get Perfect by practice. just practice!")
