import telebot
import pyttsx3
import decouple

TOKEY_KEY = decouple.config('TOKEN_KEY')
bot = telebot.TeleBot(TOKEY_KEY)

# function to convert text to speech
def textToSpeech(text, output_file = "audio.mp3"):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    return output_file

@bot.message_handler(commands=['start','help'])
def start(message):
    bot.send_message(message.chat.id, "Hii!! Send any text convert it to audio")

# for future update -> male/female voice option
# @bot.message_handler(commands=['vm'])
# def HandleTextToSpeechMale(message):
#     text = ' '.join((message.text).split(' ')[1:])
#     output_file = textToSpeech(text)
#     with open(output_file, 'rb') as audio:
#         bot.send_audio(message.chat.id, audio)

@bot.message_handler(func=lambda m: True)
def handleTextToSpeech(message):
    output_file = textToSpeech(message.text)
    with open(output_file, 'rb') as audio:
        bot.send_audio(message.chat.id, audio)

try:
    bot.infinity_polling(timeout=10,long_polling_timeout=5)
except Exception as e:
    print(e)