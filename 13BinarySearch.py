import random
def bubbleSort(list):
    for numcheck in range(len(list)-1,0,-1):
        for i in range(numcheck):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                
randList = random.sample(range(1, 100),6)
print ("Unsorted list: ",randList)
bubbleSort(randList)
print ("Sorted list: ",randList)



