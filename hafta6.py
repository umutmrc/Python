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
################################################
################################################
################################################
################################################
################################################








##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
#
#dizi="Medipol2018"
#print(dizi[3])
#
##########################################################
#
#print("-"*10)
#
##########################################################
#
#nesne = "123456789"
#print(int(nesne[1])*2)
#
##########################################################
#
#print("-"*10)
#
##########################################################
#
#nesne = "123456789"
#sayi = int(nesne[1])
#print(sayi*2)
#
##########################################################
#
#print("-"*10)
#
##########################################################
#
#print(len(dizi))
#print(dizi[len(dizi)-1])
#
##########################################################
#
#print("-"*10)
#
##########################################################
#
##print(dizi[len(dizi)])
#
##########################################################
#
#try:
#    print(dizi[len(dizi)])
#except IndexError as hata:
#    print("Orijinal Hata Mesajı: ", hata)
#
##########################################################
#
#print("-"*10)
#
##########################################################
#
#print(dizi[-1])
#print(dizi[-2])
#
##########################################################
#
#print("-"*10)
#
##########################################################
#
#for i in range(7):
#    print(dizi[i])
#
##########################################################
#
#print("-"*10)
#
##########################################################
#
#for i in range(len(dizi)):
#    print(dizi[i])
#
#print("-"*10)
#
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
#
#site = "www.medipol.com"
#print(site[4:11])
#
##########################################################
#
#site1 = "www.google.com"
#site2 = "www.medipol.com"
#site3 = "www.yaho.com"
#site4 = "www.iett.org"
#for isim in site1, site2, site3, site4:
#    print("site: ", isim[4:-4])
#
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
#
#dizi1 = "aaaaaaaaaaaaaaaaaaaaaaa!"
#dizi2 = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbb!"
#dizi3 = "cccccccccccccccccccccccccccccccccc!"
#dizi4 = "dddddddddddd!"
#dizi5 = "eeeeeeeeeeeeeeeeeeeeeeeeeeeee!"
#print("-"*10)
#for dizi in dizi1,dizi2,dizi3,dizi4,dizi5:
#    print(dizi[0:-1])
#print("-"*10)
#
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
#
#kardiz= "Sana Gül Bahçesi Vadetmedim"
#print(kardiz[0:-4])
#print(kardiz[:-4])
#print(kardiz[17:27])
#print(kardiz[17:])
#
##########################################################
#
#print("-"*10)
#
##########################################################
#
#kardiz = "istanbul"
#print(kardiz[0:8:1])
#print(kardiz[0:8:2])
#print(kardiz[::2])
#print(kardiz[::-1])
#print(kardiz[::-2])
#for i in reversed("Sana Gül Bahçesi Vadetmedim"):
#    print(i,end="")
#
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
#
#print(sorted("ketap"))
#
##########################################################
#
#print("-"*10)
#
##########################################################
#
#for i in sorted("kitap"):
#    print(i, end="")
#
##########################################################
#
#print("-"*10)
#
##########################################################
#
#for i in sorted("çiçek"):
#    print(i, end="")
#
##########################################################












##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
#
#site1 = "www.google.com"
#site2 = "www.medipol.com"
#site3 = "www.yahoo.com"
#site4 = "www.iett.org"
#
#for i in site1, site2, site3, site4:
#    print("http://", i, sep="")
#
#print("\n","-"*10,sep="")
#
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
#
#kardiz = "medipoleee"
#print(kardiz.replace("e","E"))
#print(kardiz.replace("pol","POL"))
#print(kardiz.replace("e","E"))
#print(kardiz.replace("e","E",1))
#print(kardiz.replace("e","E",2))
#
##########################################################
#
#print(kardiz)
#
##########################################################
#
#kardiz = "İstanbul Büyükşehir Belediyesi"
#print(kardiz[0], kardiz[9], kardiz[20], sep="")
#
#for i in kardiz.split():
#    print(i)

#print(kardiz.split())
#print(kardiz.split(" ", 1))

#for i in kardiz.split(" ", 1):
#    print(i)

#for i in kardiz.split():
#    print(i[0], end="")

#print("\n \n")

#kardiz = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"

#for i in kardiz.split():
#    print(i)
#for i in kardiz.split(", "):
#    print(i)
#for i in kardiz.split("1"):
#    print(i)
#
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################









###########################################################
#
#kardiz="İstanbul Büyükşehir Belediyesi"
#for i in kardiz.split():
#    print(i[0],i[1],sep="-",end="")
#
###########################################################
#
#print("Can","Savut",sep="?",end=".")
#print("Yusuf","Özer",sep="-",end=",")
#
###########################################################
#
#dizi="ARMUT"
#print(dizi.lower())
#
#dizi="armut"
#print(dizi.upper())
#
#dizi="Ankara"
#print(dizi.islower())
#print(dizi.isupper())
#print(dizi.startswith("a"))
#print(dizi.endswith("a"))
#
###########################################################
#
#dizi="Medipol"
#print(dizi.replace("i",""))
#print(dizi.replace("l","L"))
#
###########################################################
#
