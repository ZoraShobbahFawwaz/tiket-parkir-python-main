def kategori(NamaLokasi):
    while True:    
        if JenisKendaraan == "MOBIL":
            return "C"
        elif JenisKendaraan == "MOTOR":
            return "M"
        else:
            print("Kendaraan tidak terdaftar!")

def kodlok(kodeLokasi):
    if len(KodeLokasi) > 2:
        print("Kode Lokasi terlalu panjang")
    elif KodeLokasi == "":
        print("Kode Lokasi Kosong!")
    elif len(KodeLokasi) < 2:
        print("Kode Lokasi Kurang!")


print("========== Manless Pos Masuk ===============")
NamaLokasi = str(input("input Nama Lokasi: "))
if NamaLokasi == "":
    print("Nama Lokasi Kosong!")

JenisKendaraan = str(input("Input Jenis Kendaraan: "))
jenis_kendaraan = kategori(JenisKendaraan)

KodeLokasi = str(input("input Kode Lokasi: "))
kodelokasi = kodlok(KodeLokasi)
