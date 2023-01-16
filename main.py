import telebot
bot = telebot.TeleBot("5730532015:AAFuIck1d2VcGFBCMXehSGo_yLBhjzm2ZKA")
user_identifier = [0]
@bot.message_handler(commands=['start'])
def start_bot(message):
    count = 0
    bot.send_message(message.chat.id, "<b>Hello member of destruction</b>", parse_mode="html")
    for i in range(0, len(user_identifier)):
        if message.chat.id != user_identifier[i]:
            count = count + 1
    if count == len(user_identifier):
        for i in range(0, len(user_identifier)):
            if user_identifier[i] == 0:
                user_identifier.append(0)
                user_identifier[i] = message.chat.id
                print(user_identifier[i])
                break
@bot.message_handler()
def transform_message(message):
    for i in range(0, len(user_identifier)-1):
        if message.chat.id == user_identifier[i]:
            continue
        else:
            bot.send_message(user_identifier[i], message.text, parse_mode="html")

bot.infinity_polling()