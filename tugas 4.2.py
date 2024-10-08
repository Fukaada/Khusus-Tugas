import os
def otomasi_reset():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system("clear")
def cek_modular():
    while True:
        otomasi_reset()
        try :
            print("======Start Program======")
            print( '=====Masukan input=====')
            angka1 = int(input('Masukan Angka Pertama:'))
            angka2 = int(input('Masukan Angka Kedua:'))
            angka3 = int(input('Masukan Angka ketiga:'))
        except ValueError:
            print("Masukin angkanya yg bener ya syg :)")
            continue
        digit1 = angka1 % 10  
        digit2 = angka2 % 10  
        digit3 = angka3 % 10  
        if digit1 == digit2 == digit3 :
            print(f"Angka yang Anda input adalah: {angka1}, {angka2}, {angka3}.")
            print('3 Digit angka terakhir sama, Hasil = TRUE')
        elif digit1 == digit2 or digit2 == digit3 or digit3 == digit1:
            print(f"Angka yang Anda input adalah: {angka1}, {angka2}, {angka3}.")
            print(" 2 Digit angka terakhir sama, Hasil = TRUE")
        else:
            print(f"Angka yang Anda input adalah: {angka1}, {angka2}, {angka3}.")
            print('tidak ada digit terakhir yang sama, Hasil = FALSE')
        pilihan = input("tulis keluar untuk KELUAR/ Tekan enter atau apapun untuk Melanjutkan....")
        if pilihan.lower() == 'keluar':
            return
        
def menu_utama():
    while True :
        otomasi_reset()
        print("               Selamat Datang di Pengecekan Kesamaan Modular")
        print("======Untuk cek apakah digit terakhir sama dari 3 Angka yang kamu input sama?=====")
        print("                         #Credit by: Fukaada")
        print("1. Masuk Ke program")
        print('2. Keluar')

        try:
            pilihan = int(input("Pilih angka 1/2: "))
        except ValueError:
            print('Pilih angka satu atau dua aja anjai... (Tekan enter)')
            input()
            continue
        
        if pilihan == 1:   
            cek_modular()
        elif pilihan == 2:
            print('terimakasih telah menggunakan program kami')
            break
        else :
            input('pilih angka satu atau 2 aja anjai...(Tekan enter)')
            
menu_utama()
