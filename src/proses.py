import random


def buat_soal():
    """Membuat satu soal PLSV."""
    a = random.randint(2, 6)
    x = random.randint(1, 10)
    b = random.randint(1, 10)
    c = a * x + b

    soal = f"{a}x + {b} = {c}"
    return {"soal": soal, "jawaban": x}


def periksa_jawaban(jawaban_pengguna, jawaban_benar):
    """Memeriksa jawaban pengguna."""
    return jawaban_pengguna == jawaban_benar


def hitung_nilai(jumlah_benar, jumlah_soal):
    """Menghitung nilai akhir skala 0-100."""
    if jumlah_soal <= 0:
        return 0

    return round((jumlah_benar / jumlah_soal) * 100)