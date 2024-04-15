def reverse_string(str1):
    st=''
    index=len(str1)
    while index >0:
        st+=str1[index-1]
        index=index-1
    return st
print(reverse_string('1234abcd'))