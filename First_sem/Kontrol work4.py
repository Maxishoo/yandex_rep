
def rabbit(start, finish, length):
    return f + f + f + f


result = rabbit(7, 10, 3)
print(*result, sep='\n')


def multi_sum(*numbers, div=2):
    dp = [0]* len(numbers)
    numbers = [0] + list(numbers)
    for i in range(1,len(numbers)+1):
        dp[i] = max(dp[i-1], )