import hashlib

database_user = {}

def hash_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

def registrasi():
    print("\n" + "=" * 45)
    print("           REGISTRASI USER BARU")
    print("=" * 45)

    username = input("Masukkan username  : ").strip()

    if username in database_user:
        print(f"\n[!] Username '{username}' sudah terdaftar!")
        return

    password = input("Masukkan password  : ").strip()

    if not username or not password:
        print("\n[!] Username dan password tidak boleh kosong!")
        return

    hash_password = hash_sha256(password)
    database_user[username] = hash_password

    print("\n--- HASIL REGISTRASI ---")
    print(f"Username           : {username}")
    print(f"Password Asli      : {password}")
    print(f"Hash SHA-256       : {hash_password}")
    print(f"\n[✓] Registrasi berhasil! User '{username}' telah terdaftar.")

def login():
    print("\n" + "=" * 45)
    print("              LOGIN USER")
    print("=" * 45)

    username = input("Masukkan username  : ").strip()

    if username not in database_user:
        print(f"\n[✗] Login Gagal! Username '{username}' tidak ditemukan.")
        return

    password = input("Masukkan password  : ").strip()

    hash_input = hash_sha256(password)
    hash_tersimpan = database_user[username]

    print("\n--- VERIFIKASI PASSWORD ---")
    print(f"Hash Input         : {hash_input}")
    print(f"Hash Tersimpan     : {hash_tersimpan}")

    if hash_input == hash_tersimpan:
        print(f"\n[✓] Login Berhasil! Selamat datang, {username}!")
    else:
        print(f"\n[✗] Login Gagal! Password salah.")

def tampilkan_database():
    print("\n" + "=" * 45)
    print("          DATABASE USER TERDAFTAR")
    print("=" * 45)

    if not database_user:
        print("Belum ada user yang terdaftar.")
        return

    print(f"{'No':<4} {'Username':<15} {'Hash Password (SHA-256)'}")
    print("-" * 85)
    for i, (username, hash_pw) in enumerate(database_user.items(), 1):
        print(f"{i:<4} {username:<15} {hash_pw}")

def main():
    print("\n" + "=" * 45)
    print("   SISTEM REGISTRASI & LOGIN SHA-256")
    print("=" * 45)

    while True:
        print("\n--- MENU UTAMA ---")
        print("1. Registrasi User")
        print("2. Login User")
        print("3. Tampilkan Database User")
        print("4. Keluar")
        print("-" * 20)

        pilihan = input("Pilih menu (1-4)   : ").strip()

        if pilihan == "1":
            registrasi()
        elif pilihan == "2":
            login()
        elif pilihan == "3":
            tampilkan_database()
        elif pilihan == "4":
            print("\n[✓] Program selesai. Terima kasih!\n")
            break
        else:
            print("\n[!] Pilihan tidak valid. Masukkan angka 1-4.")

main()
