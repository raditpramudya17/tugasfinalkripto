import hashlib

# Dictionary untuk menyimpan data user (Username: Hash Password)
database_user = {}

def hitung_sha256(password):
    # Mengubah password menjadi hash SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def registrasi():
    print("\n--- MENU REGISTRASI ---")
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")
    
    # Proses hashing SHA-256 [cite: 99]
    hash_password = hitung_sha256(password)
    
    # Menyimpan username dan hash [cite: 100]
    database_user[username] = hash_password
    
    print(f"User {username} berhasil didaftarkan!")
    print(f"Hash Password disimpan: {hash_password}") # [cite: 101]

def login():
    print("\n--- MENU LOGIN ---")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    # Verifikasi apakah user ada di database
    if username in database_user:
        # Hash password input untuk dibandingkan dengan yang tersimpan 
        hash_input = hitung_sha256(password)
        
        if hash_input == database_user[username]:
            print("Status Login: BERHASIL!") # 
        else:
            print("Status Login: GAGAL! Password salah.")
    else:
        print("Status Login: GAGAL! Username tidak ditemukan.")

# Simulasi Jalannya Program
if __name__ == "__main__":
    # 1. Registrasi User [cite: 98]
    registrasi()
    
    # 2. Login User [cite: 102]
    login()