# Write code to Check if two strings are Anagram or not
#listen and silent
def are_anagram(str1,str2):
    if len(str1)!=len(str2):
        return False

    str1=str1.lower()
    str2=str2.lower()

    str1=sorted(str1)
    str2=sorted(str2)

    if str1==str2:
        return True
    else:
        return False

str1=input()
str2=input()
if are_anagram(str1,str2):
    print(str1,str2 , "are anagram")
else:
    print(str1,str2,"are not anagrams")