#reverse a string
def reverse_number(num):
    num_str=str(num)

    reversed_str=num_str[::-1]

    reversed_int=int(reversed_str)

    return(reversed_int)


number=int(input("Enter a number"))
reversed_number=reverse_number(number)
print(reversed_number)