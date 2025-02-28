import feedparser
import asyncio
from telegram import Bot
import schedule
import time
import sys
from googletrans import Translator

def send_news():
    for entry in feed.entries[:5]:
        print("Найденные новости:", entry.title)

translator = Translator()

schedule.every(10).minutes.do(send_news)


while True:
    sys.stdout.write("\rЖду новости...")
    sys.stdout.flush()
    schedule.run_pending()
    time.sleep(1) 

# Токен и ID чата
TOKEN = "7738677308:AAFRGuARwQq8DCs7AksRw8UB3jPHp-39xE0"
CHAT_ID = 6754357775  # Правильный chat_id

# RSS-лента New York Times
RSS_URL = "http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"

# Создание бота
bot = Bot(token=TOKEN)

async def send_news():
    while True:
        try:
            # Парсим RSS
            feed = feedparser.parse(RSS_URL)
            if not feed.entries:
                print("Нет свежих новостей")
            else:
                # Берём 5 последних новостей
                news_list = [entry.title for entry in feed.entries[:5]]
                message = "\n".join(news_list)

                # Отправляем сообщение
                await bot.send_message(chat_id=CHAT_ID, text=message)
                print("Новости отправлены")

        except Exception as e:
            print(f"Ошибка: {e}")

        # Ждём 1 час
        await asyncio.sleep(3600)

# Запуск асинхронного цикла
asyncio.run(send_news())