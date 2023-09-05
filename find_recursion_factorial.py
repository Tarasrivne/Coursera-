def find_recursion(n):
    if n == 1:
        return 1
    else:
        return n * find_recursion(n-1)

print(find_recursion(5))