# method to calculate the max disjoint palindromic subsequences that a string can have 
def max_palindrome_seq(s):
    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    count_palin = 0

    for feq in frequency.values():
        count_palin += feq//2

    return count_palin

def process():
    test_case = int(input())

    for _ in range(test_case):
        s = input()

        print(max_palindrome_seq(s))

process()