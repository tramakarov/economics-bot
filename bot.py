import telebot
import db
from texts import texts
import credentials
import datetime
from user import User
from status import Status
import keyboards

bot = telebot.TeleBot(credentials.BOT_TOKEN)
GET_statuses = [Status.GET_PERIOD.value,
                Status.GET_BALANCE_FOOD.value,
                Status.GET_BALANCE_ALCO.value,
                Status.GET_BALANCE_TRANSPORT.value,
                Status.GET_BALANCE_GENERAL.value,
                Status.GET_BALANCE_FINPILLOW.value]


@bot.message_handler(commands=['start'])
def start(message):
    user = db.get_user(message.chat.id)
    if user.status == Status.HELLO.value:
        bot.send_message(text=texts['GREETING'],
                         parse_mode='Markdown',
                         chat_id=message.chat.id,
                         reply_markup=keyboards.YES_INLINE)


@bot.message_handler(content_types=['text'])
def parse_message(message):
    user = db.get_user(message.chat.id)
    if user.status in GET_statuses:
        run_get_status(user, message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        user = db.get_user(call.message.chat.id)
        if call.data == "YES":
            user.status = Status.GET_PERIOD.value
            db.update_user(user)
            bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id)
            bot.send_message(text=texts['GET_PERIOD'],
                             parse_mode='Markdown',
                             chat_id=call.message.chat.id,
                             reply_markup=keyboards.HIDE)


def run_get_status(user, message):
    try:
        if user.status == Status.GET_PERIOD.value:
            period_length = int(message.text)
            user.period_end = datetime.datetime.now() + datetime.timedelta(days=period_length)

        elif user.status == Status.GET_BALANCE_FOOD.value:
            user.food = int(message.text)

        elif user.status == Status.GET_BALANCE_ALCO.value:
            user.alco = int(message.text)

        elif user.status == Status.GET_BALANCE_TRANSPORT.value:
            user.transport = int(message.text)

        elif user.status == Status.GET_BALANCE_GENERAL.value:
            user.general = int(message.text)

        elif user.status == Status.GET_BALANCE_FINPILLOW.value:
            user.pillow = int(message.text)

        user.status = Status.get_next_balance(user.status)
        db.update_user(user)
        if user.status == Status.MAIN_MENU.value:
            bot.send_message(text=texts['SUCCESSFUL_REG'],
                             parse_mode='Markdown',
                             chat_id=message.chat.id,
                             reply_markup=keyboards.MAIN_MENU)
        else:
            bot.send_message(text=texts[user.status],
                             parse_mode='Markdown',
                             chat_id=message.chat.id,
                             reply_markup=keyboards.HIDE)
    except ValueError:
        bot.send_message(text=texts.NOT_A_NUMBER,
                         parse_mode='Markdown',
                         chat_id=message.chat.id)


if __name__ == '__main__':
    bot.remove_webhook()
    bot.polling(none_stop=True)
