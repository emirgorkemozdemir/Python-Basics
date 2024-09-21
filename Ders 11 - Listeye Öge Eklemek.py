my_list = ["Apple","Banana","Grape"]

# Listelere öge eklemenin iki yolu var

# Birincisi Append() => Append ögeyi en sona ekler
my_list.append("Pear")

# İkincisi Insert() => Insert belirledigimiz indexe ekleme yapar
# o eklenen index silinmez. Hepsini saga veya sola kaydırır.
my_list.insert(0,"Test")

print(my_list)