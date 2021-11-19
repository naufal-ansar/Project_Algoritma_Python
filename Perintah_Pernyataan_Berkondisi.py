nama = input("Nama:")
kelas = input("Kelas:")
matkul = input("Mata Kuliah:")
nilai = int(input("Berapa Nilai Mata Kuliah:"))

if(nilai >= 80):
    grade = "A"
elif(nilai >= 60):
    grade = "B"
elif(nilai >= 40):
    grade = "C"
elif(nilai < 40):
    grade = "D"

print("Memperoleh Grade:",grade)
print('Nilai Mata Kuliah',matkul,'atas nama',nama,'dinyatakan')

if(nilai >= 60):
    print("LULUS")
elif(nilai >= 40):
    print("REMIDI")
elif(nilai > 40):
    print("TIDAK LULUS")
