# s1="Yn"
# s2="PYnative"
# if "Yn" in s2:
#     print("True")

# d1="Ynf"
# d2="Pynative"
# if "Ynf" not in d2:
#     print("False")
def check_substring(substring, string):
    if substring in string:
        print("True")
    else:
        print("False")
s1 = "Yn"
s2 = "PYnative"
check_substring(s1, s2)

d1 = "Ynf"
d2 = "Pynative"
check_substring(d1, d2)
