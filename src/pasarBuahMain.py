import pasarBuahLib

daftarBuah = {
    'Apel': [0, 'Apel', 20, 10000],
    'Jeruk': [1, 'Jeruk', 15, 15000],
    'Anggur': [2, 'Anggur', 20, 20000]
    }

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
            pasarBuahLib.show(daftarBuah)
        elif option == '2':
            pasarBuahLib.add(daftarBuah)
        elif option == '3':
            pasarBuahLib.delete(daftarBuah)
        elif option == '4':
            pasarBuahLib.buy(daftarBuah)
        elif option == '5':
            break
        else:
            print(input('Input Anda salah. Silakan input ulang!'))


main()