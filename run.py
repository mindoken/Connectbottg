from utils import start,create_form,echo
from telegram import *
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler    

def Run():
    application = ApplicationBuilder().token('6207411726:AAGTkgz8niKVarLEqwj4mbpE7MfXEFJLC1Q').build()

    start_handler = CommandHandler('start', start)
    create_form_handler = CommandHandler('create_form', create_form)
    echo_handler = CommandHandler('echo',echo)
    find_photo_handler = CommandHandler('find_photo',find_photo)
    download_video_handler = CommandHandler('download_video',download_video)
    application.add_handler(start_handler)
    application.add_handler(create_form_handler)
    application.add_handler(caps_handler)
    application.add_handler(find_photo_handler)
    application.add_handler(download_video_handler)

    application.run_polling()
