#Remove_Bg python script BY StaNLink Dev Team
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from rembg import remove
from PIL import Image
import io 

TOKEN = "7324338784:AAEVX8mPFkd4G8tsYTLUqtl-EdrofFDP02g"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🎨Send me an emoji and I'll remove it's background for you!")

def remove_bg(update: Update, context: CallbackContext):
    photo = update.message.photo[-1]
    file = context.bot.get_file(photo.file_id)
    img_bytes = io.BytesIO(file.download_as_bytearray())

    #process image with rembg
    input_img = Image.open(img_bytes)
    output_img = remove(input_img)

    #send the processed image back to the user
    bio = io.BytesIO()
    output_img.save(bio, format="PNG")
    bio.seek(0)

    update.message.reply_photo(photo=bio, caption="✅Background removed by StaNLink engine!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, remove_bg))

    updater.start_polling()
    updater.idle()

if __main__ == "__main__":
    main()
