def outer(a,b):
    def inner(a,b):
        return a+b
    addi=inner(a,b)
    return addi + 5
result=outer(3,5)
print(result)
