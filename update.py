from telegram import *
from telegram.ext import  ContextTypes,ConversationHandler
import sqlalchemy as db
from db import members,connection,engine
from pathlib import Path

UPDATE,SHOW_FORM =range(2) #создание переменных которые помогут для диалоговых окон в боте

async def update_gender(update: Update,context: ContextTypes.DEFAULT_TYPE): #метод запускающий диалог обновления значения пола в анкете
    reply_keyboard = [["Парень", "Девушка", "Другое"]]
    await update.message.reply_text("Какой ваш пол?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return UPDATE  #переход к следующему методу по плану диалогового окна

async def set_update_gender(update: Update, context: ContextTypes.DEFAULT_TYPE): #продолжение вышестоящего метода в виде следующего окна диалога
    user_gender = update.message.text #копирование сообщения пользователя
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(gender = user_gender) #создание запроса внесения обновленных данных в таблицу
    connection.execute(update_query) #выполнение запроса
    connection.commit() #подтверждение изменений в таблице
    
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM #переход к следующему методу по плану диалогового окна

async def update_age(update: Update,context: ContextTypes.DEFAULT_TYPE): #метод запускающий диалог обновления значения возраста в анкете
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Сколько вам лет?")

    return UPDATE #переход к следующему методу

async def set_update_age(update: Update, context: ContextTypes.DEFAULT_TYPE): #продолжение вышестоящего метода в виде следующего окна диалога
    user_age = int(update.message.text) #копирование сообщения пользователя
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(age = user_age) #создание запроса внесения обновленных данных в таблицу
    connection.execute(update_query) #выполнение запроса
    connection.commit() #подтверждение изменений в таблице
    
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM #переход к следующему методу по плану диалогового окна

async def update_name(update: Update,context: ContextTypes.DEFAULT_TYPE): #метод запускающий диалог обновления имени в анкете
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Как вас зовут?")

    return UPDATE #переход к следующему методу по плану диалогового окна

async def set_update_name(update: Update, context: ContextTypes.DEFAULT_TYPE): #продолжение вышестоящего метода в виде следующего окна диалога
    user_name = update.message.text #копирование сообщения пользователя
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(name = user_name) #создание запроса внесения обновленных данных в таблицу
    connection.execute(update_query) #выполнение запроса
    connection.commit() #подтверждение изменений в таблице
    
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM #переход к следующему методу по плану диалогового окна

async def update_faculty(update: Update,context: ContextTypes.DEFAULT_TYPE): #метод запускающий диалог обновления данных анкеты о факультете
    await context.bot.send_message(chat_id=update.effective_chat.id,text="На каком факультете вы учитесь?")

    return UPDATE #переход к следующему методу по плану диалогового окна

async def set_update_faculty(update: Update, context: ContextTypes.DEFAULT_TYPE): #продолжение вышестоящего метода в виде следующего окна диалога
    user_faculty = update.message.text #копирование сообщения пользователя
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(faculty = user_faculty) #создание запроса внесения обновленных данных в таблицу
    connection.execute(update_query) #выполнение запроса
    connection.commit() #подтверждение изменений в таблице
    
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM #переход к следующему методу по плану диалогового окна

async def update_networking(update: Update,context: ContextTypes.DEFAULT_TYPE): #метод запускающий диалог обновления значения тега "нетворкинг"
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Интересует ли вас нетворкинг?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return UPDATE #переход к следующему методу по плану диалогового окна

async def set_update_networking(update: Update, context: ContextTypes.DEFAULT_TYPE): #продолжение вышестоящего метода в виде следующего окна диалога
    if update.message.text=="ДА": #проверка выбранной кнопки 
        user_networking = True
    else:
        user_networking = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(networking = user_networking) #создание запроса внесения обновленных данных в таблицу
    connection.execute(update_query) #выполнение запроса
    connection.commit() #подтверждение изменений в таблице

    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM #переход к следующему методу по плану диалогового окна

async def update_friendship(update: Update,context: ContextTypes.DEFAULT_TYPE): #метод запускающий диалог обновления значения тега "дружба"
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Ищите ли вы дружбу?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return UPDATE #переход к следующему методу по плану диалогового окна

async def set_update_friendship(update: Update, context: ContextTypes.DEFAULT_TYPE): #продолжение вышестоящего метода в виде следующего окна диалога
    if update.message.text=="ДА":    
        user_friendship = True
    else:
        user_friendship = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(friendship = user_friendship) #создание запроса внесения обновленных данных в таблицу
    connection.execute(update_query) #выполнение запроса
    connection.commit() #подтверждение изменений в таблице
    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM #переход к следующему методу по плану диалогового окна

async def update_relationship(update: Update,context: ContextTypes.DEFAULT_TYPE): #метод запускающий диалог обновления значения тега "отношения"
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Интересует ли вас отношения?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return UPDATE #переход к следующему методу по плану диалогового окна

async def set_update_relationship(update: Update, context: ContextTypes.DEFAULT_TYPE): #продолжение вышестоящего метода в виде следующего окна диалога
    if update.message.text=="ДА":    
        user_relationship = True
    else:
        user_relationship = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(relationship = user_relationship) #создание запроса внесения обновленных данных в таблицу
    connection.execute(update_query) #выполнение запроса
    connection.commit() #подтверждение изменений в таблице
    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM #переход к следующему методу по плану диалогового окна

async def update_help(update: Update,context: ContextTypes.DEFAULT_TYPE): #метод запускающий диалог обновления значения тега "помощь"
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Нужна ли вам помощь?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return UPDATE #переход к следующему методу по плану диалогового окна

async def set_update_help(update: Update, context: ContextTypes.DEFAULT_TYPE): #продолжение вышестоящего метода в виде следующего окна диалога
    if update.message.text=="ДА":    
        user_help = True
    else:
        user_help = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(help = user_help) #создание запроса внесения обновленных данных в таблицу
    connection.execute(update_query) #выполнение запроса
    connection.commit() #подтверждение изменений в таблице

    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM #переход к следующему методу по плану диалогового окна

async def update_chatting(update: Update,context: ContextTypes.DEFAULT_TYPE): #метод запускающий диалог обновления значения тега "общение"
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Хотите ли вы с кем-нибудь побеседовать?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return UPDATE #переход к следующему методу по плану диалогового окна
    
async def set_update_chatting(update: Update, context: ContextTypes.DEFAULT_TYPE): #продолжение вышестоящего метода в виде следующего окна диалога
    if update.message.text=="ДА":    
        user_chatting = True
    else:
        user_chatting = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(networking = user_chatting) #создание запроса внесения обновленных данных в таблицу
    connection.execute(update_query) #выполнение запроса
    connection.commit() #подтверждение изменений в таблице

    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM #переход к следующему методу по плану диалогового окна

async def update_photo(update:Update,context:ContextTypes.DEFAULT_TYPE): #метод запускающий диалог обновления фотографии анкеты
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Пришлите ваше фото")

    return UPDATE

async def set_update_photo(update: Update, context: ContextTypes.DEFAULT_TYPE): #продолжение вышестоящего метода в виде следующего окна диалога
    photo_file = await update.message.photo[-1].get_file()
    photo_path = Path("photo",f'{update.effective_chat.id}.jpg')
    await photo_file.download_to_drive(photo_path)
    user_photo = f'{update.effective_chat.id}.jpg'
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_user.id).values(photo = user_photo) #создание запроса внесения обновленных данных в таблицу
    connection.execute(update_query) #выполнение запроса
    connection.commit() #подтверждение изменений в таблице

    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM #переход к следующему методу по плану диалогового окна

