indonesia = int(input('nilai bahasa indonesia :'))
mtk = int(input('nilai matematika :'))
ipa = int(input('nilai ipa :'))

print('==========================')

if(indonesia < 0 or indonesia > 100):
    print('maaf input ada yang tidak valid')
elif(ipa < 0 or ipa > 100):
    print('maaf input ada yang tidak valid')
elif(mtk < 0 or mtk > 100):
    print('maaf input ada yang tidak valid')

elif(indonesia > 60 and ipa > 60 and mtk > 70):
    print('stautus kelulusan : lulus')
else:
    print('status kelulusan : tidak lulus')
    print('sebab :')

    if(indonesia < 60):
        print('nilai bahasa indonesia kurang dari 60')
    if(mtk < 70):
        print('nilai matematika kurang dari 70 ')
