my_list = ["Apple","Banana","Grape"]

# Listelerden öge silmenin 2 yolu mevcut.

# Birincisi Remove() => Belirttigim ögeyi siler.
# Aynı ögeden birden fazla varsa ilk buldugunu siler.
my_list.remove("Apple")

# İkincisi Pop() => Indexe göre siler.
# Boş bırakılırsa sonuncu indexi siler.
my_list.pop(0)
print(my_list)
