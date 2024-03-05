class GradeMahasiswa: 
    def _init_(self): 
        self.nama = ""
        self.nim = ""
        self.nilai = 0.0
        self.grade = ""

    def input_data(self): 
        self.nama = input("Nama: ")
        self.nim = input("NIM: ")
        self.nilai = float(input("Masukkan nilai: "))

    def hitung_grade(self): 
       if 80 <= self.nilai <= 100:
           self.grade = "A"
       elif 77 <= self.nilai <= 79.99:
           self.grade = "A-"
       elif 74 <= self.nilai <= 76.99:
           self.grade = "B+"
       elif 68 <= self.nilai <= 73.99:
           self.grade = "B"
       elif 65 <= self.nilai <= 67.99:
           self.grade = "B-"
       elif 62 <= self.nilai <= 64.99:
           self.grade = "C+"
       elif 56 <= self.nilai <= 61.99:
           self.grade = "C"
       elif 45 <= self.nilai <= 55.99:
           self.grade = "D"
       else:
           self.grade = "E"

    def tampilkan_info(self): 
        print("--- DATA PRAKTIKAN PBO 2024 ---")
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Grade:", self.grade)

mahasiswa = GradeMahasiswa()

mahasiswa.input_data()

mahasiswa.hitung_grade()

mahasiswa.tampilkan_info()