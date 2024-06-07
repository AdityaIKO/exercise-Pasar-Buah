def inputBuah(nama, stock, harga):
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
    while True:
        nBuah = int(input(f'Masukkan jumlah {nama}: '))

        if nBuah > stock:
            print(f'Jumlah terlalu banyak, stock tersisa {stock} buah')
            continue

        break

    hargaBuah = nBuah * harga

    return nBuah, hargaBuah