################################################
#
#ilk_sayi = input("İlk Sayı: ")
#ikinci_sayi = input("İkinci Sayı: ")
#ilk_sayi=int(ilk_sayi)
#ikinci_sayi=int(ikinci_sayi)
#print(ilk_sayi, "/", ikinci_sayi, "=", ilk_sayi/ikinci_sayi)
#
################################################
#
#ilk_sayi = input("İlk Sayı: ")
#ikinci_sayi = input("İkinci Sayı: ")
#try:
#    sayi1 = int(ilk_sayi)
#    sayi2 = int(ikinci_sayi)
#    print(sayi1, "/", sayi2, "=", sayi1/sayi2)
#except ZeroDivisionError:
#    print("Bir Sayıyı 0'a Bölemezsiniz!")
##except ValueError:
##    print("Lütfen Sadece Sayı Girin!")
##except:
##    print("Beklenmeyen bir hata oluştu! ")
#
################################################
#
#           sayi=3
#              ***
#               **
#                *


#sayilar= int(input("Bir Sayı Girin"))
#a=1;
#for i in range(sayilar,0,-1):
#        print(" "*(i-1),"*"*a)
#        a+=1;
#
################################################
#
#           sayi=3
#           *
#           **
#           ***


#sayilar= int(input("Bir Sayı Girin"))
#for i in range(0,sayilar):
#        print("*"*(i+1))
#
################################################








##########################################################
dizi="Medipol2018"
print(dizi[3])
##########################################################
print("-"*10)
##########################################################
nesne = "123456789"
print(int(nesne[1])*2)
##########################################################
print("-"*10)
##########################################################
nesne = "123456789"
sayi = int(nesne[1])
print(sayi*2)
##########################################################
print("-"*10)
##########################################################
print(len(dizi))
print(dizi[len(dizi)-1])
##########################################################
print("-"*10)
##########################################################
#print(dizi[len(dizi)])
##########################################################
try:
    print(dizi[len(dizi)])
except IndexError as hata:
    print("Orijinal Hata Mesajı: ", hata)
##########################################################
print("-"*10)
##########################################################
print(dizi[-1])
print(dizi[-2])
##########################################################
print("-"*10)
##########################################################
for i in range(7):
    print(dizi[i])
##########################################################
print("-"*10)
##########################################################
for i in range(len(dizi)):
    print(dizi[i])
    
print("-"*10)
##########################################################
