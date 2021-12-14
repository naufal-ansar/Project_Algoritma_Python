nama = input("Nama Mhs:")
nim = input("Nim Mhs:")
prodi = input("Prodi:")
kelas = input("Kelas:")
semester = input("Semester:")

if(prodi == "informatika"):
    semester = 1
    if(kelas == "A"):
        matkul = "algoritma pemrograman"
    elif(kelas == "B"):
        matkul = "algoritma struktur data"
    elif(kelas == "C"):
        matkul = "sitem digital"
elif(prodi != "informatika"):
    semester = 1
    if(kelas == "A"):
        matkul = "pendidikan agama islam"
    elif(kelas == "B"):
        matkul = "pancasila"
    elif(kelas == "C"):
        matkul = "seni budaya"
    else:
        print("Salah")

print("Semester:",semester)
print("Matkul:",matkul)
