#Determining the bigger number
print ("Which number is bigger:")
number1 = float(input("Please enter first number: "))
number2 = float(input("Please enter second number: "))

if number1 > number2:
    number1bigger = True
else:
    number1bigger = False

print("number1 bigger: ", number1bigger)

if number1bigger:
    print("number1 bigger")
else:
    print("number1 not bigger")
    


