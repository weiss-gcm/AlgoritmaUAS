# Function | Digunakan untuk Menampilkan Menu serta Input untuk memilih pilihan yang muncul pada daftar
def menu():
    print("Daftar Pilihan: ")
    print("1. Tambah Barang")
    print("2. Lihat Daftar")
    print("3. Total Seluruh & Selesaikan Daftar Belanjaan")
    opsi = input("Pilih nomor pada daftar: ")
    return opsi

# Function | Digunakan untuk Menghitung Total akhir dengan jumlah barang (qty) dikalikan dengan harga (pcy)
def qty_ex_pcy(qty, pcy):
    return qty * pcy

# Function & Dictionary | Digunakan untuk Menambah Barang beserta memasukan barang kedalam dictionary menuju List
def plus_tag():
    item_tag = input("Masukan nama barang, press enter jika tidak ada barang: ")
    if item_tag == '':
        print("Program dihentikan karena tidak ada barang yang dimasukkan.")
        return None
    qty_tag = int(input(f"Jumlah barang {item_tag}        : "))
    pcy_tag = int(input(f"Masukan harga barang {item_tag}  : ")) 
    item_info = {
        'Nama Barang': item_tag,
        'Harga Barang': pcy_tag,
        'Jumlah Barang': qty_tag,
        'Total': qty_ex_pcy(qty_tag, pcy_tag) 
    }
    d_list.append(item_info)

# Function | Digunakan untuk Menampilkan List Barang
def show_list():
    if not d_list:
        print("Ga ada data yang dimasukin")
    else:
        print("List Barang & Harga")
        print(f"{'Nama Barang':<20}{'Harga Barang':<20}{'Jumlah Barang':<20}{'Total':<20}")
        print("-" * 67)
        for list_item in d_list:
            print(f"{list_item['Nama Barang']:<20}{list_item['Harga Barang']:<20}{list_item['Jumlah Barang']:<20}{list_item['Total']:<20}")

# Function | Digunakan untuk Menampilkan Total Keseluruhan serta menghitung jumlah kembalian 
def total_result():
    if not d_list:
        print("Tidak ada barang yang dimasukan")
    else:
        total = sum(list_item['Total'] for list_item in d_list)
        print(f"{'Nama Barang':<20}{'Harga Barang':<20}{'Jumlah Barang':<20}{'Total':<20}")
        print("-" * 67)
        for list_item in d_list:
            print(f"{list_item['Nama Barang']:<20}{list_item['Harga Barang']:<20}{list_item['Jumlah Barang']:<20}{list_item['Total']:<20}")
        print("-" * 67)
        print(f"{'Total Keseluruhan':<20}{'':<20}{'':<20}{total:<20}")
        pembayaran = int(input("Jumlah pembayaran : Rp. "))
        kembalian = pembayaran - total 
        print(f"kembalian  : Rp.{kembalian:,.2f}")

# List | Data yang dimasukan pada input Nama barang, Harga barang, Jumlah barang akan disimpan disini
d_list = []

# Looping | Menggunakan While True, agar program dapat diulang hingga user memilih angka 3 (Hasil Akhir) apabila selain 1-3 program akan berhenti
continue_ato_tidak = True
while continue_ato_tidak:
    opsi = menu()
    if opsi == '1':
        plus_tag()
    elif opsi == '2':
        show_list()
    elif opsi == '3':
        total_result()
        continue_ato_tidak = False
    else:
        print("Pilihan ngga sesuai daftar, program keluar")
        continue_ato_tidak = False
