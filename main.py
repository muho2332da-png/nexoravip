# main.py
import os
import sys
import time
from colorama import init, Fore, Style
from utils import APIClient, generate_fingerprint, verificar_key_com_fingerprint, login

init(autoreset=True)

VERSION = "1.0.0"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def header():
    print(Fore.CYAN + "=" * 59)
    print(Fore.WHITE + f"  Car Parking Multiplayer Tool  v{VERSION}".center(59))
    print(Fore.CYAN + "=" * 59)

def print_menu():
    print()
    print(Fore.CYAN + "[1]" + Fore.WHITE + " Giriş yap (login)")
    print(Fore.CYAN + "[2]" + Fore.WHITE + " Key + Fingerprint doğrula")
    print(Fore.CYAN + "[3]" + Fore.WHITE + " Profil bilgilerini getir (API)")
    print(Fore.CYAN + "[4]" + Fore.WHITE + " Çıkış")
    print()

def main():
    api_base = os.environ.get("CPM_API_BASE", "https://example-cpm-api.local")
    client = APIClient(base_url=api_base)
    fingerprint = generate_fingerprint()

    while True:
        clear()
        header()
        print(f"API Base: {api_base}")
        print(f"Fingerprint: {fingerprint[:12]}...")  # uzunsa kısa göster
        print_menu()
        choice = input(Fore.YELLOW + "Seçimin: " + Fore.WHITE).strip()

        if choice == "1":
            username = input("Kullanıcı adı: ").strip()
            password = input("Şifre: ").strip()
            print("Giriş yapılıyor...")
            res = login(client, username, password)
            if res.get("ok"):
                print(Fore.GREEN + "Giriş başarılı.")
            else:
                print(Fore.RED + "Giriş başarısız:", res)
            input("Devam etmek için Enter'a bas...")

        elif choice == "2":
            key = input("API Key veya lisans anahtarı: ").strip()
            print("Doğrulanıyor...")
            res = verificar_key_com_fingerprint(client, key, fingerprint)
            if res.get("ok"):
                print(Fore.GREEN + "Key doğrulandı:", res.get("data", res))
            else:
                print(Fore.RED + "Doğrulama başarısız:", res)
            input("Devam etmek için Enter'a bas...")

        elif choice == "3":
            print("Profil istek atılıyor...")
            try:
                r = client.get("/profile")
                if r.status_code == 200:
                    print(Fore.GREEN + "Profil verisi:")
                    print(r.json())
                else:
                    print(Fore.RED + f"İstek başarısız: {r.status_code} {r.text}")
            except Exception as e:
                print(Fore.RED + "Hata:", e)
            input("Devam etmek için Enter'a bas...")

        elif choice == "4":
            print("Çıkılıyor...")
            time.sleep(0.4)
            sys.exit(0)
        else:
            print("Geçersiz seçim.")
            time.sleep(0.4)

if __name__ == "__main__":
    main()
