import os

def reset_terminal():
    """Fungsi untuk membersihkan terminal."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def cek_angka_bosku():
    """Fungsi untuk memeriksa tiga angka yang dimasukkan."""
    print('========Input angka========')
    
    while True:
        reset_terminal()  # Reset terminal sebelum input angka
        try:
            print("==========Start Program============")
            print('======Cek angka input dibawah=====')
            angka1 = int(input("Masukkan angka pertama: "))
            angka2 = int(input("Masukkan angka kedua: "))
            angka3 = int(input("Masukkan angka ketiga: "))
        except ValueError:
            print("Masukkan angka yang bener !! bukan huruf atau kombinasi.")
            input("Tekan Enter untuk melanjutkan...")
            continue  # Kembali ke awal untuk meminta input ulang

        # Memeriksa apakah semua angka berbeda
        if angka1 == angka2 or angka1 == angka3 or angka2 == angka3:
            print(f"Angka yang Anda input adalah: {angka1}, {angka2}, {angka3}.")
            print("Angka tidak boleh sama. Hasil: False")
        else:
            # Memeriksa apakah ada dua angka yang dijumlahkan sama dengan angka yang ketiga
            if (angka1 + angka2 == angka3) or (angka2 + angka3 == angka1) or (angka1 + angka3 == angka2):
                print(f"Angka yang Anda input adalah: {angka1}, {angka2}, {angka3}.")
                print("Dua angka yang dijumlahkan sama dengan angka ketiga. Hasil : True")
            else:
                print(f"Angka yang Anda input adalah: {angka1}, {angka2}, {angka3}.")
                print("Tidak ada kombinasi yang memenuhi. Hasil: False")

        # Menawarkan pilihan untuk melanjutkan atau kembali ke menu utama
        pilihan = input("Ketik 'exit()' untuk kembali ke menu utama atau tekan Enter untuk cek angka lagi: ")
        if pilihan.lower() == 'exit()':
            return  # Keluar dari fungsi ini dan kembali ke menu utama

def menu():
    """Menampilkan menu utama."""
    while True:
        reset_terminal()
        print("Selamat Datang Di Program pengecekan Angka")
        print("Angka yang dicek harus memenuhi ketentuan Bila :")
        print('    A. 3 Input Angka tidak boleh sama')
        print('    B. Bila 2 angka dijumlahkan hasilnya angka ke 3')
        print('Jika kondisi terpenuhi maka hasil TRUE,')
        print("Selain Itu bila tidak memenuhi 2 kondisi Maka hasil false")
        print("=================== Masuk Menu ====================")
        print("1. Mulai Program")
        print("2. Keluar")
        
        pilihan = input("Pilih menu (1/2): ")

        if pilihan == '1':
            cek_angka_bosku()  # Panggil fungsi cek_angka_bosku
        elif pilihan == '2':
            print("Terimakasih Telah Menggunakan program ini :)")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
            input("Tekan Enter untuk melanjutkan...")  # Tunggu input dari pengguna

# Program utama yang akan dieksekusi
menu()
