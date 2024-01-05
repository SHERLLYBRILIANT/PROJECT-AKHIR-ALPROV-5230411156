import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()
#mengambil semua data dalam tabel dan tampilkan 
kursor.execute("SELECT *FROM fauna ORDER BY thn_ditemukan ASC")
#TAMPILKAN DALAM BENTUK BARIS
baris_tabel = kursor.fetchall()

print('tabel FAUNA')
print('='*120)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID FAUNA","NAMA FAUNA","JENIS","ASAL","JUMLAH SAAT INI","TAHUN TERAKHIR DITEMUKAN"))
print('='*120)

#tampil data sesuai format tabel dengan perulangan
for baris in baris_tabel:
    print("{:<8} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
koneksi.close()