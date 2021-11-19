print("Kalkulator Sederhana Python\n")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Sisa Bagi")
print("6. Kuadrat")


pil = int(input("\nMasukan Pilihan Operasi : "))

x= int(input("Bilangan Angka : "))
y= int(input("Bilangan Angka : "))

if pil == 1:
   hasil = x+y
elif pil == 2:
   hasil = x-y
elif pil == 3:
   hasil = x*y
elif pil == 4:
   hasil = x/y
elif pil == 5:
    hasil = x%y
elif pil == 6:
    hasil = pow(x,y)

print("\nHasil : %d" %hasil)
