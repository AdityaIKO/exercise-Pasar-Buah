import mylib

daftarBuah = [
    [0, 'Apel', 20, 10000],
    [1, 'Jeruk', 15, 15000],
    [2, 'Anggur', 25, 20000]
]

def main():
# print('Selamat Datang di Pasar Buah!')

    listMenu = '''
      
      Selamat Datang di Pasar Buah

      
      List Menu:
      1. Show
      2. Add
      3. Delete
      4. Buy
      5. Exit
      '''

    while True:
        print(listMenu)
        option = input('Masukkan angka menu yang ingin dijalankan: ')

        if option == '1':
            mylib.show(daftarBuah)
        elif option == '2':
            mylib.add(daftarBuah)
        elif option == '3':
            mylib.delete(daftarBuah)
        elif option == '4':
            mylib.buy(daftarBuah)
        elif option == '5':
            break
        else:
            print(input('Input Anda salah. Silakan input ulang!'))


main()


# stockApel = 10
# stockJeruk = 8
# stockAnggur = 15

# # Definisikan harga buah
# hargaApel = 10000
# hargaJeruk = 15000
# hargaAnggur = 20000

# # Minta input jumlah buah dan hitung harga buah
# nApel, totalHargaApel = mylib.inputBuah(nama='Apel', stock = stockApel, harga = hargaApel)
# nJeruk, totalHargaJeruk= mylib.inputBuah(nama='Jeruk', stock = stockJeruk, harga = hargaJeruk)
# nAnggur, totalHargaAnggur = mylib.inputBuah(nama='Anggur', stock = stockAnggur, harga = hargaAnggur)


# # Hitung total harga belanja
# totalBelanja = totalHargaApel + totalHargaJeruk + totalHargaAnggur

# # Tampilkan rincian  belanja
# print(f'''
# Detail Belanja
      
# Apel: {nApel} x {hargaApel} = {totalHargaApel}
# Jeruk: {nJeruk} x {hargaJeruk} = {totalHargaJeruk}
# Anggur: {nAnggur} x {hargaAnggur} = {totalHargaAnggur}

# Total: {totalBelanja}
# ''')

# # proses pembayaran
# while True:
#     # input jumlah uang
#     bayar = int(input('Silakan masukkan uang Anda: '))

#     # hitung selisih antara bayar dengan total
#     selisih = totalBelanja - bayar

#     # bandingkan antara uang dengan total harga
#     if selisih > 0:
#         print(f'Uang Anda kurang sebesar Rp.{selisih}')
#         continue

#     # ucapan terima kasih
#     else:
#         print(f'''
#               Terima kasih!
#               Uang kembalian Anda : Rp.{abs(selisih)}''')
#         break

