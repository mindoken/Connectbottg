from telegram import *
from telegram.ext import  ContextTypes,ConversationHandler
import sqlalchemy as db
from db import members,connection
import string



GENDER, NAME, AGE, FACULTY,NETWORKING,FRIENDSHIP, RELATIONSHIP, HELP, CHATTING ,PHOTO, BIO = range(11)
UPDATE,SHOW_FORM =range(2)
"""UPDATE_GENDER,SHOW_FORM =range(2) 
UPDATE_AGE,SHOW_FORM =range(2) 
UPDATE_NAME,SHOW_FORM =range(2)
UPDATE_FACULTY,SHOW_FORM =range(2)
UPDATE_NETWORKING,SHOW_FORM =range(2)
UPDATE_FRIENDSHIP,SHOW_FORM =range(2)
UPDATE_RELATIONSHIP,SHOW_FORM =range(2)
UPDATE_HELP,SHOW_FORM =range(2)
UPDATE_CHATTING,SHOW_FORM =range(2)
UPDATE_BIO,SHOW_FORM =range(2)"""
DELETE_FORM= range(1)

def convert_to_binary_data(filename):# Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать в бота для Нетворкинга и знакомств Spring! Чтобы создать анкету напиши /create_form")

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
    user_photo = convert_to_binary_data("user_photo.jpg")
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
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Как вас зовут?")
    return NAME

async def set_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.text
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(name = user_name)
    connection.execute(update_query)
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Сколько вам лет?")
    return AGE

async def set_age(update: Update, context: ContextTypes.DEFAULT_TYPE):    
    user_age = int(update.message.text)
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(age = user_age)
    connection.execute(update_query)

    await context.bot.send_message(chat_id=update.effective_chat.id,text="На каком факультете вы учитесь?")
    return FACULTY

async def set_faculty(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_faculty = update.message.text
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(faculty = user_faculty)
    connection.execute(update_query)

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

    await context.bot.send_message(chat_id=update.effective_chat.id,text="Пришлите ваше фото")
    
    return PHOTO

async def set_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = await update.message.photo[-1].get_file()
    await photo_file.download_to_drive("user_photo.jpg")
    user_photo = convert_to_binary_data("user_photo.jpg")
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_user.id).values(photo = user_photo)
    connection.execute(update_query)

    await context.bot.send_message(chat_id=update.effective_chat.id,text="Расскажи что-нибудь о себе:)")

    return BIO

async def set_bio(update: Update, context: ContextTypes.DEFAULT_TYPE):    
    user_bio = update.message.text
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_user.id).values(bio = user_bio)
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Твоя анкета готова!")
    connection.execute(update_query)
    select_query= db.select(members).where(members.columns.tg_chat_id ==update.effective_chat.id)
    select_result= connection.execute(select_query).fetchall()
    print(select_result)


    return ConversationHandler.END  

