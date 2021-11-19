bioskop = input("Nama Bioskop:")
tiket = int(input("Harga Tiket:"))
pengunjung = int(input("Masukan pengunjung:"))
print("-------------------------------------")
if(tiket >= 50000):
    print("Tiket VIP")
else:
    print("Tiket Reguler")

total_bayar = pengunjung * tiket
print("Total yang harus dibayar adalah",total_bayar)
print("-------------------------------------")
bioskop = input("Nama Bioskop:")
tiket = int(input("Harga Tiket:"))
pengunjung = int(input("Masukan pengunjung:"))
print("-------------------------------------")
if(tiket == 50000) & (pengunjung == 1):
    print("Tiket VIP")
else:
    print("Tiket Reguler")

total_bayar = pengunjung * tiket
print("Total yang harus dibayar adalah",total_bayar)
print("-------------------------------------")
