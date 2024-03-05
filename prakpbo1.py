class Penjumlahan:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def jumlahkan(self):
        return self.angka1 + self.angka2

# Menerima input dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Membuat objek dari class Penjumlahan dengan input pengguna
penjumlahan = Penjumlahan(angka1, angka2)

# Melakukan penjumlahan dan mencetak hasilnya
hasil = penjumlahan.jumlahkan()
print("Hasil penjumlahan:", hasil)
