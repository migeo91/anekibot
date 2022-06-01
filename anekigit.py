import requests
import random
import telebot
from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/tags/%D0%9E%D0%B4%D0%B5%D1%81%D1%81%D0%B0' ## ссылка на анекдоты для парсинга
API_KEY = '' ## токен

def parser(url):

    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    aneki = soup.find_all('div', class_='text')
    return [c.text for c in aneki]

list_aneki = parser(URL)
random.shuffle(list_aneki)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id, 'Отправьте любую цифру:')

@bot.message_handler(content_types=['text'])

def rzhaka(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_aneki[0])
        del list_aneki[0]
    else:
        bot.send_message(message.chat.id, 'Цифру!')
    
bot.polling()
