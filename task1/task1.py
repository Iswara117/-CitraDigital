from PIL import Image ,ImageDraw

# Buka gambar
gambar = Image.open('test1.jpg')  # Ganti 'contoh.jpg' dengan nama file gambar Anda

# Menampilkan ukuran gambar
ukuran_gambar = gambar.size
print(f'Ukuran gambar: {ukuran_gambar}')

# Mengubah ukuran gambar
ukuran_baru = (100, 150)  # Ganti dengan ukuran yang Anda inginkan
gambar = gambar.resize(ukuran_baru)
gambar.save('gambar_baru.jpg','JPEG' )  # Simpan gambar dengan nama yang berbeda

gambar_hitam_putih = gambar.convert('L')

# Simpan gambar hitam putih
gambar_hitam_putih.save('gambar_hitam_putih.jpg')

# # Memotong bagian tertentu dari gambar
# kotak = (100, 100, 400, 400)  # (x1, y1, x2, y2)
# potongan_gambar = gambar.crop(kotak)
# potongan_gambar.save('potongan_gambar.jpg')

# # Memutar gambar
# gambar_rotasi = gambar.rotate(90)  # Putar 90 derajat searah jarum jam
# gambar_rotasi.save('gambar_rotasi.jpg')

# Menampilkan gambar
tebal_bingkai = 1
warna_bingkai = (255, 0, 0)  # Warna merah dalam mode RGB

# Buat objek ImageDraw untuk menggambar di atas gambar
gambar_digambar = ImageDraw.Draw(gambar)
for x in range(0, ukuran_gambar[0], tebal_bingkai):
    garis_atas = [(x, 0), (x + tebal_bingkai, 0)]
    gambar_digambar.line(garis_atas, fill=warna_bingkai, width=tebal_bingkai)

# Pola putus-putus: Garis horizontal bawah
for x in range(0, ukuran_gambar[0], tebal_bingkai):
    garis_bawah = [(x, ukuran_gambar[1] - 1), (x + tebal_bingkai, ukuran_gambar[1] - 1)]
    gambar_digambar.line(garis_bawah, fill=warna_bingkai, width=tebal_bingkai)

# Pola putus-putus: Garis vertikal kiri
for y in range(0, ukuran_gambar[1], tebal_bingkai):
    garis_kiri = [(0, y), (0, y + tebal_bingkai)]
    gambar_digambar.line(garis_kiri, fill=warna_bingkai, width=tebal_bingkai)

# Pola putus-putus: Garis vertikal kanan
for y in range(0, ukuran_gambar[1], tebal_bingkai):
    garis_kanan = [(ukuran_gambar[0] - 1, y), (ukuran_gambar[0] - 1, y + tebal_bingkai)]
    gambar_digambar.line(garis_kanan, fill=warna_bingkai, width=tebal_bingkai)


    gambar.save('gambar_dengan_bingkai_putus_putus.jpg')

gambar_hitam_putih.show()