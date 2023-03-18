from telegram import *
from telegram.ext import  ContextTypes,ConversationHandler
import sqlalchemy as db
from db import members,connection
from pathlib import Path
from random import randint

SEARCH,REPLY =range(2)
search_form_id1=" "

async def search_form(update:Update,context:ContextTypes.DEFAULT_TYPE):
    out_of_stock= db.select(db.func.count()).select_from(members).where(members.columns.tg_chat_id != update.effective_chat.id)
    count =connection.execute(out_of_stock)
    count=int(count.fetchall()[0][0])
    print(count)

    select_query= db.select(members.columns.tg_chat_id).where(members.columns.tg_chat_id != update.effective_chat.id)
    select_result=connection.execute(select_query)
    print(randint(0,count-1))
    number= randint(0,count-1)
    search_form_id=str(select_result.fetchall()[number][0])
    global search_form_id1
    search_form_id1= search_form_id

    select_query= db.select( members.columns.name ).where(members.columns.tg_chat_id == search_form_id)
    select_result=connection.execute(select_query)
    connection.commit()
    name_result=str(select_result.fetchall()[0][0])

    select_query= db.select( members.columns.age ).where(members.columns.tg_chat_id == search_form_id)
    select_result=connection.execute(select_query)
    connection.commit()
    age_result=str(select_result.fetchall()[0][0])

    select_query= db.select( members.columns.faculty ).where(members.columns.tg_chat_id == search_form_id)
    select_result=connection.execute(select_query)
    connection.commit()
    faculty_result=str(select_result.fetchall()[0][0])

    select_query= db.select( members.columns.bio ).where(members.columns.tg_chat_id == search_form_id)
    select_result=connection.execute(select_query)
    connection.commit()
    bio_result=str(select_result.fetchall()[0][0])

    select_query= db.select( members.columns.photo ).where(members.columns.tg_chat_id == search_form_id)
    select_result=connection.execute(select_query)
    connection.commit()
    photo_path=(select_result.fetchall()[0][0])
    photo_path = Path("photo",photo_path)

    select_query= db.select( members.columns.networking ).where(members.columns.tg_chat_id == search_form_id)
    select_result=connection.execute(select_query)
    connection.commit()
    if select_result.fetchall()[0][0]==True:
        networking_result="Нетворкинг"
    else:
        networking_result=""

    select_query= db.select( members.columns.friendship ).where(members.columns.tg_chat_id == search_form_id)
    select_result=connection.execute(select_query)
    connection.commit()
    if select_result.fetchall()[0][0]==True:
        friendship_result="Дружба"
    else:
        friendship_result=""

    select_query= db.select( members.columns.relationship ).where(members.columns.tg_chat_id == search_form_id)
    select_result=connection.execute(select_query)
    connection.commit()
    if select_result.fetchall()[0][0]==True:
        relationship_result="Отношения"
    else:
        relationship_result=""

    select_query= db.select( members.columns.help ).where(members.columns.tg_chat_id == search_form_id)
    select_result=connection.execute(select_query)
    connection.commit()
    if select_result.fetchall()[0][0]==True:
        help_result="Помощь"
    else:
        help_result=""

        select_query= db.select( members.columns.chatting ).where(members.columns.tg_chat_id == search_form_id)
    select_result=connection.execute(select_query)
    connection.commit()
    if select_result.fetchall()[0][0]==True:
        chatting_result="Общение"
    else:
        chatting_result="" 

    form=f'Вот анкета:\n{networking_result} {friendship_result} {relationship_result} {help_result} {chatting_result} \n{name_result},{age_result},{faculty_result}\n {bio_result}'
    await context.bot.send_message(chat_id=update.effective_chat.id,text=form)
    if name_result!="":
        await context.bot.send_photo(chat_id=update.effective_chat.id,photo=photo_path)

    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Подходит ли тебе эта анкета?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )
    return REPLY

async def reply_form(update:Update,context:ContextTypes.DEFAULT_TYPE):
    if update.message.text=="НЕТ":
        return ConversationHandler.END

    else:
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

        select_query= db.select( members.columns.tg_id ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result=connection.execute(select_query)
        connection.commit()
        id_result =str(select_result.fetchall()[0][0])  

        form=f'Кого-то заинтересовала ваша анкета:{name_result},{age_result},{faculty_result}\n {bio_result}\n @{id_result}'
        print(search_form_id1)
        await context.bot.send_message(chat_id=search_form_id1,text=form)
        if name_result!="":
            await context.bot.send_photo(chat_id=search_form_id1,photo=photo_path)  

        return ConversationHandler.END  
