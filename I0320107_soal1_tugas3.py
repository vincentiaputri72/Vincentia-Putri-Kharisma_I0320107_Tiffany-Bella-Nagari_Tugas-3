# SOAL 1 TUGAS 3
# PROGRAM LIST UNTUK MENYIMPAN NAMA TEMAN

list_TEMAN = ['Uli', 'Raysa', 'Rara', 'Ica', 'Yola', 'Audrey', 'Ryan', 'Rana', 'Ammar', 'William']
print("TEMAN Vincentia:", list_TEMAN)

# Menampilkan isi indeks 4,6,7
print("Teman 4, 6, 7:",list_TEMAN[4], ",", list_TEMAN[6], ",", list_TEMAN[7])

# Mengganti nama teman 3, 5, 9
list_TEMAN[3] = 'Erysa'
list_TEMAN[5] = 'Alvin'
list_TEMAN[9] = 'Salma'
print("TEMAN Vincentia setelah di ganti:", list_TEMAN)

# Menambah 2 teman
list_TEMAN.append('Talitha')
list_TEMAN.append('Desi')
print("TEMAN Vincentia setelah ditambah:", list_TEMAN)

# Menampilkan semua teman dengan perulangan
print("TEMAN Vincentia diulang 10 kali:", list_TEMAN * 10)

# Menampilkan panjang list
print("Panjang list TEMAN Vincentia:", len(list_TEMAN))
print("Panjang list TEMAN Vincentia diulang 10 kali:", len(list_TEMAN * 10))


