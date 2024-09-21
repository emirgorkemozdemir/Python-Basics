# Degişkenler adları üzerinde uygulama esnasında çalışan ve 
# uygulamanın tamamında veya bir kısmında tutulması gereken
# degerleri tutan boş kutular gibidir.

# Veri Türleri
# Number : integer, float
# String : yazılar metinler
# Bool : True False

# Önceden bir türde belirlenen bir degişken daha sonrasında
# başka türde olabilir

# Ctrl + k + c ile seçtiginiz satırı yorum yapabilirsiniz.
# Ctrl + k + u ile seçtiginiz satırın yorumunu kaldırabilirsiniz.

test = 5
# test ="Deneme"
# print(test)

# Bir degişkenin türünü type() ile bulabilirsiniz.
print(type(test))

# Multi degişken oluşturma
x = y = z = 5

# Type Casting
test2 = str(test) # sonuç "5" olacaktır
test3 = float(test) # sonuç 5.0 olacaktır

# Python Case Sensitive'dir. Yani büyük küçük harfe duyarlıdır
deneme = 5
Deneme = 5

# Degişken ismi verilirken konuyla ve olayla baglantılı ve mantıklı 
# degişken isimleri kullanmak en dogrusu olacaktır.