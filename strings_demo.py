website = "http://www.mustafakilicsokan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
lenght = len(course)
# 2- 'website' içinden www karakterlerini alın.
result = website[7:10]
# 3- 'website' içinden com karakterlerini alın.
result1 = website[-3:]
# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result2 = course[:15],course[-15:]
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
result3 = course[::-1]


name, surname, age, job = 'Bora','Yılmaz', 32, 'mühendis' 

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'

print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

s = "Hello world"
s = s[:6] + "W" + s[-4:]
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

a = "abc " * 3
print(a)