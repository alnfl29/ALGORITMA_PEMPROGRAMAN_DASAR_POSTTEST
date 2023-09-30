import os 

bersihkan = lambda: os.system("cls")

# Input 
# Biodata 
# a) Nama ->  nama = String
# b) Umur  -> umur = Integer
# c) Alamat -> alamat = String
# d) NIM -> nim,nim_bool = Integer & Boolean
# e) Tempat Tanggal Lahir ( TTL ) -> ttl = String
# f) Berat Badan -> bb = float
os.system('cls')

# Output
# print(nama)
# print(umur)
# print(alamat)
# print(nim)
# print(tempat tanggal lahir)
# print(berat badan)
os.system('cls')

print("   Selamat Datang di POSTTEST 3 ")

def garis():
    print (" <==============================> ")
cek_userpass = False


garis()
nama = str(input("nama anda : "))
umur = int(input("umur anda : "))
asal = str(input("asal daerah anda : "))
fakultas = str(input("fakultas anda : "))
prodi = str(input("prodi anda : "))
alamat = str(input("alamat anda : "))
nim = int(input("nim anda : "))
nim_boolean = bool(input("3 digit terakhir nim anda : "))
ttl = str(input("tempat tanggal lahir : "))
bb = float(input("berat badan : "))
tb = float(input("tinggi badan :"))
os.system('cls')
garis()



print("nama anda :",nama)
print("umur anda :",umur)
print("asal daerah anda :", asal)
print("fakultas anda :",fakultas)
print("prodi anda: ", prodi)
print("alamat anda :",alamat)
print("nim :",nim)
print("nim boolean :",nim_boolean)
print("nim modulus :",nim % 2)
print("tempat tanggal lahir :",ttl)
print("berat badan :",bb)
print("tinggi badan :",tb)
garis()

