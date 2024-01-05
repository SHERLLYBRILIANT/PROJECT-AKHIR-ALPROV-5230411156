import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()

# menampilkan Query UPDATE SET
kursor.execute(f'UPDATE fauna SET jml_skrng = "650" WHERE nama_fauna = "Katak Borneo"')
koneksi.commit()

#cek apakah sudah berhasil diubah atau belum
if kursor.rowcount > 0 : 
    print(f"data jumlah baru dengan nama fauna Katak Borneo berhasil diubah")
else:
    print(f"tidak ada data nama fauna Katak Borneo ")
    
#putuskan koneksi
koneksi.close()