def pushStack(x) :
    stack.append(x)
def popStack() :
    return stack.pop()

stack = []

pushStack('Hello') 
pushStack('Matematika') 
pushStack('Komputer') 
pushStack ('Algoritma') 
pushStack ('Logika') 

for i in range(4) : 
    data = popStack () 
    if (len(data) >=10) : 
        pushStack (data)

print (stack)
