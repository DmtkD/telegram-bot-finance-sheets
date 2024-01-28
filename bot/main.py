from telebot import TeleBot as Bot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton

# Bot
bot: Bot = Bot(token='****')

# KeyBoard
keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button = KeyboardButton(text="Введіть своє ім'я")
keyboard.add(button)


@bot.message_handler(commands=['register'])
def register_in_bot(message):
    bot.send_message(message.chat.id, "Вас вітає реєстраційна форма!", reply_markup=keyboard)


# @bot.message_handler(func=lambda message: True)
# def process_name(message):
#     if message.text == "Введіть своє ім'я":
#         name = message.text
#         bot.send_message(message.chat.id, f"Ви ввели ім'я: {name}")
#     else:
#         bot.send_message(message.chat.id, "Будь ласка, використовуйте кнопки на клавіатурі.")


@bot.message_handler(commands=['register'])
def register_in_bot(Message) -> None:
    pass


def register_sheet(message: Message) -> None:
    pass


def register_notion(message: Message) -> None:
    pass


def write_to_sheet(message: Message) -> None:
    pass


def get_all_from_sheet(message: Message) -> None:
    pass


def write_daily_plan(message: Message) -> None:
    pass


bot.polling(non_stop=True)
