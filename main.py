import telebot
from gtts import gTTS
import decouple

TOKEY_KEY = decouple.config('TOKEN_KEY')
bot = telebot.TeleBot(TOKEY_KEY)

def getFileName(text):
    words = text.split(' ')
    return '_'.join(words[0:2])+".mp3"

# function to convert text to speech
def textToSpeech(text, output_file = "audio.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    return output_file

@bot.message_handler(commands=['start','help'])
def start(message):
    bot.send_message(message.chat.id, "Hii!! Send any text convert it to audio")

@bot.message_handler(func=lambda m: True)
def handleTextToSpeech(message):
    output_file = textToSpeech(message.text, getFileName(message.text))
    with open(output_file, 'rb') as audio:
        bot.send_audio(message.chat.id, audio)

try:
    bot.infinity_polling(timeout=10,long_polling_timeout=5)
except Exception as e:
    print(e)