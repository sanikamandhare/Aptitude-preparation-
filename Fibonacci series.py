#Fibonacci series

def Fibonacci(n):
     fib_series=[0,1]
     for i in range(2,n):
        fib_series.append(fib_series[-1]+fib_series[-2])
     return fib_series


n=int(input("Enter the nth term: "))
print(Fibonacci(n))
