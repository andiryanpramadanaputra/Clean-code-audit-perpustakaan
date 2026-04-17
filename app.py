from dataclasses import dataclass

STATUS_TERSEDIA = "tersedia"
STATUS_DIPINJAM = "dipinjam"

@dataclass
class Buku:
    judul: str
    penulis: str
    tahun: str
    status: str = STATUS_TERSEDIA

@dataclass
class Anggota:
    nama: str
    nim: str

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []
        self.daftar_anggota = []

    def tambah_buku(self, judul, penulis, tahun):
        self.daftar_buku.append(Buku(judul, penulis, tahun))

    def tambah_anggota(self, nama, nim):
        self.daftar_anggota.append(Anggota(nama, nim))

    def cari_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul == judul:
                return buku
        return None

    def cari_anggota(self, nim):
        for anggota in self.daftar_anggota:
            if anggota.nim == nim:
                return anggota
        return None

    def pinjam_buku(self, nim, judul):
        anggota = self.cari_anggota(nim)
        if not anggota:
            print("Anggota tidak ditemukan")
            return

        buku = self.cari_buku(judul)
        if not buku:
            print("Buku tidak ditemukan")
            return

        if buku.status == STATUS_DIPINJAM:
            print("Buku sudah dipinjam")
            return

        buku.status = STATUS_DIPINJAM
        print("Peminjaman berhasil")
