from tabulate import tabulate

def stringValidation(title):
    """Fungsi untuk validasi tipe data string

    Args:
        title (String): Pesan yang akan ditampilkan pada layar

    Returns:
        String: Nilai yang diinputkan
    """
    while True:
        teks = input(title)
        if teks.isalpha() == True:
            break
        else:
            print('Silakan input hanya teks')
    return teks.capitalize()

def integerValidation(title, minval = 0, maxval = 100):
    """Fungsi untuk validasi bilangan bulat

    Args:
        title (String): Pesan yang akan ditampilkan pada layar
        minval (int, optional): Nilai minimal. Defaults to 0.
        maxval (int, optional): Nilai maksimal. Defaults to 100.

    Returns:
        Int: Nilai yang diinputkan
    """
    while True:
        num = input(title)
        try:
            num = int(num)
            if num >= minval and num <= maxval:
                break
            else:
                print('Angka yang Anda masukkan di luar rentang.')
        except:
            print('Yang anda inputkan bukan bilangan')
    return num

def show(database, header = ['index', 'stock', 'name', 'price']):
    print(tabulate(database.values(), headers = header, tablefmt = 'grid'))

def add(database):
    name = stringValidation('Masukkan nama buah: ')
    stock = integerValidation(
        title = 'Masukkan stock buah: ',
        minval = 0
    )
    price = integerValidation(
        title = 'Masukkan harga buah: ',
        minval = 0,
        maxval = 100000
    )

    for key, buah in database.items():
        if name in buah:
            database[key] = [buah[0], name, stock, price]
            break
    else:
        database[name] = [len(database), name, stock, price]
    
    # menampilkan database terupdate
    show(database)

def delete(database):

    show(database)

    # meminta user input indeks yang akan dihapus
    idx = integerValidation(
        title = 'Masukkan index buah yang ingin dihapus: ',
        maxval = len(database)
    )

    for key, buah in database.copy().items():
        if idx in buah:
            del database[key]
            break
    else:
        print('Buah yang Anda cari tidak tersedia')

        # Memperbarui index
    for id, buah in enumerate(database.values()):
        if id != buah[0]:
            database[buah[1]][0] = id

        # menampilkan database terbaru
    show(database)

def buy(database):

    databaseTemp = database.copy()
    keranjang = {}
    reorder = None
    
    while reorder != 'No':

        show(databaseTemp)

          #meminta user input indeks dan jumlah buah yang ingin dibeli
        id = integerValidation(
            title = 'Silakan masukan index buah: ',
            minval = 0,
            maxval = len(database) - 1
            )

        for key, val in databaseTemp.items():
            if id  == val[0]:
                name = key

        stock = integerValidation(
            title = 'Silakan masukkan jumlah buah: ',
            minval = 0,
            maxval = database[name][2]
            )

        # Menambahkan ke dalam keranjang belanja
        keranjang.update(
            {name: [name, stock, databaseTemp[name][3]]}
        )
        
        # Menampilkan kernjang belanja updated
        show(database = keranjang, header = ['Nama', 'Qty', 'Harga'])

        # konfirmasi reorder
        while True:
            status = stringValidation('Mau beli yang lain? ').lower()
            if status in ['yes', 'y', 'ya']:
                reorder = 'Yes'
            elif status in ['no', 'n', 'tidak']:
                reorder = 'No'
            break

        databaseTemp[name][2] -= stock

    # Menghitung total harga
    total = 0
    for key, buah in keranjang.items():
        # Hitung total harga buah
        totalHarga = buah[1] * buah[2]
        # Input total harga ke keranjang
        keranjang[key].append(totalHarga)
        #sum seluruh harga
        total += totalHarga

    # Menampilkan kernjang belanja updated
    show(database = keranjang, header = ['Nama', 'Qty', 'Harga', 'Total Harga'])

    # Menampilkan uang yang harus dibayar
    print(f'Total yang harus Anda bayar adalah Rp.{total}')

    # proses pembayaran
    pembayaran(total)

    # update database
    database = databaseTemp.copy()

def pembayaran(totalHarga):
    while True:
        # input jumlah uang
        bayar = int(input('Silakan masukkan uang Anda: Rp. '))

        # hitung selisih antara bayar dengan total
        selisih = totalHarga - bayar

        # bandingkan antara uang dengan total harga
        if selisih > 0:
            print(f'Uang Anda kurang sebesar Rp.{selisih}')
            continue

        # ucapan terima kasih
        else:
            print(f'''
                Terima kasih!
                Uang kembalian Anda : Rp.{abs(selisih)}''')
            break
    
            



# def inputBuah(nama, stock, harga):
    """Fungsi untuk meminta user input jumlah buah
    dan menghitung harganya

    Args:
        nama (String): Nama buah yang akan dibeli
        stock (Integer): Stock buah yang akan dibeli
        harga (Integer): Harga buah per kg

    Retruns:
        nBuah (Integer): Jumlah buah yang dipesan
        hargaBuah (Integer): Total harga buah
    """

