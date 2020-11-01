indonesia = int(input('nilai bahasa indonesia :'))
matematika = int(input('nilai matematika :'))
ipa = int(input('nilai ipa :'))

print('============================')

if(indonesia < 0 or indonesia > 100):
    print('maaf input anda yang tidak valid')
elif(matematika < 0 or matematika > 100):
    print('maaf input anda yang tidak valid')
elif(ipa < 0 or ipa > 100):
    print('maaf input anda yang tidak valid')

elif(indonesia > 60 and matematika >70 and ipa > 60):
    print ('stats kelulusan : lulus')
else:
    print ('status kelulusan : tidak lulus')
