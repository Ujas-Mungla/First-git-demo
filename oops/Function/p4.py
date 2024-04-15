# fact=1
# n=6
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("Factorial is :",fact)
factorial(5)