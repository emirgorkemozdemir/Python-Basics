# Kullanıcıdan bir isim alınız, ismin ilk karakteri a ise 
# ekrana True yazdırın.

name = input("Bir isim giriniz : ")

if(name[0]=="a" or name[0]=="A"):
    print("True")
else:
    print("False")