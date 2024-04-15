def multi_num(num):
    total=1
    for x in num:
        total *=x
    return total
print(multi_num((8,2,3,-1,7)))