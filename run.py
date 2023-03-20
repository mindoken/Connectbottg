from utils import start, create_form, cancel, show_form,delete_form,delete_form_end, help
from utils import set_gender, set_age, set_chatting, set_faculty, set_friendship, set_help, set_name, set_networking, set_photo, set_relationship, set_bio
from update import update_gender,update_age,update_bio,update_chatting,update_faculty,update_friendship,update_help,update_name,update_networking,update_relationship,update_photo
from update import set_update_gender,set_update_age,set_update_bio,set_update_chatting,set_update_faculty,set_update_friendship,set_update_help,set_update_name,set_update_networking,set_update_relationship,set_update_photo,show_update_form
from search import search_form,reply_form
from utils import GENDER, NAME, AGE, FACULTY,NETWORKING,FRIENDSHIP, RELATIONSHIP, HELP, CHATTING ,PHOTO, BIO,DELETE_FORM
from update import SHOW_FORM,UPDATE
from search import REPLY
from telegram import *
from telegram.ext import ApplicationBuilder, CommandHandler,ConversationHandler,MessageHandler,filters
import db

def Run():
    exec("db") #запуск БД
    application = ApplicationBuilder().token('6207411726:AAGTkgz8niKVarLEqwj4mbpE7MfXEFJLC1Q').build() #запуск бота по токену

    start_handler = CommandHandler('start', start) #стартовая команда для бота

    create_form_handler = ConversationHandler( #создание диалоговой формы для создание анкеты
        entry_points=[CommandHandler('create_form', create_form)],
        states={
            GENDER:[MessageHandler(filters.TEXT,set_gender)],
            NAME:[MessageHandler(filters.TEXT, set_name)],
            AGE:[MessageHandler(filters.TEXT, set_age)],
            FACULTY:[MessageHandler(filters.TEXT,set_faculty)],
            NETWORKING:[MessageHandler(filters.TEXT,set_networking)],
            FRIENDSHIP:[MessageHandler(filters.TEXT,set_friendship)],
            RELATIONSHIP:[MessageHandler(filters.TEXT,set_relationship)],
            HELP:[MessageHandler(filters.TEXT,set_help)],
            CHATTING:[MessageHandler(filters.TEXT,set_chatting)],
            PHOTO:[MessageHandler(filters.PHOTO,set_photo)],
            BIO:[MessageHandler(filters.TEXT & ~filters.COMMAND, set_bio)]      
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        )
    
    show_form_handler = CommandHandler('show_form',show_form) #команда для показывания собственной анкеты

    delete_form_handler = ConversationHandler( #создание диалоговой формы для удаления анкеты
        entry_points=[CommandHandler('delete_form',delete_form)],
        states={
            DELETE_FORM:[MessageHandler(filters.TEXT,delete_form_end)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        )

    update_gender_handler = ConversationHandler( #создание диалоговой формы для обновления данных в части "пол"
        entry_points=[CommandHandler('update_gender',update_gender)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_gender)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_age_handler = ConversationHandler( #создание диалоговой формы для обновления данных в части "возраст"
        entry_points=[CommandHandler('update_age',update_age)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_age)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_name_handler = ConversationHandler( #создание диалоговой формы для обновления данных в части "имя"
        entry_points=[CommandHandler('update_name',update_name)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_name)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_faculty_handler = ConversationHandler( #создание диалоговой формы для обновления данных в части "факультет"
        entry_points=[CommandHandler('update_faculty',update_faculty)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_faculty)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_networking_handler = ConversationHandler( #создание диалоговой формы для обновления данных в части "нетворкинг"
        entry_points=[CommandHandler('update_networking',update_networking)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_networking)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_friendship_handler = ConversationHandler( #создание диалоговой формы для обновления данных в части "дружба"
        entry_points=[CommandHandler('update_friendship',update_friendship)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_friendship)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_relationship_handler = ConversationHandler( #создание диалоговой формы для обновления данных в части "отношения"
        entry_points=[CommandHandler('update_relationship',update_relationship)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_relationship)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_help_handler = ConversationHandler( #создание диалоговой формы для обновления данных в части "помощь"
        entry_points=[CommandHandler('update_help',update_help)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_help)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_chatting_handler = ConversationHandler( #создание диалоговой формы для обновления данных в части "общение"
        entry_points=[CommandHandler('update_chatting',update_chatting)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_chatting)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_photo_handler = ConversationHandler( #создание диалоговой формы для обновления данных в части "фото"
        entry_points=[CommandHandler('update_photo',update_photo)],
        states={
            UPDATE:[MessageHandler(filters.PHOTO,set_update_photo)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    ) 

    update_bio_handler = ConversationHandler( #создание диалоговой формы для обновления данных в части "о себе"
        entry_points=[CommandHandler('update_bio',update_bio)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_bio)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    search_form_handler = ConversationHandler( #создание диалоговой формы для просмотра чужой анкеты
        entry_points=[CommandHandler('search_form',search_form)],
        states={
            REPLY:[MessageHandler(filters.TEXT & ~filters.COMMAND,reply_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    help_handler = CommandHandler('help',help) #команда выводящая все доступные пользователю действия

#данный блок посвящен добавлению команд в бота для их определения после отправки команды

    application.add_handler(start_handler)
    application.add_handler(create_form_handler)
    application.add_handler(show_form_handler)
    application.add_handler(delete_form_handler)
    application.add_handler(update_gender_handler)
    application.add_handler(update_age_handler)
    application.add_handler(update_name_handler)
    application.add_handler(update_faculty_handler)
    application.add_handler(update_networking_handler)
    application.add_handler(update_friendship_handler)
    application.add_handler(update_relationship_handler)
    application.add_handler(update_help_handler)
    application.add_handler(update_chatting_handler)
    application.add_handler(update_bio_handler)
    application.add_handler(update_photo_handler)
    application.add_handler(search_form_handler)
    application.add_handler(help_handler)
    application.add_handler(audio_handler)
    application.run_polling()
