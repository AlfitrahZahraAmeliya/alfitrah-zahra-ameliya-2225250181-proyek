# Program Generator Soal Persamaan Linear Satu Variabel (PLSV)

## Deskripsi
Program ini merupakan generator soal Persamaan Linear Satu Variabel (PLSV) berbasis Python. Program menghasilkan soal secara acak, memeriksa jawaban pengguna, dan menghitung nilai akhir latihan.

## Fitur
- Menghasilkan soal PLSV secara acak.
- Memeriksa jawaban benar dan salah.
- Menghitung nilai akhir dalam skala 0–100.
- Memvalidasi jumlah soal antara 1 sampai 10.
- Memvalidasi input jawaban agar berupa bilangan bulat.
- Menampilkan ringkasan hasil latihan.

## Persyaratan
- Python 3.x
- Visual Studio Code (disarankan)
- Git (untuk pengelolaan versi)

## Cara Menjalankan
1. Buka folder proyek di Visual Studio Code.
2. Buka terminal pada folder utama proyek.
3. Jalankan perintah:

```bash
python main.py
```

4. Masukkan jumlah soal antara 1 sampai 10.
5. Jawab setiap soal dengan memasukkan nilai x.
6. Program menampilkan hasil latihan dan nilai akhir.

## Struktur Folder
```text
alfitrah-zahra-ameliya-2225250181-proyek/
├── README.md
├── .gitignore
├── main.py
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── proses.py
│   └── output.py
├── data/
│   └── contoh_data.txt
├── tests/
│   └── test_case.md
└── docs/
    └── screenshot/
```

## Test Case
Skenario pengujian mencakup:
- Pembuatan soal PLSV.
- Pemeriksaan jawaban benar dan salah.
- Perhitungan nilai sempurna.
- Perhitungan nilai sebagian.
- Perhitungan nilai ketika jumlah soal nol.
- Validasi jumlah soal yang tidak valid.
- Validasi jawaban yang bukan bilangan bulat.

Hasil aktual dan status pengujian dicatat dalam `tests/test_case.md`.

## Known Issues
- Soal dibuat secara acak sehingga soal yang muncul dapat berbeda setiap program dijalankan.
- Program belum menyimpan hasil latihan ke file.

## Anggota dan Kontribusi
- **Alfitrah Zahra Ameliya:** implementasi program, pengujian, dokumentasi, dan pengelolaan repositori GitHub.

## Referensi/Bantuan
- Bahan Ajar Algoritma dan Pemrograman, Pertemuan 15.
- Dokumentasi Python 3: https://docs.python.org/3/
- Bantuan ChatGPT untuk alur penyusunan dan pemeriksaan kode.