integer = int(input("Please enter a number: "))
factorial = 1
for i in range(integer,0,-1):
    factorial = factorial * i
    print("factorial of",integer,"",factorial)
