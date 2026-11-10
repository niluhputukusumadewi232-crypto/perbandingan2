
daftar_obat = {
    "m01": ("Paracetamol", 5000),
    "m02": ("Antasida", 8000),
    "m03": ("Oralit", 3000),
    "m04": ("Cetirizine", 7000),
    "m05": ("Vitamin C", 10000),
    "m06": ("Obat batuk", 12000),
    "m07": ("Balsem", 14500),
    "m08": ("Betadine", 16000),
    "m09": ("Minyak kayu putih", 13500),
    "m10": ("Obat flu", 15000),
}

daftar_pasien = {
    "p01": "Demam",
    "p02": "Flu",
    "p03": "Diare",
    "p04": "Maag",
    "p05": "Alergi",
    "p06": "Infeksi",
    "p07": "Gangguan pernapasan",
    "p08": "Tifus",
    "p09": "DBD",
    "p10": "Pemulihan pascaoperasi",
}

print("""
====================================
             APOTEK DEWI
====================================
          DAFTAR NAMA OBAT
====================================
Kode   Nama Obat             Harga
====================================
""")

for kode, data in daftar_obat.items():
    print(f"{kode}   {data[0]:22} Rp {data[1]}")

print("""
====================================
          DAFTAR PASIEN
====================================
""")

for kode, penyakit in daftar_pasien.items():
    print(kode, penyakit)

print("====================================")

kode_pasien = input("Masukkan kode pasien = ").lower()

if kode_pasien in daftar_pasien:

    nama_pasien = input("Masukkan nama pasien = ")
    penyakit = daftar_pasien[kode_pasien]
    hari = int(input("Lama opname (hari) = "))

    print("\n====================================")
    print("             DATA PASIEN")
    print("====================================")
    print("Nama pasien :", nama_pasien)
    print("Penyakit    :", penyakit)
    print("Lama opname :", hari, "hari")

    print("\nHASIL OPERATOR PERBANDINGAN")
    print("Opname lebih dari 3 hari  :", hari > 3)
    print("Opname kurang dari 7 hari :", hari < 7)
    print("Opname minimal 3 hari     :", hari >= 3)
    print("Opname maksimal 10 hari   :", hari <= 10)
    print("Opname tepat 5 hari       :", hari == 5)
    print("Opname bukan 3 hari       :", hari != 3)

    kode_obat = input("\nMasukkan kode obat = ").lower()

    if kode_obat in daftar_obat:

        nama_obat, harga = daftar_obat[kode_obat]
        jumlah = int(input("Jumlah pembelian obat = "))

        total = harga * jumlah

        print("\n====================================")
        print("           STRUK PEMBELIAN")
        print("====================================")
        print("Nama obat :", nama_obat)
        print("Harga     : Rp", harga)
        print("Jumlah    :", jumlah)
        print("Total     : Rp", total)

        print("\nHASIL PERBANDINGAN JUMLAH OBAT")
        print("Jumlah lebih dari 5  :", jumlah > 5)
        print("Jumlah kurang dari 10:", jumlah < 10)
        print("Jumlah minimal 5     :", jumlah >= 5)
        print("Jumlah maksimal 10   :", jumlah <= 10)
        print("Jumlah tepat 5       :", jumlah == 5)
        print("Jumlah bukan 5       :", jumlah != 5)

        print("====================================")
        print("          TERIMA KASIH")
        print("====================================")

    else:
        print("Kode obat tidak terdaftar!")

else:
    print("Kode pasien tidak terdaftar!")
