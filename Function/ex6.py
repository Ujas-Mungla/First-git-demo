def recursion(n):
    if n==0:
        return 0
    else:
         return n + recursion(n-1)
result=recursion(10)
print(result)

