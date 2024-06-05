# Minta input user
nApel = int(input('Masukkan jumlah Apel: '))
nJeruk = int(input('Masukkan jumlah Jeruk: '))
nAnggur = int(input('Masukkan jumlah Anggur: '))

# Definisikan harga buah
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

# Menghitung harga per buah
totalHargaApel = nApel * hargaApel
totalHargaJeruk = nJeruk * hargaJeruk
totalHargaAnggur = nAnggur * hargaAnggur

# Hitung total harga belanja
totalBelanja = totalHargaApel + totalHargaJeruk + totalHargaAnggur

# Tampilkan rincian  belanja
print(f'''
Detail Belanja
      
Apel: {nApel} x {hargaApel} = {totalHargaApel}
Jeruk: {nJeruk} x {hargaJeruk} = {totalHargaJeruk}
Anggur: {nAnggur} x {hargaAnggur} = {totalHargaAnggur}

Total: {totalBelanja}
''')