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

| No. | Pengujian | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | Membuat soal PLSV | Program menghasilkan 5 soal secara acak | Berhasil menghasilkan 5 soal | Berhasil |
| 2 | Memeriksa jawaban benar | Jawaban dinyatakan benar | `True` | Berhasil |
| 3 | Memeriksa jawaban salah | Jawaban dinyatakan salah | `False` | Berhasil |
| 4 | Menghitung nilai sempurna | Nilai 100 | Nilai 100 | Berhasil |
| 5 | Menghitung nilai sebagian | Nilai 60 | Nilai 60 | Berhasil |
| 6 | Menghitung nilai tanpa soal | Nilai 0 | Nilai 0 | Berhasil |
| 7 | Validasi jumlah soal | Input tidak valid ditolak | Sesuai harapan | Berhasil |
| 8 | Validasi jawaban | Input bukan bilangan bulat ditolak | Sesuai harapan | Berhasil |

Skenario pengujian dicatat dalam file `tests/test_case.md`.

## Known Issues
- Soal dibuat secara acak sehingga soal yang muncul dapat berbeda setiap program dijalankan.
- Program belum menyimpan hasil latihan ke file.

## Anggota dan Kontribusi
- **Alfitrah Zahra Ameliya:** implementasi program, pengujian, dokumentasi, dan pengelolaan repositori GitHub.

## Referensi/Bantuan
- Bahan Ajar Algoritma dan Pemrograman, Pertemuan 15.
- Dokumentasi Python 3: https://docs.python.org/3/
- Bantuan ChatGPT untuk alur penyusunan dan pemeriksaan kode.