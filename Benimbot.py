import os
import telebot

TOKEN = os.getenv('BOT_TOKEN')  # Tokenı çevresel değişkenden alıyoruz
ADMIN_ID = 6934555622

bot = telebot.TeleBot(TOKEN)

welcome_message_template = """
🎉 WELCOME TO Pakundo Tools👑 🇵🇭
🔥 THE REVOLUTION IN CHEATS HAS BEGUN
AND YOU ARE NOW PART OF IT 🥀
🔐 YOUR ACCOUNT DETAILS👇
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
🆔 TG ID: {user_id}
🔑 Access Key: 
💎 Balance: 1,000

⚠️ Security Alert
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
🚫 Never share your Access Key with anyone!
🔒 Our team will never ask for your credentials

⚙️ Explore all available features.
📩 Need help? Contact our support!
🚀 Enjoy your experience! @aydnqx 🇵🇭🔥
"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, welcome_message_template.format(user_id=user_id))

@bot.message_handler(commands=['menu'])
def menu(message):
    if message.from_user.id == ADMIN_ID:
        bot.send_message(message.chat.id, "📋 Menü:\n1. Komut 1\n2. Komut 2")
    else:
        bot.send_message(message.chat.id, "🚫 Yetkin yok.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Yardım menüsü:\n/menu - Menü göster\n/help - Yardım")

print("✅ Bot çalışıyor...")
bot.polling()
