def pushQueue(x) :
    Queue.append(x)
def popQueue() :
    return Queue.pop()

Queue = []

pushQueue('Hello') 
pushQueue('Matematika') 
pushQueue('Komputer') 
pushQueue('Algoritma') 
pushQueue('Logika') 

for i in range(4) : 
    data = popQueue () 
    if (len(data) >=8) : 
        pushQueue (data)

print (Queue)
