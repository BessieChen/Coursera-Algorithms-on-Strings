#Uses python2
from __future__ import print_function
import sys


text = raw_input()
n = int(raw_input())
patterns = []
for i in range(n):
    patterns.append(raw_input())

def formTrie(patterns):
    trie = {0:{}}
    node = 1
    for pattern in patterns:
        curr = 0
        for p in pattern:
            if p not in trie[curr]:
                trie[curr][p] = node
                trie[node] = {}
                node += 1
            curr = trie[curr][p]
    return trie

def patternMatch(text,patterns):
    res = []
    trie = formTrie(patterns)
    for i in range(len(text)):
        currText = text[i:]
        found = match(trie,currText,i)
        if found != None:
            res.append(found)
    return res

def match(trie,string,i):
    curr = 0
    for c in string:
        if trie[curr] == {}:
            return i
        if c in trie[curr]:
            curr = trie[curr][c]
        elif c not in trie[curr]:
            return None
    if trie[curr] == {}:
        return i
    else:
        return None

for p in patternMatch(text,patterns):
    print(p,end = " ")