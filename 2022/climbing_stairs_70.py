import sys
sys.setrecursionlimit(5000)
def climbStairs( n: int) -> int:
    def factorial(num):
        if num == 1:
            return num
        else:
            return num * factorial(num - 1)

    count = 0

    count += 1
    if n == 1:
        return count
    total = n
    combination = 0
    total = total - 1
    combination = combination + 1
    while total >= combination:
        count += factorial(total) / (factorial(total - combination) * factorial(combination))
        total = total - 1
        combination = combination + 1
    return int(count)

print(climbStairs(10))