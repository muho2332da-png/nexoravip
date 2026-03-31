# ================================================
# AUREX3T CPM CHEATS - v2.6.2
# Owner: @Aurex3t
# ================================================

import os
import sys
from time import sleep
import signal

__OWNER__ = "@Aurex3t"
__TOOL_NAME__ = "AUREX3T CPM CHEATS"
CURRENT_VERSION = "2.6.2"

try:
    from colorama import init
    init()
    from pystyle import Anime, Colors, Colorate, Center, Box
    from rich.console import Console
    from rich.prompt import Prompt, IntPrompt
except:
    os.system("pip install colorama pystyle rich --quiet")
    from colorama import init
    init()
    from pystyle import Anime, Colors, Colorate, Center, Box
    from rich.console import Console
    from rich.prompt import Prompt, IntPrompt

console = Console()

def signal_handler(sig, frame):
    console.print("\n[bold red]Çıkış yapılıyor...[/bold red]")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear()
    brand = f"""
 ██████╗██████╗ ███╗   ███╗ ██████╗██╗  ██╗███████╗ █████╗ ████████╗███████╗
██╔════╝██╔══██╗████╗ ████║██╔════╝██║  ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝
██║     ██████╔╝██╔████╔██║██║     ███████║█████╗  ███████║   ██║   ███████╗
██║     ██╔═══╝ ██║╚██╔╝██║██║     ██╔══██║██╔══╝  ██╔══██║   ██║   ╚════██║
╚██████╗██║     ██║ ╚═╝ ██║╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████║
 ╚═════╝╚═╝     ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝

                    @Aurex3t CPM CHEATS v{CURRENT_VERSION}
    """
    Anime.Fade(Center.Center(brand), Colors.red_to_yellow, Colorate.Vertical, enter=True)
    
    console.print(Center.XCenter("[bold yellow]══════════════════════════════════════════════════════════════[/bold yellow]"))
    console.print(Center.XCenter(f"[bold red]OWNER: {__OWNER__} | PAYLAŞIM YASAKTIR[/bold red]"))
    console.print(Center.XCenter("[bold yellow]══════════════════════════════════════════════════════════════[/bold yellow]"))

