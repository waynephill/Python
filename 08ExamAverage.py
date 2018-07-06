def average(number1,number2,number3):
    average = (number1 + number2 + number3)/3.0
    return average

maths_mark = int(input("Please input mark (0 to 100) for Maths: "))
english_mark = int(input("Please input mark (0 to 100) for English: "))
ICT_mark = int(input("Please input mark (0 to 100) for ICT: "))

if(maths_mark < 0 or maths_mark > 100
   or english_mark < 0 or english_mark > 100
   or ICT_mark < 0 or ICT_mark > 100):
        print("invalid mark")
else:
        average_mark = average(maths_mark,english_mark,ICT_mark)
        if average_mark >= 65:
            print(average_mark,"Pass")
        else:
            print(average_mark,"Fail")
