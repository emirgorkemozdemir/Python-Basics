# Kullanıcı tarafından girilen deger listede var mı diye kontrol edin.
# Varsa true yoksa false yazdırın.

my_list = ["Apple","Banana","Grape"]

selected_fruit = input("Bir meyve giriniz : ")

if (selected_fruit in my_list):
    print(True)
else:
    print(False)

# in kelimesini kullanarak bir deger listenin içinde mi sorusunun
# cevabını alabiliyorsunuz.

"""
age_list = [11,12,25,26]

age = int(input("Yaşınızı giriniz : "))
if(age in age_list):
    print(True)
else:
    print(False)
"""
