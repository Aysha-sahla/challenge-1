num = int(input("Enter any number: "))
n = num
power = len(str(num))
sum = 0

while n > 0:
    digit = n % 10       
    sum += digit**power
    n //= 10             

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")