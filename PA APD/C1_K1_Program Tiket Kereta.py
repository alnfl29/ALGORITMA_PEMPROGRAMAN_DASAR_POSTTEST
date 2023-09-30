import os
import sys



# TUPLE

# INPUT DATA 
gender1 = {1: ' Laki - Laki ',2: ' Perempuan '}
jam1 = {1: ' 07.00 - 11.00 ',2: ' 12.00 - 15.00 ',3: ' 16.00 - 18.00 ',4: ' 19.00 - 22.00 '}
tujuan1 = {1: ' bandung ',2: ' cirebon ',3: ' depok '}
# nik = []
# nama = []
# nohp = []
# gender = []
# jam = []
# tanggal = []
# tujuan = []
# nominal = []



# LIST

# USERNAME & PASSWORD ADMIN
admin = 'adi'
codeadmin = '123'


# USERNAME & PASSWORD PEMBELI
pembeli = []
codepembeli = []



# DICTIONARY

data_admin = {
    'nik'     : ['2209106108', '2209106099', '2209106111'],
    'nama'    : ['Alif Naufal F', 'M. Ihsan', 'Aji Dinda N.R'],
    'no hp'   : ['082331644739', '081234567890','089876543210'],
    'gender'  : [' Laki - Laki ', ' Laki - Laki ', '  Perempuan  '],
    'jam'     : [' 07.00 - 11.00 ',' 12.00 - 15.00', ' 16.00 - 18.00 '],
    'tanggal' : ['20 November 2022 ', '21 November 2022 ', '22 November 2022 '],
    'tujuan'  : [' bandung ', ' cirebon ', ' depok '],
    'nominal' : ['50.000 ', '50.000 ', '50.000 ']
}



# MENU REGIS
def registrasi():
    newUser = input("Daftarkan username : ")
    if newUser in admin:
        print("Username sudah ada")
    else:
        newPw = input("Daftarkan password : ")
        pembeli.append(newUser)
        codepembeli.append(newPw)
        # data_admin['nama'].append(newUser)
        # data_admin['nominal'].append(newPw)


        input(" Anda Berhasil Registrasi")
        print ("Akun anda telah terdaftar.")
        os.system("cls")
        print (f"username anda : {newUser} |==| password anda : {newPw}")
        print (" ")

    menulayardepan()



# MENU UTAMA
def menuutama():
    os.system('cls')
    print("menu log in aplikasi")
    print("________________________")
    print("1. ADMIN")
    print("2. PEMBELI")
    print("3. keluar dari aplikasi")
    pilihlog = int(input("masukan pilihan anda : "))
    if pilihlog == 1:
        username = str(input("masukan nama anda : "))
        password = str(input("masukan nama passcode : "))
        if username == admin and password == codeadmin :
            menuadmin()
        elif username != admin and password == codeadmin :
            print("username salah")
            input("kembali")
            menuutama()
        elif username == admin and password != codeadmin :
            print("password salah")
            input("kembali")
            menuutama()
        else:
            print("input anda salah")
            input("kembali")
            menuutama()
    elif pilihlog == 2:
        username1 = str(input("masukan nama anda : "))
        password1 = str(input("masukan nama passcode : "))
        if username1 in pembeli and password1 in codepembeli :
            menupembeli()
        elif username1 not in pembeli and password1 in codepembeli :
            print("username salah")
            input("kembali")
            menuutama()
        elif username1 in pembeli and password1 not in codepembeli :
            print("password salah")
            input("kembali")
            menuutama()
        else:
            print("input anda salah")
            input("kembali")
            menuutama()
    elif pilihlog == 3:
        print("------------------------------------")
        print("---- Terima Kasih Sudah Singgah ----")
        print("------------------------------------")
        sys.exit()
    else:
        print('tidak ada pilihan :-c ')
        input('kembali')
        menuutama()

        

