import requests
from bs4 import BeautifulSoup
from telegram import *
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler 
import pytube



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def find_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://yandex.ru/images/search?source=collections&rpt=imageview&url=urltofile&"+update.message.photo
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    similar = soup.find_all('li', class_='cbir-similar__thumb')
    set_of_photo=[]
    j=0
    for i in similar:
        set_of_photo.append(f"https://yandex.ru{i.find('a').get('href')}")
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=set_of_photo[j])
        j+=1


async def weekly_plan(update:Update, context: ContextTypes.DEFAULT_TYPE):
    pass

async def daily_plan(update:Update, context: ContextTypes.DEFAULT_TYPE):
    pass

async def download_video(update:Update, context: ContextTypes.DEFAULT_TYPE):
    link = pytube.YouTube(update.message.text)
    videos = link.streams.first().download()
    await context.bot.send_video(chat_id=update.effective_chat.id, video=videos)


