import os

def resetos():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def baca_soal():
    try:
        with open('soal.txt', 'r') as file:
            soal = []
            for baris in file:
                bagian = baris.strip().split('||')
                soal.append((bagian[0].strip(), bagian[1].strip()))
            return soal
    except FileNotFoundError:
        print("File soal.txt tidak ditemukan!")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []

def ujian():
    soal_list = baca_soal()
    print("Selamat datang di ujian!")
    print("Jawablah soal-soal berikut.")

    skor = 0
    total_soal = len(soal_list)

    for nomor, (soal, jawaban_benar) in enumerate(soal_list, 1):
        print(f"\nSoal {nomor}: {soal}")
        jawaban_user = input("Jawab: ").strip().lower()

        if jawaban_user == jawaban_benar.lower():
            print("Jawaban benar!")
            skor += 1
        else:
            print(f"Jawaban salah! Jawaban yang benar adalah: {jawaban_benar}")

    print(f"\nUjian selesai! Skor Anda: {skor} dari {total_soal}")

def utama():
    resetos()
    print('Selamat Datang di Program Ujian')
    print('==============v1.0================')
    print('1. Mulai Ujian')
    print('2. Keluar Program')
    try:
        pilih = int(input('Silakan pilih: '))
        if pilih == 1:
            ujian()
        elif pilih == 2:
            print('Terima kasih telah menggunakan program ini :)')
        else:
            print('Masukkan angka yang benar.')
    except ValueError:
        print("Masukkan angka yang valid.")
    input('Tekan enter untuk keluar...')

if __name__ == "__main__":
    utama()
