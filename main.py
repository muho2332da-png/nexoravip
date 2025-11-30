import os
import sys
import time
from colorama import init, Fore

init(autoreset=True)

VERSION = "1.0.0"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def header():
    print(Fore.CYAN + "=" * 50)
    print(Fore.WHITE + f" Car Parking Multiplayer Tool v{VERSION}".center(50))
    print(Fore.CYAN + "=" * 50)

def print_menu():
    print()
    print(Fore.CYAN + "[1]" + Fore.WHITE + " Oyuncu bilgilerini gir")
    print(Fore.CYAN + "[2]" + Fore.WHITE + " Çıkış")
    print()

def main():
    while True:
        clear()
        header()
        print_menu()
        choice = input(Fore.YELLOW + "Seçimin: " + Fore.WHITE).strip()

        if choice == "1":
            username = input("Kullanıcı adı: ").strip()
            email = input("E-posta: ").strip()
            password = input("Şifre: ").strip()
            print(Fore.GREEN + "\nBilgiler alındı!")
            print(Fore.WHITE + f"Kullanıcı adı: {username}")
            print(Fore.WHITE + f"E-posta: {email}")
            print(Fore.WHITE + f"Şifre: {'*' * len(password)}")
            input("\nDevam etmek için Enter'a bas...")
        elif choice == "2":
            print("Çıkılıyor...")
            time.sleep(0.5)
            sys.exit(0)
        else:
            print("Geçersiz seçim.")
            time.sleep(0.5)

if __name__ == "__main__":
    main()