if __name__ == "__main__":
    while True:
        banner()
        
        console.print("\n[bold cyan][?] ACCOUNT EMAIL[/bold cyan]")
        acc_email = Prompt.ask("   Email")
        
        console.print("[bold cyan][?] ACCOUNT PASSWORD[/bold cyan]")
        acc_password = Prompt.ask("   Password", password=False)
        
        console.print("[bold cyan][?] ACCESS KEY[/bold cyan]")
        acc_access_key = Prompt.ask("   Access Key")

        console.print("\n[%] Giriş yapılıyor...", end=" ")
        
        try:
            from cpmcheats import CPMCheats
            cpm = CPMCheats(acc_access_key)
            login_response = cpm.login(acc_email, acc_password)
        except Exception as e:
            console.print("[bold red]FAILED[/bold red]")
            console.print(f"[red]Hata: {e}[/red]")
            console.print("[yellow]cpmcheats modülü yüklü değil veya access key hatalı.[/yellow]")
            sleep(3)
            continue

        if login_response != 0:
            console.print("[bold red]LOGIN FAILED[/bold red]")
            sleep(2)
            continue

        console.print("[bold green]SUCCESSFUL ✓[/bold green]")
        sleep(1.5)

        while True:
            banner()
            console.print(f"[bold green]Hoş geldin {__OWNER__}[/bold green]\n")

            print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(
                Box.DoubleCube(
                    "➩ (01) Money          (02) Coins\n"
                    "➩ (03) King Rank      (04) Change ID\n"
                    "➩ (05) Name           (06) Rainbow Name\n"
                    "➩ (07) Plates         (08) Delete Account\n"
                    "➩ (09) Register       (10) Delete Friends\n"
                    "➩ (11) Lambo          (12) All Cars\n"
                    "➩ (13) All Siren      (14) W16\n"
                    "➩ (15) Horns          (16) No Damage\n"
                    "➩ (17) Unlimited Fuel (18) House 3\n"
                    "➩ (19) Smoke          (20) Wheels\n"
                    "➩ (21) Animations     (22) Equip M\n"
                    "➩ (23) Equip F        (24) Race Wins\n"
                    "➩ (25) Race Loses     (26) Clone Account\n"
                    "➩ (27) Custom HP      (28) Angle\n"
                    "➩ (29) Tire Burner    (30) Mileage\n"
                    "➩ (31) Brake          (32) Rear Bumper\n"
                    "➩ (33) Front Bumper   (34) Password\n"
                    "➩ (35) Email          (36) Spoiler\n"
                    "➩ (37) BodyKit        (38) Premium Wheels\n"
                    "➩ (39) Toyota Crown   (40) Clan Hat\n"
                    "➩ (41) Head M         (42) Head F\n"
                    "➩ (43) Top1 M         (44) Top2 M\n"
                    "➩ (45) Top3 M         (46) Top1 FM\n"
                    "➩ (47) Top2 FM        (48) Mercedes CLS\n"
                    "➩ (49) Speed Hack     (50) Paid Cars\n"
                    "➩ (51) Stance         (52) Copy Livery\n"
                    "➩ (00) Exit"
                )
            )))

            service = IntPrompt.ask("[bold]Seçim yap [0-52][/bold]", choices=[str(i) for i in range(53)], show_choices=False)

            if service == 0:
                console.print("[bold white]Teşekkürler @Aurex3t, araç kapatılıyor...[/bold white]")
                sys.exit(0)

            console.print("[%] İşlem yapılıyor...", end=" ")
            success = False

            try:
                if service == 1:
                    amount = IntPrompt.ask("[?] Amount")
                    success = cpm.set_player_money(amount)
                elif service == 2:
                    amount = IntPrompt.ask("[?] Amount")
                    success = cpm.set_player_coins(amount)
                elif service == 3:
                    success = cpm.set_player_rank()
                elif service == 4:
                    new_id = Prompt.ask("[?] New ID")
                    success = cpm.set_player_localid(new_id.upper())
                elif service == 5:
                    new_name = Prompt.ask("[?] New Name")
                    success = cpm.set_player_name(new_name)
                elif service == 6:
                    new_name = Prompt.ask("[?] Rainbow Name")
                    success = cpm.set_player_name(new_name)
                elif service == 7:
                    success = cpm.set_player_plates()
                elif service == 8:
                    if Prompt.ask("[?] Delete account? (y/n)", choices=["y","n"]) == "y":
                        cpm.delete()
                        success = True
                elif service == 9:
                    e = Prompt.ask("[?] New Email")
                    p = Prompt.ask("[?] New Password")
                    if cpm.register(e, p) == 0:
                        success = True
                elif service == 10:
                    success = cpm.delete_player_friends()
                elif service == 11:
                    success = cpm.unlock_all_lamborghinis()
                elif service == 12:
                    success = cpm.unlock_all_cars()
                elif service == 13:
                    success = cpm.unlock_all_cars_siren()
                elif service == 14:
                    success = cpm.unlock_w16()
                elif service == 15:
                    success = cpm.unlock_horns()
                elif service == 16:
                    success = cpm.disable_engine_damage()
                elif service == 17:
                    success = cpm.unlimited_fuel()
                elif service == 18:
                    success = cpm.unlock_houses()
                elif service == 19:
                    success = cpm.unlock_smoke()
                elif service == 20:
                    success = cpm.unlock_wheels()
                elif service == 21:
                    success = cpm.unlock_animations()
                elif service == 22:
                    success = cpm.unlock_equipments_male()
                elif service == 23:
                    success = cpm.unlock_equipments_female()
                elif service == 24:
                    amount = IntPrompt.ask("[?] Wins")
                    success = cpm.set_player_wins(amount)
                elif service == 25:
                    amount = IntPrompt.ask("[?] Loses")
                    success = cpm.set_player_loses(amount)
                elif service == 26:
                    e = Prompt.ask("[?] Target Email")
                    p = Prompt.ask("[?] Target Password")
                    success = cpm.account_clone(e, p)
                elif service == 27:
                    cid = IntPrompt.ask("[?] Car ID")
                    hp = IntPrompt.ask("[?] HP")
                    ihp = IntPrompt.ask("[?] Inner HP")
                    nm = IntPrompt.ask("[?] NM")
                    tq = IntPrompt.ask("[?] Torque")
                    success = cpm.hack_car_speed(cid, hp, ihp, nm, tq)
                elif service == 28:
                    cid = IntPrompt.ask("[?] Car ID")
                    angle = IntPrompt.ask("[?] Angle")
                    success = cpm.max_max1(cid, angle)
                elif service == 29:
                    cid = IntPrompt.ask("[?] Car ID")
                    perc = IntPrompt.ask("[?] Percentage")
                    success = cpm.max_max2(cid, perc)
                elif service == 30:
                    cid = IntPrompt.ask("[?] Car ID")
                    mil = IntPrompt.ask("[?] Mileage")
                    success = cpm.millage_car(cid, mil)
                elif service == 31:
                    cid = IntPrompt.ask("[?] Car ID")
                    brk = IntPrompt.ask("[?] Brake")
                    success = cpm.brake_car(cid, brk)
                elif service == 32:
                    cid = IntPrompt.ask("[?] Car ID")
                    success = cpm.rear_bumper(cid)
                elif service == 33:
                    cid = IntPrompt.ask("[?] Car ID")
                    success = cpm.front_bumper(cid)
                elif service == 34:
                    new_pass = Prompt.ask("[?] New Password")
                    success = cpm.change_password(new_pass)
                elif service == 35:
                    new_email = Prompt.ask("[?] New Email")
                    success = cpm.change_email(new_email)
                elif service == 36:
                    cid = IntPrompt.ask("[?] Car ID")
                    spo = IntPrompt.ask("[?] Spoiler ID")
                    success = cpm.telmunnongodz(cid, spo)
                elif service == 37:
                    cid = IntPrompt.ask("[?] Car ID")
                    bk = IntPrompt.ask("[?] BodyKit ID")
                    success = cpm.telmunnongonz(cid, bk)
                elif service == 38:
                    success = cpm.shittin()
                elif service == 39:
                    success = cpm.unlock_crown()
                elif service == 40:
                    success = cpm.unlock_hat_m()
                elif service == 41:
                    success = cpm.rmhm()
                elif service == 42:
                    success = cpm.rmhfm()
                elif service == 43:
                    success = cpm.unlock_topm()
                elif service == 44:
                    success = cpm.unlock_topmz()
                elif service == 45:
                    success = cpm.unlock_topm()  # 3. top için aynı
                elif service == 46:
                    success = cpm.unlock_topf()
                elif service == 47:
                    success = cpm.unlock_topfz()
                elif service == 48:
                    success = cpm.unlock_cls()
                elif service == 49:
                    success = cpm.modificar_todos_los_autos if hasattr(cpm, 'modificar_todos_los_autos') else False
                elif service == 50:
                    success = cpm.unlock_paid_cars()
                elif service == 51:
                    cid = IntPrompt.ask("[?] Car ID")
                    val = IntPrompt.ask("[?] Value")
                    success = cpm.incline(cid, val)
                elif service == 52:
                    src = IntPrompt.ask("[?] Source Car ID")
                    tgt = IntPrompt.ask("[?] Target Car ID")
                    success = cpm.copy_livery(src, tgt)

                if success:
                    console.print("[bold green]SUCCESSFUL ✓[/bold green]")
                else:
                    console.print("[bold red]FAILED ✘[/bold red]")

            except AttributeError:
                console.print("[bold red]Fonksiyon modülde yok.[/bold red]")
            except Exception as e:
                console.print(f"[bold red]Hata: {e}[/bold red]")

            input("\nDevam için Enter tuşuna bas...")
