barang = [
    {"nama": "Jaket", "harga": 15000, "stok": 10},
    {"nama": "Sepatu Gunung", "harga": 20000, "stok": 5},
    {"nama": "Tas Carrier", "harga": 25000, "stok": 7},
    {"nama": "Daypack", "harga": 15000, "stok": 8},
    {"nama": "Tenda", "harga": 50000, "stok": 3},
    {"nama": "Sleeping Bag", "harga": 10000, "stok": 6},
    {"nama": "Senter", "harga": 10000, "stok": 15},
    {"nama": "Jas Hujan", "harga": 12000, "stok": 10},
    {"nama": "Sarung Tangan", "harga": 8000, "stok": 20},
    {"nama": "Gaiters", "harga": 10000, "stok": 5},
    {"nama": "Tali", "harga": 5000, "stok": 30},
    {"nama": "Trekking Pole", "harga": 15000, "stok": 4},
]

transaksi = []

admin_password = "admin123"

def login():
    print("\n=== Login ===")
    print("1. Admin")
    print("2. User")
    pilihan = input("Pilih tipe login (1/2): ")
    if pilihan == "1":
        password = input("Masukkan password Admin: ")
        if password == admin_password:
            print("Password benar. Anda login sebagai Admin.")
            return "admin"
        else:
            print("Password salah. Akses ditolak.")
            return login()
    elif pilihan == "2":
        print("Anda login sebagai User.")
        return "user"
    else:
        print("Pilihan tidak valid.")
        return login()


def lihat_barang():
    print("\n=== Daftar Barang untuk Disewa ===")
    for idx, item in enumerate(barang):
        print(f"{idx+1}. {item['nama']} - Harga: {item['harga']} - Stok: {item['stok']}")

def tambah_barang():
    print("\n=== Tambah Barang Baru ===")
    nama = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga barang: "))
    stok = int(input("Masukkan stok barang: "))
    barang.append({"nama": nama, "harga": harga, "stok": stok})
    print(f"Barang '{nama}' berhasil ditambahkan!")

def edit_barang():
    lihat_barang()
    pilihan = int(input("\nMasukkan nomor barang yang ingin diedit: ")) - 1
    if 0 <= pilihan < len(barang):
        nama = input(f"Masukkan nama baru (kosongkan untuk tidak mengubah): ") or barang[pilihan]["nama"]
        harga = input(f"Masukkan harga baru (kosongkan untuk tidak mengubah): ")
        stok = input(f"Masukkan stok baru (kosongkan untuk tidak mengubah): ")

        barang[pilihan]["nama"] = nama
        if harga:
            barang[pilihan]["harga"] = int(harga)
        if stok:
            barang[pilihan]["stok"] = int(stok)
        print(f"Barang '{barang[pilihan]['nama']}' berhasil diperbarui!")
    else:
        print("Pilihan tidak valid.")

def hapus_barang():
    lihat_barang()
    pilihan = int(input("\nMasukkan nomor barang yang ingin dihapus: ")) - 1
    if 0 <= pilihan < len(barang):
        barang_dihapus = barang.pop(pilihan) #elemen tertentu
        print(f"Barang '{barang_dihapus['nama']}' berhasil dihapus!")
    else:
        print("Pilihan tidak valid.")

