indonesia = int(input('nilai bahasa indonesia :'))
if(indonesia >= 0 and indonesia <= 100):

    matematika = int(input('nilai matematika:'))
if(matematika >= 0 and matematika <= 100):

    ipa = int(input('nilai ipa:'))
if(ipa >= 0 and ipa <= 100):

    print('==========================')

if (indonesia>60 and ipa>60 and matematika>70):
    print ('lulus')
else:
    print ('tidak lulus')
