print("-------------------YANA NURIKA-----------------")
print("---------------------K3520079------------------")

file = open("file.txt" , "r")

data = file.readlines()
dataMHS = {}
for i in range(len(data)) :
     Mhs = data[i]
     a,b,c = Mhs.split('|')
     a,b,c= a,b,c.replace('\n', '')
     dataMahasiswa = {'nim' : a, 'nama' : b, 'alamat' : c}
     dataMHS[a] = dataMahasiswa

print(dataMHS)
file.close
