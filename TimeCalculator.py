##from datetime import datetime
##date_entry = input('Enter a date in YYYY-MM-DD format')
##year, month, day = map(int, date_entry.split('-'))
##date1 = datetime.date(year, month, day)


import datetime
def ObtainDate():
##    isValid=False
##    while not isValid:
        userIn = input("Type Date dd/mm/yy: ")
##        try: # strptime throws an exception if the input doesn't match the pattern
##            d = datetime.datetime.strptime(userIn, "%d/%m/%y")
##            isValid=True
##        except:
            print ("Doh, try again!\n")
##    return d
#test the function
print (ObtainDate())
