from collections import Counter

def transform(s):
#Use Counster to count the frequency of all the chars in string s
    frequency = Counter(s)
#count the number of odd chars
    count_odd = sum(1 for freq in frequency.values() if freq%2 != 0)
    
#  return cost based on count_odd min is 0 and max is number of odd chars - 1
#  because we can keep atmost 1 odd_count char
    return max(0, count_odd-1)

def process():
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input()
        print(transform(s))

process()