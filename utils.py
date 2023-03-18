from telegram import *
from telegram.ext import  ContextTypes,ConversationHandler
import sqlalchemy as db
from db import members,connection,engine
from pathlib import Path
from os import remove

GENDER, NAME, AGE, FACULTY,NETWORKING,FRIENDSHIP, RELATIONSHIP, HELP, CHATTING , PHOTO, BIO = range(11)

DELETE_FORM= range(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать в бота для Нетворкинга и знакомств ConnectBot!\n Чтобы создать анкету, напиши /create_form \nЧтобы посмотреть все доступные команды, напиши /help")

async def create_form(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.username
    user_gender=""
    user_age=0
    user_name=""
    user_faculty=""
    user_networking=False
    user_friendship=False
    user_relationship=False
    user_help=False
    user_chatting=False
    user_photo = ""
    out_of_stock= db.select(db.func.count()).select_from(members).where(members.columns.tg_chat_id == update.effective_chat.id)
    count =connection.execute(out_of_stock)
    count=int(count.fetchall()[0][0])

    if count==0:
        insertion_query = members.insert().values([
            {"tg_id":user_id,
            "gender":user_gender,
            "age":user_age,
            "name":user_name,
            "tg_chat_id":update.effective_chat.id,
            "faculty":user_faculty,
            "networking":user_networking,
            "friendship":user_friendship,
            "relationship":user_relationship,
            "help":user_help,
            "chatting":user_chatting,
            "photo":user_photo}

            ])
        connection.execute(insertion_query)
    else:
        pass
        
    
    connection.commit()
    reply_keyboard = [["Парень", "Девушка", "Другое"]]
    await update.message.reply_text("Какой ваш пол?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return GENDER

async def set_gender(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_gender = update.message.text
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(gender = user_gender)
    connection.execute(update_query)
    connection.commit()
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Как вас зовут?")
    return NAME

async def set_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.text
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(name = user_name)
    connection.execute(update_query)
    connection.commit()
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Сколько вам лет?")
    return AGE

async def set_age(update: Update, context: ContextTypes.DEFAULT_TYPE):    
    user_age = int(update.message.text)
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(age = user_age)
    connection.execute(update_query)
    connection.commit()
    await context.bot.send_message(chat_id=update.effective_chat.id,text="На каком факультете вы учитесь?")
    return FACULTY

async def set_faculty(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_faculty = update.message.text
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(faculty = user_faculty)
    connection.execute(update_query)
    connection.commit()

    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Интересует ли вас нетворкинг?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return NETWORKING

async def set_networking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_networking = True
    else:
        user_networking = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(networking = user_networking)
    connection.execute(update_query)
    connection.commit()

    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Ищите ли вы дружбу?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return FRIENDSHIP

async def set_friendship(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_friendship = True
    else:
        user_friendship = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(friendship = user_friendship)
    connection.execute(update_query)
    connection.commit()

    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Интересует ли вас отношения?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )
    
    return RELATIONSHIP

async def set_relationship(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_relationship = True
    else:
        user_relationship = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(relationship = user_relationship)
    connection.execute(update_query)
    connection.commit()

    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Нужна ли вам помощь?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return HELP

async def set_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_help = True
    else:
        user_help = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(help = user_help)
    connection.execute(update_query)
    connection.commit()

    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Хотите ли вы с кем-нибудь побеседовать?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return CHATTING

async def set_chatting(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_chatting = True
    else:
        user_chatting = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_user.id).values(chatting = user_chatting)
    connection.execute(update_query)
    connection.commit()

    await context.bot.send_message(chat_id=update.effective_chat.id,text="Пришлите ваше фото",reply_markup=ReplyKeyboardRemove())
    
    return PHOTO

async def set_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = await update.message.photo[-1].get_file()
    photo_path = Path("photo",f'{update.effective_chat.id}.jpg')
    await photo_file.download_to_drive(photo_path)
    user_photo = f'{update.effective_chat.id}.jpg'
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_user.id).values(photo = user_photo)
    connection.execute(update_query)
    connection.commit()

    await context.bot.send_message(chat_id=update.effective_chat.id,text="Расскажи что-нибудь о себе:)")

    return BIO

async def set_bio(update: Update, context: ContextTypes.DEFAULT_TYPE):    
    user_bio = update.message.text
    engine.connect()
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_user.id).values(bio = user_bio)
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Твоя анкета готова!")
    connection.execute(update_query)
    select_query= db.select(members).where(members.columns.tg_chat_id ==update.effective_chat.id)
    select_result= connection.execute(select_query).fetchall()
    print(select_result)

    return ConversationHandler.END  

async def delete_form(update: Update, context:ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Вы точно хотите удалить анкету?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )
    return DELETE_FORM   
    
async def delete_form_end(update: Update, context:ContextTypes.DEFAULT_TYPE):
    delete_query= db.delete(members).where(members.columns.tg_chat_id == update.effective_chat.id)
    connection.execute(delete_query)
    connection.commit()
    remove(Path("photo",f'{update.effective_chat.id}.jpg'))
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Твоя анкета удалена")
    return ConversationHandler.END

async def show_form(update: Update, context:ContextTypes.DEFAULT_TYPE):
    select_query= db.select( members.columns.name ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result=connection.execute(select_query)
    connection.commit()
    name_result=str(select_result.fetchall()[0][0])

    select_query= db.select( members.columns.age ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result=connection.execute(select_query)
    connection.commit()
    age_result=str(select_result.fetchall()[0][0])

    select_query= db.select( members.columns.faculty ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result=connection.execute(select_query)
    connection.commit()
    faculty_result=str(select_result.fetchall()[0][0])

    select_query= db.select( members.columns.bio ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result=connection.execute(select_query)
    connection.commit()
    bio_result=str(select_result.fetchall()[0][0])

    select_query= db.select( members.columns.photo ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result=connection.execute(select_query)
    connection.commit()
    photo_path=(select_result.fetchall()[0][0])
    photo_path = Path("photo",photo_path) 

    select_query= db.select( members.columns.networking ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result=connection.execute(select_query)
    connection.commit()
    if select_result.fetchall()[0][0]==True:
        networking_result="Нетворкинг"
    else:
        networking_result=""

    select_query= db.select( members.columns.friendship ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result=connection.execute(select_query)
    connection.commit()
    if select_result.fetchall()[0][0]==True:
        friendship_result="Дружба"
    else:
        friendship_result=""

    select_query= db.select( members.columns.relationship ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result=connection.execute(select_query)
    connection.commit()
    if select_result.fetchall()[0][0]==True:
        relationship_result="Отношения"
    else:
        relationship_result=""

    select_query= db.select( members.columns.help ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result=connection.execute(select_query)
    connection.commit()
    if select_result.fetchall()[0][0]==True:
        help_result="Помощь"
    else:
        help_result=""

        select_query= db.select( members.columns.chatting ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result=connection.execute(select_query)
    connection.commit()
    if select_result.fetchall()[0][0]==True:
        chatting_result="Общение"
    else:
        chatting_result=""

    form=f'Твоя анкета: \n{networking_result} {friendship_result} {relationship_result} {help_result} {chatting_result}\n{name_result},{age_result},{faculty_result}\n {bio_result}'
    
    if name_result=="":
        await context.bot.send_message(chat_id=update.effective_chat.id,text=form)
    else:
        await context.bot.send_photo(chat_id=update.effective_chat.id,photo=photo_path,caption=form)
        

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Хорошо!", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text="Все команды установленные в боте:\n Создание анкеты /create_form \n Удаление анкеты /delete_form \n Показать свою анкету /show_form \n Поиск анкеты /search_form \n Отмена любой команды /cancel \n Обновление возраста /update_age \n Обновление имени /update_name \n Обновление фотографии /update_photo \n Обновление факультета /update_faculty \n Обновление статуса поиска нетворкинга /update_networking \n Обновление статуса поиска общения  /update_chatting \n Обновление статуса поиска дружбы /update_friendship \n Обновление статуса поиска отношений /update_relationship \n Обновление статуса поиска помощи /update_help \n Обновление описания профиля /update_bio"
    await context.bot.send_message(chat_id=update.effective_chat.id,text=help_text)
