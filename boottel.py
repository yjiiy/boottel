import telebot

# حط توكن البوت هنا بعد ما تفعله
TOKEN = '8067799528:AAF0KOlCHSLfxIXlLlN1Z2lHHyIueEEcMdA'

bot = telebot.TeleBot(TOKEN)

# عند استقبال رسالة من أي شخص
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # الرد على الرسالة
    bot.reply_to(message, f"أنت قلت: {message.text}")

# هذا بيسمح للبوت إنه يشتغل بدون توقف
bot.infinity_polling()