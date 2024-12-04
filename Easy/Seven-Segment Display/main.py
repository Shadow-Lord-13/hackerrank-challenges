T = int(input())

matches = {
    "0": 6,
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6
}

for _ in range(T):
    n = input()
    count = sum(matches[num] for num in n)

    if count%2==0:
        print("1"*(count//2))
    else:
        print("7"+"1"*((count//2)-1))