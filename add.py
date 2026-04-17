d = []
u = []

def tambah():
    a = input("Judul: ")
    b = input("Penulis: ")
    c = input("Tahun: ")
    d.append([a,b,c,"tersedia"])

def tambah2():
    a = input("Nama: ")
    b = input("NIM: ")
    u.append([a,b])

def pinjam():
    nim = input("NIM: ")
    judul = input("Judul: ")
    user_ada = False

    for i in u:
        if i[1] == nim:
            user_ada = True

    if user_ada:
        for j in d:
            if j[0] == judul:
                if j[3] == "tersedia":
                    j[3] = "dipinjam"
                    print("Berhasil")
                else:
                    print("Sudah dipinjam")
    else:
        print("User tidak ada")
