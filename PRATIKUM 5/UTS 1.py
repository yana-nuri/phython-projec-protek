BeratBadan=int(input("berapa berat badan anda dalam kilogram ? "))
TinggiBadan=int(input("berapa tinggi anda dalam centimeter ? "))

def hitunganYANA(BeratBadan,TinggiBadan):
    global YANA
    TinggiBadan=TinggiBadan/100
    YANA=BeratBadan/(TinggiBadan*TinggiBadan)

hitunganYANA(BeratBadan, TinggiBadan)

if(YANA<18):
    status = 'KURUS'
    print("Badan Anda ", status)
elif(YANA >= 18 and YANA < 23):
    status= 'IDEAL'
    print("Badan Anda ", status)
elif(YANA >= 23 and YANA < 27):
    status = 'GEMUK'
    print("Badan Anda ", status)
elif(YANA >= 27 and YANA < 35):
    status = 'OBESITAS'
    print("Badan Anda ", status)
elif(YANA >= 35):
    status = 'OBISITAS MORBID'
    print("Badan Anda ", status)
