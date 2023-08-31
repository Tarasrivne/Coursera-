def factorial_looping(n):
    if n<0:
        return 0
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial = factorial * i
        return factorial

print(factorial_looping(100))