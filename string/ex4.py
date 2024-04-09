str1="PyNaTive"
lower=[]
upper=[]
for i in str1:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
str2=" ".join(lower+upper)
print(str2)