import re

from tree import MyTrie

with open("input.txt" , "r") as fin:
    res = []
    for line in fin:
        res += [re.sub(r'[^\w\s]','',x) for x in line.split(' ')]

t = MyTrie()

for item in res:
    t.insert(item)

print(t.search(res[0]))
t.printMaxFreq()