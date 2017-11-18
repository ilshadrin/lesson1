# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start. Эгегей, я жив!!!!!!'
    #print(1/0)
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    logging.info(user_text)
    update.message.reply_text(user_text)


def main():
    updater = Updater("478411131:AAFn2nvMqaDicbbqE2Xsta_L4cQu1MY-zPM")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()

# Вызываем функцию - эта строчка собственно запускает бота
main()
