def average(*n):
    i=0
    j=0
    for x in n:
        i=i+x
        j+=1

    average=i/j
    print(average)

def max(*n):
    max=n[0]
    for i in (n):
        if(i>max):
            max=i
        print(max)

def min(*n):
    min=n[0]
    for i in (n):
        if(i<min):
            min=i
    print(min)
#5a
average(5,10,4,9,30,16,2,11)
max(5,10,4,9,30,16,2,11)
min(5,10,4,9,30,16,2,11)
#5b
average(81,98,12,83,45,77,69,30,56)
max(81,98,12,83,45,77,69,30,56)
min(81,98,12,83,45,77,69,30,56)
