def fence():
    n = int(input())
    grid = list(input())

    for i in range(1, n):
        if grid[i]=='H' and grid[i-1]=='H':
            print("NO")
    
    for i in range(n):
        if grid[i] == '.':
            grid[i] =  'B'

    print("YES")
    print("".join(grid))

fence()