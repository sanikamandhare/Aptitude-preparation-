#repeated words

input_str = input("Enter a string: ").split()
N = int(input("Enter a count: "))
word = set()

for i in input_str:
    if input_str.count(i) >= N:
        word.add(i)

if len(word) == 0:
    print("NA")
else:
    print(" ".join(word))



