def is_armstrong(num):
    temp = num
    sum = 0
    
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    
    if sum == num:
        return True
    else:
        return False

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")
