import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()
#ambil data berdasarkan total populasi
kursor.execute("SELECT SUM(jml_skrng) FROM fauna")
total_populasi = kursor.fetchone()[0] 

print(f"Total populasi hewan langka saat ini adalah : {total_populasi}")

koneksi.close()