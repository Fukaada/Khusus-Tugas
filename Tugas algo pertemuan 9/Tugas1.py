import difflib
import os

def resetos():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def utama():
    resetos()
    print('Selamat Datang di Program Pengecekan Ulasan File')
    print('   Program dedicated by Fukaada')
    print('==============v1.0================')
    print('1. Masuk Program')
    print('2. Keluar Program')
    try:
        pilih = int(input('Silakan pilih: '))
        if pilih == 1:
            file1, file2 = pilih_file()
            if file1 and file2:
                bandingkan_file(file1, file2)
            else:
                print("Salah satu atau kedua file tidak ditemukan. Program tidak dapat dilanjutkan.")
        elif pilih == 2:
            print('Terima kasih telah menggunakan program ini :)')
        else:
            print('Masukkan angka yang benar.')
    except ValueError:
        print("Masukkan angka yang valid.")
    input('Tekan enter untuk keluar...')

def pilih_file():
    resetos()
    print('Masukkan dua nama file untuk dibandingkan.')
    file_ada = [file.lower() for file in os.listdir()]

    file1 = input('Masukkan nama file pertama: ').strip().lower()
    if file1 not in file_ada:
        print(f'File "{file1}" tidak ditemukan.')
        return None, None

    file2 = input('Masukkan nama file kedua: ').strip().lower()
    if file2 not in file_ada:
        print(f'File "{file2}" tidak ditemukan.')
        return None, None

    return file_ada[file_ada.index(file1)], file_ada[file_ada.index(file2)]

def baca_file(namafile):
    try:
        with open(namafile, 'r') as file:
            return file.readlines()
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file {namafile}: {e}")
        return None

def bandingkan_file(file1, file2):
    print(f'\nPERBEDAAN file "{file1}" dengan file "{file2}"\n')
    teks1 = baca_file(file1)
    teks2 = baca_file(file2)

    if teks1 is None or teks2 is None:
        print("Gagal membaca salah satu file. Pastikan file tersedia dan dapat diakses.")
        return

    if teks1 == teks2:
        print("Kedua file identik.")
        return

    print("Perbedaan jumlah baris:")

    print(f"- Jumlah baris di {file1}: {len(teks1)}")
    print(f"- Jumlah baris di {file2}: {len(teks2)}")
    print("\nPerbedaan isi baris:\n")

    perbedaan = difflib.ndiff(teks1, teks2)

    baris_sama = 0
    baris_berbeda = 0

    for baris in perbedaan:
        if baris.startswith("  "):  # Baris yang sama
            baris_sama += 1
        elif baris.startswith("- ") or baris.startswith("+ "):  # Baris yang berbeda
            baris_berbeda += 1

    # Menampilkan hasil perbandingan
    print(f"Total baris yang sama: {baris_sama}")
    print(f"Total baris yang berbeda: {baris_berbeda}")

    print('\nLetak Perbedaannya Adalah Di =\n')
    perbedaan = difflib.ndiff(teks1, teks2)
    for baris in perbedaan:
        if baris.startswith("- "):
            print(f"Ada di File 1 {file1}: {baris[2:].strip()}")
        elif baris.startswith("+ "):
            print(f"Ada di File 2 {file2}: {baris[2:].strip()}")
        elif baris.startswith("  "):  
            print(f"Baris yang sama di kedua file: {baris[2:].strip()}")
        
if __name__ == "__main__":
    utama()
