import os
os.system('cls')

while True :
    print(" <== Selamat Datang di POSTTEST 4 ==> ")
    username = input(" <== masukkan username anda  ==> ")
    password = input(" <== masukkan password anda  ==> ")
    os.system('cls')
    if(username == "alif" and password == "alif2964"):
        print(" <== Pilih menu ==> ")
        print("1. Operator Mencari Volume ")
        print("2. Operator Mencari Luas   ")
        print("3.         Exit            ")
        menu = int(input(" <== Masukkan Menu ==> : "))
        os.system('cls')
        if menu == 1:
            print(" <== Selamat Datang di Program Mencari Volume ==> ")
            print(" <== Pilih Program Volume ==> : ")
            print("1. Volume Balok  ")
            print("2. Volume Kubus  ")
            print("3. Volume Prisma ")
            menu1  = int(input("Masukkan Menu : "))
            if menu1 == 1:
                print(" <== Program Balok ==> ")
                panjang = float(input("Masukkan Panjang Balok : "))
                lebar   = float(input("Masukkan Lebar Balok   : "))
                tinggi  = float(input("Masukkan Tinggi Balok  : "))
                volume_balok = (panjang*lebar*tinggi)
                volume_balok = round(volume_balok)
                os.system('cls')
                print('Volume balok',volume_balok)
                break
            elif (menu1 == 2):
                print(" <== Program Kubus ==> ")
                sisi = float(input("Masukkan Sisi Kubus : "))
                volume_kubus = (sisi*sisi*sisi)
                volume_kubus = round(volume_kubus)
                os.system('cls')
                print('Volume kubus',volume_kubus)
                break
            elif (menu1 == 3):
                print(" <== Program Prisma ==> ")
                luas_alas = float(input("Masukkan Luas Alas Prisma : "))
                tinggi    = float(input("Masukkan Tinggi Prisma    : "))
                volume_prisma = (luas_alas*tinggi)
                volume_prisma = round(volume_prisma)
                os.system('cls')
                print('Volume prisma',volume_prisma)
                break
            else:
                print("No Komen")
            
        elif menu == 2:
            print(" <== Selamat Datang di Program Mencari Luas ==> ")
            print(" <== Pilih Program Luas ==> : ")
            print("1. Luas Persegi Panjang")
            print("2. Luas Segitiga")
            print("3. Luas Trapesium")
            print("4. Luas Jajar Genjang")
            print("5. Luas Belah Ketupat")
            menu2 = int(input("Masukkan Menu : "))
            if (menu2 ==  1):
                print(" <== Program Luas Persegi Panjang ==> ")
                panjang = float(input("Masukkan Panjang Persegi Panjang : "))
                lebar   = float(input("Masukkan Lebar Persegi Panjang   : "))
                luas_persegi_panjang = panjang*lebar
                luas_persegi_panjang = round(luas_persegi_panjang)
                os.system('cls')
                print('Luas Persegi Panjang = ',luas_persegi_panjang)
                break
            elif (menu2 == 2):
                print(" <== Program Segitiga ==> ")
                alas   = float(input("Masukkan Alas Segitiga   : "))
                tinggi = float(input("Masukkan Tinggi Segitiga : "))
                luas_segitiga = 0.5*alas*tinggi
                luas_segitiga = round(luas_segitiga)
                os.system('cls')
                print('Luas segitiga',luas_segitiga)
                break
            elif (menu2 == 3):
                print(" <== Program Trapesium ==> ")
                sisi_atas  = float(input("Masukkan Sisi Atas Trapesium  : "))
                sisi_bawah = float(input("Masukkan Sisi Bawah Trapesium : "))
                tinggi     = float(input("Masukkan Tinggi trapesium     : "))
                luas_trapesium = 0.5*(sisi_atas+sisi_bawah)*tinggi
                luas_trapesium = round(luas_trapesium)
                os.system('cls')
                print('luas trapesium',luas_trapesium)
                break
            elif (menu2 == 4):
                print(" <== Program Jajar genjang ==> ")
                alas   = float(input("Masukkan Alas Jajar Genjang   :"))
                tinggi = float(input("Masukkan Tinggi jajar Genjang :"))
                luas_jajargenjang = alas*tinggi
                luas_jajargenjang = round(luas_jajargenjang)
                os.system('cls')
                print('Luas jajargenjang',luas_jajargenjang)
                break
            elif (menu2 == 5):
                print(" <== Program Belah Ketupat ==> ")
                diagonal1 = float(input("Masukkan Diagonal 1 Belah Ketupat : "))
                diagonal2 = float(input("Masukkan Diagonal 2 Belah Ketupat : "))
                luas_belahketupat = (diagonal1*diagonal2)*0.5
                luas_belahketupat = round(luas_belahketupat)
                os.system('cls')
                print('luas belah ketupat',luas_belahketupat)
                break
            else:
                print("No Komen")
                break
    elif username != "alif" and password == "alif2964":
        print("Username anda salah.")
    elif username == "alif" and password != "alif2964":
        print("Password anda salah.")
    else:
        print("Mohon maaf username dan password anda salah.")
            


