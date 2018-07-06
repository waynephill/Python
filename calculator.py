print ("Menu")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - Square")
print("6 - Power")

menu_option = int(input("Please select a calculation to perform: "))

val1 = int(input("Enter first number: "))
val2 = int(input("Enter first number: "))

if menu_option == 1:
    print(val1 + val2)
elif menu_option == 2:
    print(val1 - val2)
elif menu_option == 3:
    print(val1 * val2)
elif menu_option == 4:
    print(val1 / val2)
elif menu_option == 5:
    print(val1 * val1)
elif menu_option == 6:
    print(val1 ** val2)
else:
    print("Invalid choice")
    

