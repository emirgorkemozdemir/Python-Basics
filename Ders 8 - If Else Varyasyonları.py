# If ile veya elif ile tek durum yazmak zorunda degilim. Birden fazla
# durumu karışık olarak and ve or kullanarak yapabilirim.

a=5
b=7
c=10

if (a>b) or (b>c):
    print("Sonuç")

# not ekleyerek o durumun dogru olmamasını da kontrol edebiliyorsunuz
if not (a>b):
    pass 
    # pass yazarsanız hata almadan if elif else durumlarını boş bırakabilirsiniz