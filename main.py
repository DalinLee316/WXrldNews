import feedparser
from telegram import Bot
import schedule
import time
import asyncio

# Токен и ID чата
TOKEN = "7738677308:AAFRGuARwQq8DCs7AksRw8UB3jPHp-39xE0"
CHAT_ID = 6754357775  

# RSS-лента New York Times
RSS_URLS = [
    "http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "https://cointelegraph.com/rss",
    "https://decrypt.co/feed"
]

# Создание бота
bot = Bot(token=TOKEN)

# Функция для отправки новостей
async def send_news():
    print("Функция send news() вызвана")
    try:
        feed = feedparser.parse(RSS_URL)
        if not feed.entries:
            print("Нет свежих новостей")
            return

        news_list = [entry.title for entry in feed.entries[:5]]
        message = "\n".join(news_list)

        await bot.send_message(chat_id=6754357775, text=message)
        print("Новости отправлены")

    except Exception as e:
        print(f"Ошибка: {e}")

def run_asyncio_job():
    asyncio.run(send_news())

# Запускаем `send_news()` каждые 10 минут
schedule.every(10).minutes.do(run_asyncio_job)

# Бесконечный цикл для работы schedule
while True:
    print("\rЖду новости...", end="", flush=True)
    schedule.run_pending()
    time.sleep(1)
