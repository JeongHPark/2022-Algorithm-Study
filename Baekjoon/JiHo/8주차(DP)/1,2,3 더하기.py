def dp_sum(n) :
    if n < 0 : return 0
    elif n == 0 : return 1
    return dp_sum(n - 1) + dp_sum(n - 2) + dp_sum(n-3)

n = int(input())

for i in range(n) :
    print(dp_sum(int(input())))