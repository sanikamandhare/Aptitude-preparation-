#Write code Check if the given string is Palindrome or not.

def is_palindrome(user_input):
    reversed_s = user_input[::-1]
    if user_input == reversed_s:
        return True
    else:
        return False

user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")
