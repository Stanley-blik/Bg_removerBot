#Remove_Bg python script BY StaNLink Dev Team
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import PHOTO
from rembg import remove
from io import BytesIO
import os

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '7324338784:AAG6uFqCirGL0r_gf01SIDCXYdQWCf2icqw'

def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"Welcome, {user.first_name}! Send me an image to remove its background.")

def help_command(update, context):
    update.message.reply_text("Here's how to use me:\n\n"
                              "/start - Start the bot\n"
                              "/help - Get these instructions\n"
                              "Send an image - I'll remove the background for you.\n"
                              "/about - Learn more about me.")

def remove_background(update, context):
    user = update.message.from_user
    update.message.reply_text(f"Processing your image, {user.first_name}...")
    try:
        photo_file = context.bot.get_file(update.message.photo[-1].file_id)
        photo_bytes = photo_file.download_as_bytearray()

        # Remove background
        output_bytes = remove(photo_bytes)

        # Send the processed image
        context.bot.send_photo(chat_id=update.message.chat_id, photo=BytesIO(output_bytes))
        update.message.reply_text("Background removed!")

    except Exception as e:
        update.message.reply_text(f"Sorry, there was an error processing your image: {e}")

def about(update, context):
    update.message.reply_text("I am Bg_RemoverBot, created to instantly remove backgrounds from your images. Just send me a picture, and I'll take care of the rest!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(PHOTO, remove_background))
    dp.add_handler(CommandHandler("about", about))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
