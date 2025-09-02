#!/bin/bash

# ===============================================
# nexoraviptool Bash Menü Versiyonu
# ===============================================

# Renkler
RED="\033[1;31m"
GREEN="\033[1;32m"
YELLOW="\033[1;33m"
CYAN="\033[1;36m"
RESET="\033[0m"

# Banner
banner() {
    clear
    echo -e "${CYAN}==============================${RESET}"
    echo -e "${GREEN}♕ nexoraviptool${RESET}"
    echo -e "${YELLOW}Car Parking Multiplayer 2 Hacking Tool${RESET}"
    echo -e "${CYAN}==============================${RESET}"
}

# Kullanıcı girişi
read_account_data() {
    read -p "Account Email: " acc_email
    read -p "Account Password: " acc_password
    read -p "Access Key: " acc_access_key
}

# Menü gösterimi
menu() {
    echo -e "${CYAN}(01)${RESET} Account Delete ~ FREE"
    echo -e "${CYAN}(02)${RESET} Account Register ~ FREE"
    echo -e "${CYAN}(03)${RESET} Increase Money ~ 4K"
    echo -e "${CYAN}(04)${RESET} Change ID ~ 2.5K"
    echo -e "${CYAN}(05)${RESET} Change Name ~ 1K"
    echo -e "${CYAN}(06)${RESET} Complete Missions ~ 6K"
    echo -e "${CYAN}(07)${RESET} Delete Friends ~ 2K"
    echo -e "${CYAN}(08)${RESET} King Rank ~ 6K"
    echo -e "${CYAN}(09)${RESET} Maximize Drag Wins ~ 6K"
    echo -e "${CYAN}(10)${RESET} Unlock Slots ~ 7K"
    echo -e "${CYAN}(11)${RESET} Unlock Apartments ~ 10K"
    echo -e "${CYAN}(12)${RESET} Unlock Brakes ~ 5K"
    echo -e "${CYAN}(13)${RESET} Unlock Wheels ~ 6K"
    echo -e "${CYAN}(14)${RESET} Unlock Clothes ~ 9K"
    echo -e "${CYAN}(15)${RESET} Unlock Cars ~ 10K"
    echo -e "${CYAN}(0)${RESET} Exit"
}

# Placeholder işlemler
execute_action() {
    case $1 in
        1) echo -e "${GREEN}[ACTION] Deleting Account...${RESET}" ;;
        2) echo -e "${GREEN}[ACTION] Registering new Account...${RESET}" ;;
        3) echo -e "${GREEN}[ACTION] Increasing Money...${RESET}" ;;
        4) echo -e "${GREEN}[ACTION] Changing ID...${RESET}" ;;
        5) echo -e "${GREEN}[ACTION] Changing Name...${RESET}" ;;
        6) echo -e "${GREEN}[ACTION] Completing Missions...${RESET}" ;;
        7) echo -e "${GREEN}[ACTION] Deleting Friends...${RESET}" ;;
        8) echo -e "${GREEN}[ACTION] Upgrading King Rank...${RESET}" ;;
        9) echo -e "${GREEN}[ACTION] Maximizing Drag Wins...${RESET}" ;;
        10) echo -e "${GREEN}[ACTION] Unlocking Slots...${RESET}" ;;
        11) echo -e "${GREEN}[ACTION] Unlocking Apartments...${RESET}" ;;
        12) echo -e "${GREEN}[ACTION] Unlocking Brakes...${RESET}" ;;
        13) echo -e "${GREEN}[ACTION] Unlocking Wheels...${RESET}" ;;
        14) echo -e "${GREEN}[ACTION] Unlocking Clothes...${RESET}" ;;
        15) echo -e "${GREEN}[ACTION] Unlocking Cars...${RESET}" ;;
        0) echo -e "${YELLOW}Exiting... Bye!${RESET}"; exit 0 ;;
        *) echo -e "${RED}Invalid choice!${RESET}" ;;
    esac
}

# Ana döngü
while true; do
    banner
    read_account_data
    while true; do
        banner
        menu
        read -p "Select a Service [0-15]: " service
        execute_action $service
        read -p "Do you want to continue? (y/n): " cont
        if [[ "$cont" != "y" ]]; then
            echo -e "${YELLOW}Exiting... Bye!${RESET}"
            exit 0
        fi
    done
done
