T = int(input())

for _ in range(T):
    cost_green, cost_blue = map(int, input().split())
    n = int(input())

    problem1_solved = 0
    problem2_solved = 0

    for _ in range(n):
        problem1, problem2 = map(int, input().split())
        if problem1 == 1:
            problem1_solved += 1
        if problem2 == 1:
            problem2_solved += 1

    cost1 = (problem1_solved*cost_green)+(problem2_solved*cost_blue)
    cost2 = (problem1_solved*cost_blue)+(problem2_solved*cost_green)

    print(min(cost1,cost2))