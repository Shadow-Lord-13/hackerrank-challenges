n = list((input()))

vow = ['A','E','I','O','U','Y']

for item in n:
    if item in vow:
        print("invalid")
        break
else:
    if (int(n[0])+int(n[1]))%2==0 and (int(n[3])+int(n[4]))%2==0 and (int(n[4])+int(n[5]))%2==0 and (int(n[7])+int(n[8]))%2==0:
        print("valid")
    else:
        print("invalid")