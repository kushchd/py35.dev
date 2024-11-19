#
str1 ="khokho"
length = len(str1)

if str1[:length//2] == str1[length//2:]:
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")