# LOGIN ADMIN         
def masuk():
    salah = 0
    while salah < 3:
        admin = str(input("Masukkan Username: "))
        codeadmin = str(input("Masukkan Password: "))
        if admin == "adi" and codeadmin == "123":
            os.system("cls")
            print("login Berhasil!")
            print("Selamat Datang Admin")
            menuadmin()
        elif admin != "adi" and codeadmin == "123":
            print("Username anda salah.")
            salah+=1
        elif admin == "adi" and codeadmin != "123":
            print("Password anda salah.")
            salah+=1
        else:
            print("Mohon maaf username dan password anda salah.")
            salah+=1           
    if salah == 0 :
        print("Login gagal.")
        admin

        

# FUNGSI

# INPUT GENDER
def pilihgen1():
    print("PILIH JENIS KELAMIN ANDA")
    print("___________________")
    print("1. laki laki")
    print("2. perempuan")
    pilihgen = int(input('masukan nomor : '))
    if pilihgen == 1 in gender1:
        ingender = gender1[1]
        # gender.append({'gender' : ingender})
        data_admin['gender'].append(ingender)
    elif pilihgen == 2 in gender1:
        ingender = gender1[2]
        # gender.append({'gender' : ingender})
        data_admin['gender'].append(ingender)
    else:
        print('tidak ada pilihan :-c ')
        input('ulang')
        pilihgen1()



#INPUT JAM
def piljam1():
    print("PILIH WAKTU KEBERANGKATAN ANDA")
    print("___________________")
    print("1. 07.00 - 11.00")
    print("2. 12.00 - 15.00")
    print("3. 16.00 - 18.00")
    print("4. 19.00 - 22.00")
    pilihjam = int(input('masukan pilihan : '))
    if pilihjam == 1 in jam1:
        injam = jam1[1]
        # jam.append({'jam' : injam})
        data_admin['jam'].append(injam)
    elif pilihjam == 2 in jam1:
        injam = jam1[2]
        # jam.append({'jam' : injam})
        data_admin['jam'].append(injam)
    elif pilihjam == 3 in jam1:
        injam = jam1[3]
        # jam.append({'jam' : injam})
        data_admin['jam'].append(injam)
    elif pilihjam == 4 in jam1:
        injam = jam1[4]
        # jam.append({'jam' : injam})
        data_admin['jam'].append(injam)
    else:
        print('tidak ada pilihan :-c ')
        input('ulang')
        piljam1()



#INPUT TUJUAN
def piljuan1():
    print("PILIH TUJUAN KEBERANGKATAN ANDA")
    print("___________________")
    print("1. bandung")
    print("2. cirebon")
    print("3. depok")
    piljuan = int(input('masukan pilihan : '))
    if piljuan == 1 in tujuan1:
        injuan = tujuan1[1]
        # tujuan.append({'tujuan' : injuan})
        data_admin['tujuan'].append(injuan)
        # print(data_admin['tujuan'])
    elif piljuan == 2 in tujuan1:
        injuan = tujuan1[2]
        # tujuan.append({'tujuan' : injuan})
        data_admin['tujuan'].append(injuan)
    elif piljuan == 3 in tujuan1:
        injuan = tujuan1[3]
        # tujuan.append({'tujuan' : injuan})
        data_admin['tujuan'].append(injuan)
    else:
        print('tidak ada pilihan :-c ')
        input('ulang')
        piljuan1()



# CRUD ( CREATE, READ, UPDATE, DELETE)
        
#CREATE
def tambah():
    innik = input("masukan nik : ")
    # nik.append({'nik' : innik})
    data_admin['nik'].append(innik)
    print(data_admin['nik'])
    innama = input("masukan nama anda : ")
    # nama.append({'nama' : innama})
    data_admin['nama'].append(innama)
    innohp = input("masukan nomor hp : ")
    # nohp.append({'nohp' : innohp})
    data_admin['no hp'].append(innohp)
    pilihgen1()
    piljam1()
    piljuan1()
    intanggal = input("masukan tanggal : ")
    # tanggal.append({'tanggal' : intanggal})
    data_admin['tanggal'].append(intanggal)
    # nominal.append({'harga' : '50.000'})
    data_admin['harga'].append('50.000')

    # print(nik)
    # print(nama)
    # print(nohp)
    print('selesai ! ')
    input('kembali')
    menuadmin()



