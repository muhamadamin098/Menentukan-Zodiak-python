def tebak_zodiak():
    try:
        tanggal_lahir = int(input("masukkan tanggal lahir anda : "))
        if tanggal_lahir >= 32:
            print("tanggal lahir hanya sampai 31")
            return""
        bulan_lahir = int(input("masukkan bulan lahir anda : "))
        if bulan_lahir >= 13 :
            print("hanya ada 12 bulan (masukkan bulan yang benar)")
            return""
        zodiak = tentukan_zodiak(tanggal_lahir,bulan_lahir)
        print(f"saya ramal zodiak anda adalah : {zodiak}.")
    except ValueError :
        print("masukkan nilai bulan dan tanggal dengan benar")

    
def tentukan_zodiak(tanggal,bulan):
    #logika
    if (bulan == 3 and tanggal >=21) or (bulan == 4 and tanggal <= 19):
        return "aries"
    elif (bulan == 4 and tanggal >=20) or (bulan == 5 and tanggal <=20):
        return "Taurus"
    elif (bulan == 5 and tanggal >=21) or (bulan == 6 and tanggal <=20):
        return " Gemini"
    elif (bulan == 6 and tanggal >=21) or (bulan == 7 and tanggal <= 22):
        return "cancer"
    elif (bulan == 7 and tanggal >= 23) or (bulan == 8 and tanggal <= 22):
        return "Leo"
    elif (bulan == 8 and tanggal >= 23) or (bulan == 9 and tanggal <= 22):
        return "virgo"
    elif (bulan == 9 and tanggal >= 23) or (bulan == 10 and tanggal <= 22):
        return "Libra"
    elif (bulan == 10 and tanggal >= 23) or (bulan == 11 and tanggal <=21):
        return "Scorpio"
    elif (bulan == 11 and tanggal >= 22) or (bulan == 12 and tanggal <=21):
        return " Sagitarius"
    elif (bulan == 12 and tanggal >= 22) or (bulan == 1 and tanggal <= 19):
        return "capricorn"
    elif (bulan == 1 and tanggal >= 20) or (bulan == 2 and tanggal <= 18):
        return " Aquarius"
    else:
        return " pisces"
#list
daftar_zodiak = ["aries","taurus","gemini",
                 "cancer","Leo","Virgo",
                 "Libra","Scorpio"," sagitarius",
                 "Capricorn","Aquarius","piscer"
                 ]

def cetak_zodiak():
    print(f"ada {len(daftar_zodiak)} zodiak yaitu : ")
    #perulangan for
    for indeks,zodiak in enumerate(daftar_zodiak,start=1):
        print(f"{indeks}.{zodiak}")
    #perulngan while
    while True:
        print("tekan 1 untuk ke menu utama, dan tekan 2 untuk keluar\n")
        opsi = input("pilih : ")
        if opsi == "1":
            program_utama()
            break
        elif opsi == "2":
            print("terimah kasih telah bermain")
            break
        else:
            print("pilih 1 atau 2 ")
        
           
#program utama
print("PROGRAM MENEBAK ZODIAK BERDASARKAN TANGGAL DAN BULAN LAHIR")
def program_utama():
    while True:
        print(
            """SILAHKAN PILIH OPSI DI BAWAH INI !
            1. LIHAT DAFTAR ZODIAK
            2. MULAI BERMAIN
            3. KELUAR
            """)
        pilihan = input("PILIH : ")
        if pilihan == "1":
            cetak_zodiak()
            break
        elif pilihan == "2":
            tebak_zodiak()
            
        elif pilihan == "3":
            print("Sampai jumpa lagi yaa")
            break
        else:
            pass
program_utama()
        
              


