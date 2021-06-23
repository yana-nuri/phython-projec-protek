data = [70, 78, 62, 23, 83]

n = len(data)
swapped = True

while swapped == True :
    swapped = False
    for i in range (n-1) :
        if data[i] > data[i+1] :
            data[i], data[i+1] = data[i+1], data[i]
            print(data)
            swapped = True

print (data)
 
