# Kullanıcı tarafından girilen degere göre elimizdeki sayıyla kıyaslama
# yapalım

num1 = 5
num2 = int(input("Bir sayı giriniz :"))

if(num2>num1):
    print("Girilen sayı daha büyük")
elif(num1==num2):
    print("Sayılar eşit")
else:
    print("Girilen sayı daha küçük")