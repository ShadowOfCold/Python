import requests
from bs4 import BeautifulSoup
import Database as Database
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import sqlite3
import Config

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.731 YaBrowser/23.11.1.731 Yowser/2.5 Safari/537.36' }

URL = "https://mangalib.me/"
page = requests.get(url = URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
comics = soup.find_all("div", class_="updates__item")

Database.create_table()

for comic in comics:

    comics_type = comic.find("div", class_="updates__type").text.strip()
    comics_title = comic.find("a", class_="link-default").text.strip()
    comics_chapter = comic.find("strong", class_="updates__chapter-vol").text.strip()
    comics_link = comic.find("a", class_="link-default", href=True)["href"].strip()
    
    try:
        if Database.check_comics(comics_title) == False:
            Database.insert_comics(comics_type, comics_title, comics_chapter, comics_link)
        else:
            Database.update_comics(comics_title, comics_chapter)
    except Exception as ex:
        continue

db = sqlite3.connect('MangaLib.db')
cursor = db.cursor()

bot = Bot(token=Config.API_TOKEN)
dp = Dispatcher()

@dp.message(Command('show_table'))
async def show_table(message: types.Message):
    cursor.execute('SELECT * FROM comics')
    data = cursor.fetchall()

    response = ""
    for row in data:
        response += " | ".join(str(cell) for cell in row) + "\n"
    if len(response) > 4096:
        for x in range(0, len(response), 4096):
            await message.answer(response[x:x+4096])
    else:
        await message.answer(response)
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())