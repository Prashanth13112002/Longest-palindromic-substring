def Longest_Palindromic_Substring(string):
    while True:
        if string==string[::-1]:
            return string
        else:
            string=string[1:]

x=input()
print(Longest_Palindromic_Substring(x))
