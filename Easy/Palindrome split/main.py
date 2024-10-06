# method to calculate the max disjoint palindromic subsequences that a string can have.
def max_palindrome_seq(s):
    frequency = {}

#loop to calculate total no. value for each chat and store it in the frequecy dir.
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    count_palin = 0


# count the palindrone with min len 2 example: if we have 3 a the it will form 1 disjoint palindrome sequence "aa"
# leaving 1 a or you can say ("aaa") since there no other char for single a to from palindrome with min len 2.
# If we have 4 a then it will form 2 disjoint palindromice seq "aa" "aa".

    for feq in frequency.values():
        count_palin += feq//2

    return count_palin

def process():
    test_case = int(input())

    for _ in range(test_case):
        s = input()

        print(max_palindrome_seq(s))

process()