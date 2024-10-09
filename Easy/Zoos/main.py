from collections import Counter

s = input()

freuqency = Counter(s)

x = freuqency['z']
y = freuqency['o']

if 2 * x == y:
    print("Yes")
else:
    print("No")