def is_perfect_number(num):
    sum_of_divisor = 0

    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum_of_divisor += i

    
    if sum_of_divisor == num:
        return True
    else:
        return False

number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")
