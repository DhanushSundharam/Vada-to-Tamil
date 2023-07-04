from telegram.ext import Updater, CommandHandler,MessageHandler, Filters
import json
with open("Vada eluthu Final.json","r",encoding="utf-8") as file:
    word_meanings=json.load(file)


def start(update, context):
    statement = "வடக்கு வார்த்தையிலிருந்து தமிழ் வார்த்தை மற்றும் பொருள் பாட்க்கு வரவேற்கிறோம்!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=statement)

def help(update, context):
    howto_message = "போட்டைப் பயன்படுத்த:\n1. அரட்டையில் ஏதேனும் வடக்கு வார்த்தையை உள்ளிடவும்.\n2. போட் தமிழ், ஆங்கிலம், வார்த்தை சராசரி மற்றும் இலக்கணத்தில் அதன் அர்த்தங்களுடன் பதிலளிக்கும்"
    context.bot.send_message(chat_id=update.effective_chat.id, text=howto_message)

def handle_message(update, context):
    word = update.message.text.strip()
    meaning_tamil = word_meanings.get(word, {}).get("ta")
    meaning_english = word_meanings.get(word, {}).get("en")
    mean=word_meanings.get(word,{}).get("mean")
    grammar=word_meanings.get(word,{}).get("grammar")

    if meaning_tamil and meaning_english:
        
        options = f"Word: {word}\n\nTamil: {meaning_tamil}\n\nEnglish: {meaning_english}\n\nMean:{mean}\n\nGrammar:{grammar}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=options)
    else:
        
        context.bot.send_message(chat_id=update.effective_chat.id, text="Word not found.")


updater = Updater("6086803494:AAFNdSccXo0Cck0fG4FAtE83zXK8L2EJUn4", use_context=True)
dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))


updater.start_polling()
