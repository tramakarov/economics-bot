import telebot
YES_INLINE = telebot.types.InlineKeyboardMarkup()
YES_BUTTON = telebot.types.InlineKeyboardButton(text="Да", callback_data='YES')
YES_INLINE.row(YES_BUTTON)

MAIN_MENU = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
MAIN_MENU.row("🛒", "🍷", "🚍", "🧾", "💰")
MAIN_MENU.row("Настройки")

HIDE = telebot.types.ReplyKeyboardRemove(selective=False)