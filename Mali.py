nama = "Mali"
umur = int(input("Input umur kamu:"))

if umur < 19:
    print("Maaf ",nama,"belum boleh daftar vaksin")
elif umur >= 19:
    print("Selamat",nama,"kamu sudah terdaftar vaksin")
else:
    print("Ada yang salah")
