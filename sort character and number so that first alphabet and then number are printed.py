#sort character and number so that first alphabet and then number are printed . input-(A7B1R3) 
#output-ABR137

str="A7B1R3"
Alphabets=[]
numbers=[]

for ch in str:
    if ch.isalpha():
        Alphabets.append(ch)
    else:
        numbers.append(ch)

MyList=sorted(Alphabets)+sorted(numbers)
output="".join(MyList)
