n = int(input("Masukkan bilangan: "))
if n > 0:
    jenis = "positif"
elif n < 0:
    jenis = "negatif"
else:
    jenis = "nol"

if n % 2 == 0:
    sifat = "genap"
else:
    sifat = "ganjil"
print("Bilangan", jenis, "dan", sifat)