async def update_bio(update: Update,context: ContextTypes.DEFAULT_TYPE): #метод запускающий диалог обновления данных "о себе"
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Расскажи что-нибудь о себе:)")
    return UPDATE #переход к следующему методу по плану диалогового окна
    
async def set_update_bio(update:Update, context:ContextTypes.DEFAULT_TYPE): #продолжение вышестоящего метода в виде следующего окна диалога
    user_bio = update.message.text #копирование сообщения пользователя
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(bio = user_bio) #создание запроса внесения обновленных данных в таблицу
    connection.execute(update_query) #выполнение запроса
    connection.commit() #подтверждение изменений в таблице
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM #переход к следующему методу по плану диалогового окна

async def show_update_form(update: Update, context:ContextTypes.DEFAULT_TYPE): #метод показывающий обновленную анкету
    if update.message.text=="НЕТ":    
        pass
    else:
        select_query= db.select( members.columns.name ).where(members.columns.tg_chat_id == update.effective_chat.id) #создание запроса поиска данных выбранной анкеты
        select_result=connection.execute(select_query) #выполнение запроса
        name_result=str(select_result.fetchall()[0][0])

        select_query= db.select( members.columns.age ).where(members.columns.tg_chat_id == update.effective_chat.id) #создание запроса поиска данных выбранной анкеты
        select_result=connection.execute(select_query) #выполнение запроса
        age_result=str(select_result.fetchall()[0][0])

        select_query= db.select( members.columns.faculty ).where(members.columns.tg_chat_id == update.effective_chat.id) #создание запроса поиска данных выбранной анкеты
        select_result=connection.execute(select_query) #выполнение запроса
        faculty_result=str(select_result.fetchall()[0][0])

        select_query= db.select( members.columns.bio ).where(members.columns.tg_chat_id == update.effective_chat.id) #создание запроса поиска данных выбранной анкеты
        select_result=connection.execute(select_query) #выполнение запроса
        bio_result=str(select_result.fetchall()[0][0])

        select_query= db.select( members.columns.photo ).where(members.columns.tg_chat_id == update.effective_chat.id) #создание запроса поиска данных выбранной анкеты
        select_result=connection.execute(select_query) #выполнение запроса
        photo_path=(select_result.fetchall()[0][0])
        photo_path = Path("photo",photo_path) 

        select_query= db.select( members.columns.networking ).where(members.columns.tg_chat_id == update.effective_chat.id) #создание запроса поиска данных выбранной анкеты
        select_result=connection.execute(select_query) #выполнение запроса
        if select_result.fetchall()[0][0]==True:
            networking_result="Нетворкинг"
        else:
            networking_result=""

        select_query= db.select( members.columns.friendship ).where(members.columns.tg_chat_id == update.effective_chat.id) #создание запроса поиска данных выбранной анкеты
        select_result=connection.execute(select_query) #выполнение запроса
        if select_result.fetchall()[0][0]==True:
            friendship_result="Дружба"
        else:
            friendship_result=""

        select_query= db.select( members.columns.relationship ).where(members.columns.tg_chat_id == update.effective_chat.id) #создание запроса поиска данных выбранной анкеты
        select_result=connection.execute(select_query) #выполнение запроса
        if select_result.fetchall()[0][0]==True:
            relationship_result="Отношения"
        else:
            relationship_result=""

        select_query= db.select( members.columns.help ).where(members.columns.tg_chat_id == update.effective_chat.id) #создание запроса поиска данных выбранной анкеты
        select_result=connection.execute(select_query) #выполнение запроса
        if select_result.fetchall()[0][0]==True:
            help_result="Помощь"
        else:
            help_result=""

        select_query= db.select( members.columns.chatting ).where(members.columns.tg_chat_id == update.effective_chat.id) #создание запроса поиска данных выбранной анкеты
        select_result=connection.execute(select_query) #выполнение запроса
        if select_result.fetchall()[0][0]==True:
            chatting_result="Общение"
        else:
            chatting_result=""

        form=f'Твоя анкета: \n{networking_result} {friendship_result} {relationship_result} {help_result} {chatting_result}\n{name_result},{age_result},{faculty_result}\n {bio_result}'
        
        if name_result=="":
            await context.bot.send_message(chat_id=update.effective_chat.id,text=form) #вывод для пустой анкеты
        else:
            await context.bot.send_photo(chat_id=update.effective_chat.id,photo=photo_path,caption=form) #вывод для нормальной анкеты

    
    return ConversationHandler.END #завершение диалога
