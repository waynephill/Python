def volume(number1,number2,number3):
    if number1 < 0 or number2 < 0 or number3 < 0:
        print ("Invalid length")
    else:
        volume = number1 * number2 * number3
        print("Volume:",volume)

width = float(input("Please input width: "))
depth = float(input("Please input depth: "))
height = float(input("Please input height: "))

if width < 0 or depth < 0 or height < 0:
    print ("Invalid length")
else:
    print("Volume:",volume(width,depth,height))



