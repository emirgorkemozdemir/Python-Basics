# Listeler birden fazla deger tutmak için oluşturulan degişkenlerdir.
# Listeler diger programlama dillerindeki array (dizi) kavramında denk gelir.
my_list = ["Apple","Banana","Grape",15]

# Liste oluşturmanın alternatif yolu
# my_list_2 = list(("Apple","Banana","Grape"))

# Oluşturdugumuz listeler sıralıdır.
# Degiştirilebilirler.
# Tür odaklı degillerdir
# İçerikleri tek tek dolaşılabilir.
# Birden fazla aynı degeri içerebilir (duplicate)

# Ögeleri seçmek için index (sıra sayısı) kullanılır.
# Python'da indexler 0'dan başlar

# Listelerin uzunlugu len() ile alınır.
print(len(my_list))

# Bir degerin kaçıncı indexte bulundugunu görmek için index()
# fonksiyonu kullanılır.
my_list.index("Apple")

# Listelerin içerikleri degiştirilebilir.
# İçerigin degiştigi satırdan sonra o degişiklik geçerlidir.
my_list[0] = "Chery"

