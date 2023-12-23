import os
import openai
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# loading the env variables
load_dotenv()
telegram_token = os.environ['TELEGRAM_TOKEN']
openai.api_key = os.getenv("OPENAI_API_KEY")

# initialize fileNumber to 1 by default
fileNumber = 1


# Telegram bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am your Telegram bot. Use /setfile <number> to set the chat file.')


# Command handler to set the fileNumber
def set_file(update: Update, context: CallbackContext) -> None:
    global fileNumber
    try:
        # Get the provided argument
        arg = context.args[0] if context.args else ''

        if not arg:
            # If no argument is provided, suggest possible file numbers
            suggestions = ' '.join([f'/setfile {i}' for i in range(1, 4)])  # Adjust the range as needed
            update.message.reply_text(f'Please provide a file number. Suggestions: {suggestions}')
        else:
            # Try to set the file number
            fileNumber = int(arg)
            update.message.reply_text(f'Successfully set file number to {fileNumber}.')
            print(f'Successfully set file number to {fileNumber}.')  # Print success statement
    except (ValueError, IndexError):
        update.message.reply_text('Invalid file number. Usage: /setfile <number>.')


def handle_message(update: Update, context: CallbackContext) -> None:
    global chat, fileNumber
    try:
        user_message = update.message.text

        # Check if fileNumber is set
        if fileNumber is not None:
            file = f'chats/chat{fileNumber}.txt'
            with open(file, "r") as f:
                chat = f.read()
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": f"{chat}\nmyGPT:"},
                        {"role": "user", "content": user_message}
                    ],
                    temperature=1,
                    max_tokens=500,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                bot_message = response['choices'][0]['message']['content']
                update.message.reply_text(bot_message)
        else:
            update.message.reply_text('Please use /setfile <number> to set the chat file first.')

    except Exception as e:
        print(e)
        chat = ""


def main() -> None:
    updater = Updater(token=telegram_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("setfile", set_file, pass_args=True))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    print('Telegram bot is running!')
    updater.idle()


if __name__ == '__main__':
    main()
