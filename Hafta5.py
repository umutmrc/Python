#############################
# 1 den 10 a kadar yazdırır.
#
#a = 1
#while a<11:
#    print(a)
#    a+=1
#
#############################
#
##Aksi belirtilmediği sürece kullanıcıya
##Aşağıdaki soruyu sormaya devam et!
#
#while True:
#    soru = input("Nasılsınız, iyi misiniz?")
##Eğer kullanıccı 'q' tuşuna basarsa...
#    if soru == "q":
#        break #döngüyü kır ve programdan çık.
#
#############################
#
#tekrar=1
#while tekrar<=3:
#    print("tekrar: ", tekrar)
#    tekrar +=1
#    input("Nasılsınız, iyi misiniz?")
#    print("bool değeri: ",bool(tekrar<=3))
#
#############################
# 0 dan 100 e kadar çift sayıları bas
#
#a=0
#while a<=100:
#    if(a%2)==0:
#        print(a)
#    a+=1
#
#############################
# Alt alta medipol ve myo yaz
#
#harfler = "medipol"
#for harf in harfler:
#    print(harf)
#for h in "myo":
#    print(h)
#
#############################
#for kullanarak 1 den 5 e kadar olan sayıların karesi
#
#sayilar=1,2,3,4,5
#for sayi in sayilar:
#    print(sayi*sayi)
#
#############################
#kullanıcıdan parola alın türkçe karakter olmasın
#
#parola=input("Bir Parola Girin")
#for harf in parola:
#    if harf in "şçğıİüö":
#        print("Türkçe Karakter Var")
#        break
#    else:
#        print("Türkçe Karakter Yok")
#        break
#
#############################
#
# 0 dan 4 e kadar yazdırır.
#for i in range(0,5):
#    print(i)
#print("-"*10)
#
#############################
# 0 dan 9 a kadar yazdırır.
#
#for i in  range(10):
#    print(i)
#print("-"*10)
#
#############################
# 0 dan 8 e kadar yazdırır.
#
#for i in range(0,10,2):
#    print(i)
#print("-"*10)
#
#############################
# 10 dan 1 e kadar yazdırır.
#
#for i in range(10,0,-1):
#    print(i)
#
#############################
#
#for i in range(3):
#    parola=input("Parola Belirleyin: ")
#    if i==2:
#        print("Parolayı 3 kez yanlış girdiniz.","Lütfen 30 dakika sonra tekrar deneyin")
#    elif not parola:
#        print("Boş Geçilemez! ")
#    elif len(parola) in range(3,8):
#        print("Yeni Parolanız ",parola)
#    else:
#        print("Parola 8 Karakterden Uzun 3 Karakterden Kısa Olmamalı")
#
#############################
#
#while True:
#    parola=input("Parola Belirleyin: ")
#    if not parola:
#        pass
#    elif len(parola) in range(3,8):
#        print("Yeni Parolanız: ",parola)
#        break
#    else:
#        print("Parola 8 karakterden uzun 3 karakterden kısa olmamalı")
#
#############################
#
#while True:
#    parola=input("Bir Sayı Girin: ")
#    if len(parola)<5:
#        print("Parola 5 karakterden az olmamalı")
#    else:
#        print("Parola Doğru Uzunluktadır")
#
#############################
#
#while True:
#    s=input("Bir Sayı Girin: ")
#    if s=="iptal":
#        break
#    if len(s)<=3:
#        continue
#        #pass
#    print("En fazla üç haneli bir sayı girebilirsiniz. ")
#
#############################
