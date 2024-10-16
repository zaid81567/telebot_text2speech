# Text-to-MP3 Telegram Bot

This is a Telegram bot that converts text messages into audio files using Google Text-to-Speech (gTTS). Users can send any text, and the bot will respond with an MP3 audio file of that text.

## Features
- Converts user text input into audio format (MP3).
- Responds to `/start` and `/help` commands with a welcome message.
- Automatically generates filenames based on the first two words of the text input.

## Requirements
- Python 3.x
- `pyTelegramBotAPI==4.10.0`
- `python-decouple==3.8`
- `gtts==2.5.3`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/zaid81567/telebot_text2speech.git
   cd telebot_text2speech
