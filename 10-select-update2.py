import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()

# menampilkan Query UPDATE SET
kursor.execute(f'UPDATE fauna SET asal = "Kalimantan Timur" WHERE nama_fauna = "Pesut Mahankam"')
koneksi.commit()

#cek apakah sudah berhasil diubah atau belum
if kursor.rowcount > 0 : 
    print(f"data asal dengan nama fauna Pesut Mahankam berhasil diubah")
else:
    print(f"tidak ada data nama fauna Pesut Mahankam ")
    
#putuskan koneksi
koneksi.close()