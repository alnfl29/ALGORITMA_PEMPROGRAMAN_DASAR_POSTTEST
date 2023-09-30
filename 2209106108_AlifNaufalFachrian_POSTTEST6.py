import os, time
os.system('cls')

print(" <== Selamat Datang di POSTTEST 6 ==> ")

list_username=["alif","naufal"]
list_password=["123","456"]
list_role    =["admin","user"]

list_kacamata =["-1", '-2', '-3']
list_jumlah = ['10', '20', '30']
list_harga = ['1500000', "3000000", '4500000']

def garis():
    print (" <===========================> ")
cek_userpass = False

def tampilan_admin():
    garis()
    print("1. Tambah Kacamata")
    print("2. Tampilkan List Kacamata")
    print("3. Update Data Kacamata")
    print("4. Hapus Kacamata")
    print("5. Log Out")
    garis()

def tampilan_user():
    garis()
    print("1. Tampilkan List Kacamata")
    print("2. Log Out")
    garis()

while(cek_userpass == False):
    os.system("cls")
    garis()
    input_username = str(input(" masukkan username "))
    input_password = str(input(" masukkan password "))
    garis()

    if(input_username) in list_username :
        cek_userpass = True
        if(list_username.index(input_username)==list_password.index(input_password)):
            garis()
            print("  login berhasil  ")
            garis()
            os.system("cls")

            get_index = list_username.index(input_username)
            if(list_role[get_index] == "admin"):
                tampilan_admin()
                pilihan_admin = str(input("Masukkan Pilihan : "))
                if(pilihan_admin == "1"):
                    os.system('cls')
                    garis()
                    new_kacamata = str(input("Masukkan Ukuran : "))
                    new_jumlah = str(input("Masukkan Jumlah : "))
                    new_harga = str(input("Masukkan Harga : "))
                    garis()
                    if(new_jumlah.isnumeric() and new_harga.isnumeric()):
                        list_kacamata.append(new_kacamata)
                        list_jumlah.append(new_jumlah)
                        list_harga.append(new_harga)
                    time.sleep(3)
                    cek_userpass = False
                elif(pilihan_admin == '2'):
                    os.system('cls')
                    garis()
                    print("No.\tUkuran\tJumlah\tHarga")
                    for i in range(len(list_kacamata)):
                        print(str(i+1)+'. ' + "\t" + list_kacamata[i] + "\t" + list_jumlah[i] + "\t" + list_harga[i])
                    time.sleep(3)
                    cek_userpass = False 
                elif(pilihan_admin == '3'):
                    os.system('cls')
                    garis()
                    print("No.\tUkuran\tJumlah\tHarga")
                    for i in range(len(list_kacamata)):
                        print(str(i+1)+'. ' + "\t" + list_kacamata[i] + "\t" + list_jumlah[i] + "\t" + list_harga[i])
                    garis()
                    pilihan_ubah = str(input("Masukkan Pilihan : "))
                    if(pilihan_ubah.isnumeric()):
                        index_update = int(pilihan_ubah) - 1
                        
                        new_kacamata = str(input("Masukkan Ukuran : "))
                        new_jumlah = str(input("Masukkan Jumlah : "))
                        new_harga = str(input("Masukkan Harga : "))
                        garis()
                        if(new_jumlah.isnumeric() and new_harga.isnumeric()):
                            list_kacamata.pop(index_update)
                            list_jumlah.pop(index_update)
                            list_harga.pop(index_update)

                            list_kacamata.insert(index_update, new_kacamata)
                            list_jumlah.insert(index_update, new_jumlah)
                            list_harga.insert(index_update, new_harga)
                    cek_userpass = False
                elif(pilihan_admin == '4'):
                    os.system('cls')
                    garis()
                    print("No.\tUkuran\tJumlah\tHarga")
                    for i in range(len(list_kacamata)):
                        print(str(i+1)+'. ' + "\t" + list_kacamata[i] + "\t" + list_jumlah[i] + "\t" + list_harga[i])
                    garis()
                    pilihan_ubah = str(input("Masukkan Pilihan : "))
                    if(pilihan_ubah.isnumeric()):
                        index_update = int(pilihan_ubah) - 1
                    
                        list_kacamata.pop(index_update)
                        list_jumlah.pop(index_update)
                        list_harga.pop(index_update)
                    cek_userpass = False
                elif(pilihan_admin == '5'):
                    cek_userpass = False
                else:
                    garis()
                    print(" pilihan tidak tersedia ")
                    garis()
                    time.sleep(3)
                    cek_userpass = False
                    
            elif(list_role[get_index] == "user"):
                tampilan_user()
                pilihan_user = str(input("Masukkan Pilihan : ")) 
                if(pilihan_user  == '1'):
                    os.system('cls')
                    garis()
                    print("No.\tUkuran\tJumlah\tHarga")
                    for i in range(len(list_kacamata)):
                        print(str(i+1)+'. ' + "\t" + list_kacamata[i] + "\t" + list_jumlah[i] + "\t" + list_harga[i])
                    time.sleep(3)
                    cek_userpass = False
                elif(pilihan_user == '2'):
                    cek_userpass = False
                else:
                    garis()
                    print(" pilihan tidak tersedia ")
                    garis()
                    time.sleep(3)
                    cek_userpass = False

        else:
            print("   login gagal    ")
    else:
        print(" username tidak ada dalam data ")