async def update_gender(update: Update,context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["Парень", "Девушка", "Другое"]]
    await update.message.reply_text("Какой ваш пол?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )
    return UPDATE
    #return UPDATE_GENDER    

async def set_update_gender(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_gender = update.message.text
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(gender = user_gender)
    connection.execute(update_query)

    return SHOW_FORM

async def update_age(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Сколько вам лет?")
    return UPDATE
    #return UPDATE_AGE

async def set_update_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_age = int(update.message.text)
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(age = user_age)
    connection.execute(update_query)
    return SHOW_FORM

async def update_name(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Как вас зовут?")
    return UPDATE
    #return UPDATE_NAME

async def set_update_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.text
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(name = user_name)
    connection.execute(update_query)
    return SHOW_FORM

async def update_faculty(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="На каком факультете вы учитесь?")
    return UPDATE
    #return UPDATE_FACULTY

async def set_update_faculty(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_faculty = update.message.text
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(faculty = user_faculty)
    connection.execute(update_query)
    return SHOW_FORM

async def update_networking(update: Update,context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Интересует ли вас нетворкинг?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )
    return UPDATE
    #return UPDATE_NETWORKING

async def set_update_networking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_networking = True
    else:
        user_networking = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(networking = user_networking)
    connection.execute(update_query)
    return SHOW_FORM

async def update_friendship(update: Update,context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Ищите ли вы дружбу?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )
    return UPDATE
    #return UPDATE_FRIENDSHIP

async def set_update_friendship(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_friendship = True
    else:
        user_friendship = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(friendship = user_friendship)
    connection.execute(update_query)
    return SHOW_FORM

async def update_relationship(update: Update,context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Интересует ли вас отношения?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )
    return UPDATE
    #return UPDATE_RELATIONSHIP

async def set_update_relationship(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_relationship = True
    else:
        user_relationship = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(relationship = user_relationship)
    connection.execute(update_query)
    return SHOW_FORM

async def update_help(update: Update,context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Нужна ли вам помощь?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )
    return UPDATE
    #return UPDATE_HELP

async def set_update_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_help = True
    else:
        user_help = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(help = user_help)
    connection.execute(update_query)
    return SHOW_FORM

async def update_chatting(update: Update,context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Хотите ли вы с кем-нибудь побеседовать?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )
    return UPDATE
    #return UPDATE_CHATTING

async def set_update_chatting(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_chatting = True
    else:
        user_chatting = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(networking = user_chatting)
    connection.execute(update_query)
    return SHOW_FORM

async def set_update_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass

async def update_bio(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Расскажи что-нибудь о себе:)")
    return UPDATE
    #return UPDATE_BIO

async def set_update_bio(update:Update, context:ContextTypes.DEFAULT_TYPE):
    user_bio = update.message.text
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(bio = user_bio)
    connection.execute(update_query)
    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )
    return SHOW_FORM

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
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Твоя анкета удалена")
    return ConversationHandler.END

async def show_form(update: Update, context:ContextTypes.DEFAULT_TYPE):
    select_query0= db.select( members.columns.name ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result0=connection.execute(select_query0)
    name_result=str(select_result0.fetchall())
    name_result=name_result.translate(str.maketrans('', '', string.punctuation))

    select_query1= db.select( members.columns.age ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result1=connection.execute(select_query1)
    age_result=str(select_result1.fetchall())
    age_result=age_result.translate(str.maketrans('', '', string.punctuation))

    select_query2= db.select( members.columns.faculty ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result2=connection.execute(select_query2)
    faculty_result=str(select_result2.fetchall())
    faculty_result=faculty_result.translate(str.maketrans('', '', string.punctuation))

    select_query3= db.select( members.columns.bio ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result3=connection.execute(select_query3)
    bio_result=str(select_result3.fetchall())
    bio_result=bio_result.translate(str.maketrans('', '', string.punctuation))

    """select_query= db.select( members.columns.photo ).where(members.columns.tg_chat_id == update.effective_chat.id)
    select_result=connection.execute(select_query)
    photo_result=select_result.fetchall()
    print(photo_result)
    filename="userphoto.jpg"
    with open(filename,'wb') as file:
        file.write(photo_result)"""

    form=f'Твоя анкета:{name_result},{age_result},{faculty_result}\n {bio_result}'
    await context.bot.send_message(chat_id=update.effective_chat.id,text=form)

async def show_update_form(update: Update, context:ContextTypes.DEFAULT_TYPE):
    if update.message.text=="НЕТ":    
        pass
    else:
        select_query0= db.select( members.columns.name ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result0=connection.execute(select_query0)
        name_result=str(select_result0.fetchall())
        name_result=name_result.translate(str.maketrans('', '', string.punctuation))

        select_query1= db.select( members.columns.age ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result1=connection.execute(select_query1)
        age_result=str(select_result1.fetchall())
        age_result=age_result.translate(str.maketrans('', '', string.punctuation))

        select_query2= db.select( members.columns.faculty ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result2=connection.execute(select_query2)
        faculty_result=str(select_result2.fetchall())
        faculty_result=faculty_result.translate(str.maketrans('', '', string.punctuation))

        select_query3= db.select( members.columns.bio ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result3=connection.execute(select_query3)
        bio_result=str(select_result3.fetchall())
        bio_result=bio_result.translate(str.maketrans('', '', string.punctuation))

        """select_query= db.select( members.columns.photo ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result=connection.execute(select_query)
        photo_result=select_result.fetchall()
        print(photo_result)
        filename="userphoto.jpg"
        with open(filename,'wb') as file:
        file.write(photo_result)"""

        form=f'Твоя анкета:{name_result},{age_result},{faculty_result}\n {bio_result}'
        await context.bot.send_message(chat_id=update.effective_chat.id,text=form)
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
    