def sewa_barang():
    nama_penyewa = input("Masukkan nama orang yang ingin menyewa: ")

    lihat_barang()
    total_harga = 0
    jumlah_barang = 0

    while True:
        pilihan = int(input("\nMasukkan nomor barang yang ingin disewa (0 untuk selesai): ")) - 1
        if pilihan == -1:
            break

        if 0 <= pilihan < len(barang):
            jumlah = int(input(f"Masukkan jumlah {barang[pilihan]['nama']} yang ingin disewa: "))
            if jumlah <= barang[pilihan]["stok"]:
                lama_sewa = int(input("Masukkan lama sewa (maksimal 5 hari): "))
                if lama_sewa > 5:
                    biaya_tambahan = (lama_sewa - 5) * 5000
                    harga_sewa = jumlah * barang[pilihan]["harga"] * lama_sewa + biaya_tambahan
                    print(f"Biaya tambahan untuk {lama_sewa - 5} hari: {biaya_tambahan}")
                else:
                    harga_sewa = jumlah * barang[pilihan]["harga"] * lama_sewa
                total_harga += harga_sewa
                jumlah_barang += 1
                barang[pilihan]["stok"] -= jumlah
                transaksi.append({
                    "nama_barang": barang[pilihan]["nama"],
                    "jumlah": jumlah,
                    "lama_sewa": lama_sewa,
                    "harga_sewa": harga_sewa,
                    "nama_penyewa": nama_penyewa
                })
                print(f"Berhasil menyewa {jumlah} {barang[pilihan]['nama']}. Harga: {harga_sewa}")
            else:
                print("Maaf, stok tidak mencukupi.")
        else:
            print("Pilihan tidak valid.")

        lagi = input("Apakah Anda ingin menyewa barang lagi? (y/n): ")
        if lagi.lower() != 'y':
            break

    if jumlah_barang >= 3:
        diskon = total_harga * 0.05
        total_harga -= diskon
        print(f"Anda mendapatkan diskon 5% karena menyewa minimal 3 barang. Diskon: {diskon}")

    print(f"Total harga yang harus dibayar: {total_harga}")

    print("\nPilih jenis jaminan:")
    print("1. KTP")
    print("2. SIM")
    print("3. KTM")
    jenis_jaminan = input("Masukkan nomor jenis jaminan (1/2/3): ")

    if jenis_jaminan == "1":
        jaminan = "KTP"
    elif jenis_jaminan == "2":
        jaminan = "SIM"
    elif jenis_jaminan == "3":
        jaminan = "KTM"
    else:
        print("Pilihan tidak valid. Transaksi dibatalkan.")
        for t in transaksi:
            for item in barang:
                if item["nama"] == t["nama_barang"]:
                    item["stok"] += t["jumlah"]
        transaksi.clear()
        print("Stok barang telah dikembalikan.")
        return

    print(f"Jaminan berhasil diterima: {jaminan}")
    print("\n=== Metode Pembayaran ===")
    print("1. Cash")
    metode = input("Pilih metode pembayaran: ")
    if metode != "1":
        print("Metode pembayaran yang dipilih tidak valid. Transaksi dibatalkan.")
        for t in transaksi:
            for item in barang:
                if item["nama"] == t["nama_barang"]:
                    item["stok"] += t["jumlah"]
        transaksi.clear()
        print("Stok barang telah dikembalikan.")
    else:
        print("Pembayaran berhasil. Terima kasih sudah menyewa!")

def lihat_barang_yang_disewa():
    if not transaksi:
        print("\nBelum ada barang yang disewa.")
        return

    print("\n=== Barang yang Disewa ===")
    for t in transaksi:
        print(f"{t['nama_barang']} - Jumlah: {t['jumlah']} - Lama Sewa: {t['lama_sewa']} hari - Harga Sewa: {t['harga_sewa']}")

def pengembalian_barang():
    if not transaksi:
        print("\nBelum ada barang yang disewa.")
        return

    print("\n--- Data Transaksi Penyewaan ---")
    for idx, t in enumerate(transaksi):
        print(f"{idx+1}. {t['nama_barang']} - Jumlah: {t['jumlah']} - Lama Sewa: {t['lama_sewa']} hari - Harga Sewa: {t['harga_sewa']}")

    pilihan = int(input("\nMasukkan nomor transaksi yang ingin dikembalikan: ")) - 1
    if 0 <= pilihan < len(transaksi):
        hari_terlambat = int(input("Masukkan jumlah hari terlambat: "))
        if hari_terlambat > 0:
            denda = hari_terlambat * 5000
        else:
            denda = 0

        print(f"Barang '{transaksi[pilihan]['nama_barang']}' berhasil dikembalikan. Denda: {denda}")
        barang_dikembalikan = transaksi.pop(pilihan)

        for item in barang:
            if item["nama"] == barang_dikembalikan["nama_barang"]:
                item["stok"] += barang_dikembalikan["jumlah"]

    else:
        print("Pilihan tidak valid.")

def menu(user_type):
    while True:
        if user_type == "admin":
            print("\n=== Menu Admin ===")
            print("1. Lihat Barang")
            print("2. Tambah Barang")
            print("3. Edit Barang")
            print("4. Hapus Barang")
            print("0. Keluar")
            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                lihat_barang()
            elif pilihan == "2":
                tambah_barang()
            elif pilihan == "3":
                edit_barang()
            elif pilihan == "4":
                hapus_barang()
            elif pilihan == "0":
                print("Keluar dari menu Admin...")
                return  
            else:
                print("Pilihan tidak valid.")
        elif user_type == "user":
            print("\n=== Menu User ===")
            print("1. Lihat Barang")
            print("2. Sewa Barang")
            print("3. Pengembalian Barang")
            print("4. Lihat Barang yang sudah Disewa")
            print("0. Keluar")
            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                lihat_barang()
            elif pilihan == "2":
                sewa_barang()
            elif pilihan == "3":
                pengembalian_barang()
            elif pilihan == "4":
                lihat_barang_yang_disewa()
            elif pilihan == "0":
                print("Keluar dari menu User...")
                return  
            else:
                print("Pilihan tidak valid.")


if __name__ == "__main__":
    while True:
        user_type = login() 
        menu(user_type)  
