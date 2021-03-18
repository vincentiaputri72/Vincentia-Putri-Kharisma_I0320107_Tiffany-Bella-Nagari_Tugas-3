# SOAL 2 TUGAS 3
# PROGRAM DICTIONARY

# Nama, Hobi, Sosial media, Lagu kesukaan, Makanan favorit
dict = {'Nama': 'Vincentia', 'Hobi1': 'Nonton', 'Hobi2': 'Membaca', 'Hobi3': 'Tidur', 'Sosmed1': 'Ig: @vincentia_pk', 'Sosmed2': 'Twitter: @longlivvvve', 'Sosmed3': 'linkedIn: Vincentia Putri', 'Lagu1': 'Apocalypse', 'Lagu2': 'Do I Wanna Know?', 'Lagu3': 'Sweater Weather', 'Makanan1': 'nasi goreng', 'Makanan2': 'mi ayam', 'Makanan3': 'martabak'}
print("dict:", dict)

# Mengubah Hobi dan Sosial media
dict['Hobi1'] = 'jalan-jalan'
dict['Sosmed1'] = 'LINE: @vincentia17'
print("dict setelah salah satu hodi dan sosial media diubah:", dict)

# Menghapus 2 makanan favorit
del dict['Makanan1']
del dict['Makanan3']
print("dict setelah 2 makanan favorit dihapus:", dict)

# Menambah 1 hobi baru
dict['Hobi4'] = 'Menggambar'
print("dict setelah menambah hobi baru:", dict)

