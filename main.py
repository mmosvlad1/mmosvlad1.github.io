import telebot
bot = telebot.TeleBot("5985822950:AAH3rRW52PCmfg6ifnHKJTtQdyHXNSvYj4E")
vlad_id = 541694991

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, "<b>Hello member of destruction</b>",parse_mode="html")
@bot.message_handler()
def start_bot(message):
    if message.chat.id == vlad_id:
        bot.send_message(vlad_id, message.text,parse_mode="html")
bot.infinity_polling()