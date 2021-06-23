X = []
Y = []

def push(a, n) :
    n.append (a)

def pushInteger(a, X, Y) :
    if a >=1 and a<= 20 :
        if a % 2 != 0 :
            push (a, X)
        else :
            push (a, Y)

Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in range(len(Z)) :
    pushInteger(Z[i], X, Y)

print (X)
print (Y)
