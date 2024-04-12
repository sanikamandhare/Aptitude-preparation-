#Write code to Calculate frequency of characters in a string

def calculate_frequency(input_string):
    frequency={}

    for char in input_string:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1

    return frequency


input_string=input("enter a string: ")
result = calculate_frequency(input_string)
print("the calculated frequencies are : ",result)

