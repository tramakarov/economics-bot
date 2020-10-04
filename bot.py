import telebot
import db
import texts
import credentials

bot = telebot.TeleBot(credentials.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    print('start!')
    user = db.get_user_info(message.chat.id)
    if user is None:
        bot.send_message(text=texts.GREETING,
                         parse_mode='Markdown',
                         chat_id=message.chat.id)


if __name__ == '__main__':
    bot.remove_webhook()
    bot.polling(none_stop=True)
