#GCD

def gcd(a,b):
    if b==0:
        return a

    return gcd(b,a%b)



num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
result=gcd(num1,num2)
print("The greatest gcd of {} and {} is {}".format (num1 , num2 , result))