#READ
def tampil():
    os.system('cls')
    print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------
| Nomor |         NIK          |       Nama      |   No  Handphone   |     Gender     |       Jam      |       Tanggal      |   Tujuan   |   Nominal  |
--------------------------------------------------------------------------------------------------------------------------------------------------------
""")                


    for i in range(len(data_admin["nama"])):
        kolom_1 = str(i+1)
        kolom_2 = str(data_admin['nik'][i])
        kolom_3 = str(data_admin['nama'][i])
        kolom_4 = str(data_admin['no hp'][i])
        kolom_5 = str(data_admin['gender'][i])
        kolom_6 = str(data_admin['jam'][i])
        kolom_7 = str(data_admin['tanggal'][i])
        kolom_8 = str(data_admin['tujuan'][i])
        kolom_9 = str(data_admin['nominal'][i])
        print("|  " + kolom_1 + (5-len(kolom_1))*" "
            + "|  " + kolom_2 + (20-len(kolom_2))*" "
            + "|  " + kolom_3 + (15-len(kolom_3))*" "
            + "|  " + kolom_4 + (17-len(kolom_4))*" "
            + "|  " + kolom_5 + (14-len(kolom_5))*" "
            + "|  " + kolom_6 + (15-len(kolom_6))*" "
            + "|  " + kolom_7 + (17-len(kolom_7))*" "
            + "|  " + kolom_8 + (10-len(kolom_8))*" "
            + "|  " + kolom_9 + (10-len(kolom_9))*" " + "|")
        print(152*"-")



        
#UPDATE
def ubah():
    os.system('cls')
    tampil()
    pilih_nik = input("Masukkan NIK dari data yang ingin diubah: ")
    print(pilih_nik)
    print(data_admin['nik'])
    # cek_indeks = 0

    if(pilih_nik in data_admin['nik']):
            get_index = data_admin['nik'].index(pilih_nik) 
    
            data_admin['nik'].pop(get_index)
            data_admin['nama'].pop(get_index)
            data_admin['no hp'].pop(get_index)
            data_admin['gender'].pop(get_index)
            data_admin['jam'].pop(get_index)
            data_admin['tanggal'].pop(get_index)
            data_admin['tujuan'].pop(get_index)
            data_admin['nominal'].pop(get_index)
            print('masukan data pengganti')

            

            innik = int(input("masukan nik : "))
            data_admin['nik'].append(innik)
            # data_admin['nik'][i] = innik
            # print(data_admin['nik'])
            # nik.append({'nik' : innik})
            # data_admin['nik'].append(innik)
            innama = input("masukan nama anda : ")
            data_admin['nama'].append(innama)
            # nama.append({'nama' : innama})
            # data_admin['nik'].append(innama)
            innohp = input("masukan nomor hp : ")
            data_admin['no hp'].append(innohp)
            # nohp.append({'nohp' : innohp})
            # data_admin['no hp'].append(innohp)
            pilihgen1()
            piljam1()
            piljuan1()
            intanggal = input("masukan tanggal : ")
            # tanggal.append({'tanggal' : intanggal})
            data_admin['tanggal'].append(intanggal)
            # nominal.append({'harga' : '50.000'})
            data_admin['nominal'].append("50.000")
            print('selesai ! ')
            input('kembali')
            

    menuadmin()

    

#DELETE
def hapus():
    os.system('cls')
    tampil()
    innik = input("masukan nik data yang ingin di hapus : ")
    
    if(innik in data_admin['nik']):
            get_index = data_admin['nik'].index(innik) 
            data_admin['nik'].pop(get_index)
            data_admin['nama'].pop(get_index)
            data_admin['no hp'].pop(get_index)
            data_admin['gender'].pop(get_index)
            data_admin['jam'].pop(get_index)
            data_admin['tanggal'].pop(get_index)
            data_admin['tujuan'].pop(get_index)
            data_admin['nominal'].pop(get_index)
        

# PERULANGAN
        
def pilih1():
    ulang = 'y'
    while ulang in('y','Y'):
        os.system('cls')
        innik = input("masukan nik : ")
        # nik.append({'nik' : innik})
        data_admin['nik'].append(innik)
        innama = input("masukan nama anda : ")
        # nama.append({'nama' : innama})
        data_admin['nama'].append(innama)
        innohp = input("masukan nomor hp : ")
        # nohp.append({'nohp' : innohp})
        data_admin['no hp'].append(innohp)
        pilihgen1()
        piljam1()
        piljuan1()
        intanggal = input("masukan tanggal : ")
        # tanggal.append({'tanggal' : intanggal})
        data_admin['tanggal'].append(intanggal)
        # nominal.append({'harga' : '50.000'})
        data_admin['nominal'].append('50.000')
        ulang = input("apakah anda masih ingin menambah y/t : ")


        
# PERCABANGAN
            
# MENU ADMIN
def menuadmin():
    os.system('cls')
    print("selamat datang ADMIN !")
    print("Menu KHUSUS Admin")
    print("--------------------")
    print("1. ubah data ")
    print("2. tampilkan data")
    print("3. hapus data")
    print("4. log out")
    pilih = int(input("masukan pilihan anda : "))
    if pilih == 1:
        print('ubah data')
        ubah()
        menuadmin()
    elif pilih == 2:
        tampil()
        input("kembali ke menu utama")
        menuadmin()
    elif pilih == 3:
        hapus()
        input("kembali ke menu utama")
        menuadmin()
    elif pilih == 4:
        menuutama()
    else:
        print('tidak ada pilihan :-c ')
        input('kembali')
        menuadmin()



# MENU PEMBELI
def menupembeli():
    os.system('cls')
    print("menu aplikasi pembelian")
    print("________________________")
    print("1. pesan tiket anda")
    print("2. tampilkan data")
    print("3. log out")
    pilih = int(input("masukan pilihan anda : "))
    if pilih == 1:
        pilih1()
        menupembeli()
    elif pilih == 2:
        tampil()
        input("kembali")
        menupembeli()
    elif pilih == 3:
        menuutama()
    else:
        print('tidak ada pilihan :-c ')
        input('kembali')
        menupembeli()



#LAYAR DEPAN
def menulayardepan():
    try:
        os.system('cls')
        print('____________________________________________________')
        print(':__________________________________________________:')
        print(':                                                  :')
        print(':                 APLIKASI PESAN                   :')
        print(':                  TIKET KERETA                    :')
        print(':                                                  :')
        print(':         |̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡ ̴̡ı̴̴̡ ̡l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ |          :')
        print(':                                                  :')
        print(':                   1. LOG IN                      :')
        print(':                   2. REGISTRASI                  :')
        print(':                   3. EXIT                        :')
        print('----------------------------------------------------')
        pilihlay = int(input('masukan pilihan anda : '))
        if pilihlay == 1 :
            menuutama()

        elif pilihlay == 2:
            registrasi()
        
        elif pilihlay == 3 :
            print("------------------------------------")
            print("---- Terima Kasih Sudah Singgah ----")
            print("------------------------------------")
            sys.exit()
        else:
            print('tidak ada pilihan :-c ')
            input('kembali')
            menulayardepan()
    except ValueError:
        print('tidak ada pilihan :-c ')
        input('kembali')
        menulayardepan()

        

    
menulayardepan()