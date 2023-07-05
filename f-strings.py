a , b = 5 , 10
print(f"{a} ile {b}'u çarparsak {a * b}'yi elde ederiz.")

name , surname , age = input("adınız: "), input("soyadınz: "), input("yaşınız: ")
print(f"Merhaba {name} {surname} bey/bayan. Nasılsınız? {age} yaşında olmak nasıl bir duygu? ")

# değişkenin başına " * " koyarsak diğer her değişkene 1 karakter atanırken *'lı değişkene diğerlerinden kalan bütün karakterler atanır.
fiyat = "€1456,789#"
ilk, *orta, son = fiyat
print(ilk)
print(*orta, sep="")
print(son)