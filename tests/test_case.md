# Test Case Generator Soal PLSV

| No. | Pengujian | Data Masukan | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | Membuat soal PLSV | Jumlah soal 5 | Program menghasilkan soal PLSV secara acak | Program berhasil menghasilkan 5 soal | Berhasil |
| 2 | Memeriksa jawaban benar | Jawaban pengguna 5, jawaban benar 5 | `True` | `True` | Berhasil |
| 3 | Memeriksa jawaban salah | Jawaban pengguna 3, jawaban benar 5 | `False` | `False` | Berhasil |
| 4 | Menghitung nilai sempurna | 5 benar dari 5 soal | Nilai 100 | Nilai 100 | Berhasil |
| 5 | Menghitung nilai sebagian | 3 benar dari 5 soal | Nilai 60 | Nilai 60 | Berhasil |
| 6 | Menghitung nilai tanpa soal | 0 benar dari 0 soal | Nilai 0 | Nilai 0 | Berhasil |
| 7 | Validasi jumlah soal | `abc`, `11`, `0`, `5` | Menolak tiga input pertama dan menerima 5 | Sesuai harapan | Berhasil |
| 8 | Validasi jawaban | `abc`, `5` | Menolak `abc` dan menerima 5 | Sesuai harapan | Berhasil |

## Kesimpulan

Berdasarkan pengujian yang telah dilakukan, fungsi pembuatan soal, pemeriksaan jawaban, perhitungan nilai, dan validasi input berjalan sesuai harapan.