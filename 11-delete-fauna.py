import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

#ubah berdasarkan id_pegawai
asal_del = 'Kalimantan'

# menampilkan Query UPDATE SET
kursor.execute(f"DELETE FROM fauna WHERE asal = ?", (asal_del,))
koneksi.commit()

#cek apakah sudah berhasil diubah atau belum
if kursor.rowcount > 0: #cek berdasarkan adanya baris atau tidak
    print(f"data dengan asal Kalimantan {asal_del} berhasil dihapus")
else:
    print(f"tidak ada data fauna dengan asal Kalimantan {asal_del} ")
    
#putuskan koneksi
koneksi.close()