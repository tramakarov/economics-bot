import telebot
YES = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
YES.row("Да")

MAIN_MENU = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
MAIN_MENU.row("🛒", "🍷", "🚍", "🧾", "💰")
MAIN_MENU.row("Настройки")

HIDE = telebot.types.ReplyKeyboardRemove(selective=False)