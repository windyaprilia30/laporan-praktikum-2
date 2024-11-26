from collections import deque
def simulasi_antrian():
    antrian = deque()
    while True:
        print("\n 1. Tambah pelanggan ke antrian")
        print("2. Layani pelanggan")
        print("3. Tampilkan antrian")
        print("4. Keluar")
        pilihan = input("pilih opsi :")

        if pilihan == "1":
            nama = input("masukkan nama pelanggan :")
            antrian.append(nama)
            print(f"pelanggan{nama} ditambahkan ke antrian")

        elif pilihan == "2":
            if antrian:
                dilayani = antrian.popleft()
                print(f"pelanggan {dilayani} sedang dilayani")
            else:
                print("antrian kosong!")

        elif pilihan == "3":
            print("Antrian saat ini:", list(antrian))
        elif pilihan == "4":
            print("keluar dari program")
            break
        else:
            print("opsi tidak valid!")
simulasi_antrian()