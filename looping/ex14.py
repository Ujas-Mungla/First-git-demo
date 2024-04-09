
num=76542
rev_num=0
print("Given Numbar :",num)
while num >0:
    rem=num%10
    print(rem)
    rev_num = (rev_num * 10) + rem
    num = num // 10
print("Reverese Number:  ", rev_num)
# list1=[10,20,30]
# list2=[10,20,30]
# reversed(list1)
# list2.reverse()
# print(list1)
# print(list2)