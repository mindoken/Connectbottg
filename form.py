from telegram import *
from telegram.ext import  ContextTypes

async def get_gender(update, context):   
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Какой ваш пол?")
    gender=update.message.text
    return gender

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message("Как вас зовут?")
    name=update.callback_query.message.text
    return name

async def get_age(update: Update, context: ContextTypes.DEFAULT_TYPE):    
    await context.bot.send_message("Сколько вам лет?")
    age=update.callback_query.message.text
    return age

async def get_faculty(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message("На каком факультете вы учитесь?")
    faculty=update.callback_query.message.text
    return faculty

async def get_networking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message("Интересует ли вас нетворкинг?")
    networking=1
    return networking

async def get_friendship(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Bot.send_message("Ищите ли вы дружбу?")
    friendship=ForceReply.selective
    return friendship

async def get_relationship(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Bot.send_message("Ищите ли вы отношения?")
    relationship=ForceReply.selective
    return relationship

async def get_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Bot.send_message("Ищите ли вы помощь?")
    help=ForceReply.selective
    return help

async def get_chatting(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Bot.send_message("Интересует ли вас общение?")
    chatting=ForceReply.selective
    return chatting

async def get_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Bot.send_message("Пришлите ваше фото")
    photo= update.message.photo
    return photo