print("-------------------YANA NURIKA-----------------")
print("---------------------K3520079------------------")

file = open('IsiFileAngka.txt', 'r')
IsiFileAngka = file.readlines()

angkaGenap = []
angkaGanjil = []
for i in range(len(IsiFileAngka)):
    if ('\n' in IsiFileAngka[i] == True):
        IsiFileAngka[i].replace('\n', '')

        if (int(IsiFileAngka[i])%2 == 0):
            angkaGenap.append(IsiFileAngka[i])
        else :
            angkaGanjil.append(IsiFileAngka[i])
    else :
        if (int(IsiFileAngka[i])%2 == 0) :
            angkaGenap.append(IsiFileAngka[i])
        else :
            angkaGanjil.append(IsiFileAngka[i])

print ("Banyaknya bilangan Genap : {0}".format(len(angkaGenap)))
print ("Banyaknya bilangan Genap : {0}".format(len(angkaGanjil)))            
        
            

        
