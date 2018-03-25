##############################################################################
#
#    a=int(input("Bir Sayı Girin : "))
#    if a>10:
#        print("10 dan büyüktür.")
#    if a<10:
#        print("10 dan küçüktür")
#    if a==10 :
#        print("Girdiğiniz sayı 10 dur")
#
##############################################################################
#
#    yas= int(input("Yaşınız : "))
#    if yas==18:
#        print("18 iyidir!")
#    elif yas<18:
#        print("Genç bir kardeşimizsin!")
#    elif yas>18:
#        print("Eh, artık yaş yavaş yavaş kemale eriyor!")
#
##############################################################################
#
#    ad=input("kullanıcı adı : ")
#    if bool(ad)==True:
#        print("hoşgeldin")
#    else:
#        print("boş geçme")
#
##############################################################################
#
#    a=int(input("Bir Sayı Girin : "))
#    if (a%2)==0:
#        print("Girdiğiniz Sayı Çift")
#    else:
#        print("Girdiğiniz Sayı Tek")
#
##############################################################################
#
#    kullanıcı_adı=input("Kullanıcı adınız : ")
#    parola=input("Parolanız : ")
#    if kullanıcı_adı == "umut" :
#        if parola == "123456" :
#            print("Programa hoşgeldiniz. ")
#        else:
#            print("Yanlış kullanıcı adı veya parola! ")
#    else:
#        print("Yanlış kullanıcı adı veya parola! ")
#
##############################################################################
#
#    x=int(input("Notunuz : "))
#    if x>100 or x<0:
#        print("Böyle Bir Not Yok. ")
#    elif x>=90 and x<=100:
#        print("A Aldınız. ")
#    elif x>=80 and x<=89:
#        print("B Aldınız. ")
#    elif x>=70 and x<=79:
#        print("C Aldınız. ")
#    elif x>=50 and x<=69:
#        print("D Aldınız. ")
#    else:
#        print("F Aldınız. ")
#
##############################################################################
#
a=int(input("Bir Sayı Giriniz: "))
if(a>1000 and a<9999):

    birler=a%10
    onlar=(a%100)//10
    yuzler = (a % 1000) // 100
    binler = (a % 10000) // 1000

    print(birler,onlar,yuzler,binler)
else:
    print("Yanlış Sayı Girdiniz ")
#
##############################################################################
