from utils import start, create_form, cancel, show_form,delete_form,delete_form_end,show_update_form
from utils import set_gender, set_age, set_chatting, set_faculty, set_friendship, set_help, set_name, set_networking, set_photo, set_relationship, set_bio
from utils import update_gender,update_age,update_bio,update_chatting,update_faculty,update_friendship,update_help,update_name,update_networking,update_relationship
from utils import set_update_gender,set_update_age,set_update_bio,set_update_chatting,set_update_faculty,set_update_friendship,set_update_help,set_update_name,set_update_networking,set_update_relationship
from utils import GENDER, NAME, AGE, FACULTY,NETWORKING,FRIENDSHIP, RELATIONSHIP, HELP, CHATTING ,PHOTO, BIO
from utils import DELETE_FORM,SHOW_FORM,UPDATE
#from utils import UPDATE_GENDER,UPDATE_AGE
#from utils import SHOW_NEW_GENDER,SHOW_NEW_AGE
from telegram import *
from telegram.ext import ApplicationBuilder, CommandHandler,ConversationHandler,MessageHandler,filters
import db

def Run():
    exec("db")
    application = ApplicationBuilder().token('6207411726:AAGTkgz8niKVarLEqwj4mbpE7MfXEFJLC1Q').build()

    start_handler = CommandHandler('start', start)

    create_form_handler = ConversationHandler(
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
    
    show_form_handler = CommandHandler('show_form',show_form)

    delete_form_handler = ConversationHandler(
        entry_points=[CommandHandler('delete_form',delete_form)],
        states={
            DELETE_FORM:[MessageHandler(filters.TEXT,delete_form_end)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        )

    update_gender_handler = ConversationHandler(
        entry_points=[CommandHandler('update_gender',update_gender)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_gender)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_age_handler = ConversationHandler(
        entry_points=[CommandHandler('update_age',update_age)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_age)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_name_handler = ConversationHandler(
        entry_points=[CommandHandler('update_name',update_name)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_name)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_faculty_handler = ConversationHandler(
        entry_points=[CommandHandler('update_faculty',update_faculty)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_faculty)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_networking_handler = ConversationHandler(
        entry_points=[CommandHandler('update_networking',update_networking)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_networking)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_friendship_handler = ConversationHandler(
        entry_points=[CommandHandler('update_friendship',update_friendship)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_friendship)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_relationship_handler = ConversationHandler(
        entry_points=[CommandHandler('update_relationship',update_relationship)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_relationship)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_help_handler = ConversationHandler(
        entry_points=[CommandHandler('update_help',update_help)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_help)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    update_chatting_handler = ConversationHandler(
        entry_points=[CommandHandler('update_chatting',update_chatting)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_chatting)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    ) 

    update_bio_handler = ConversationHandler(
        entry_points=[CommandHandler('update_bio',update_bio)],
        states={
            UPDATE:[MessageHandler(filters.TEXT,set_update_bio)],
            SHOW_FORM:[MessageHandler(filters.TEXT & ~filters.COMMAND,show_update_form)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

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
    application.run_polling()
