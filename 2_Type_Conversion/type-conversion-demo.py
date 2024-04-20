'''
    Daire Alanı     : pi*r2
    Daire Çevresi   : 2*pi*r

    * Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (r:3.14)
'''
pi=3.14

r=float(input("yarı çap : "))

alan=pi*(r**2)
cevre=2*pi*r

print("alan : "+ str(alan))
print("cevre :" + str(cevre))