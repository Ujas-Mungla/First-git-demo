str1="P@#yn26at^&i5ve"
Chars=0
Digits=0
Symbol=0
for i in str1:
    if i.isalpha():
        Chars+=1
    elif i.isdigit():
        Digits+=1
    else:
        Symbol+=1
print(f"Chars :",Chars,"\n","Digits :",Digits,"\n","Symbol :",Symbol)
