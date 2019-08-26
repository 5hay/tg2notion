import os
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from notionutil import notionutil

def onMessageReceived(bot, update):
    #update.message.reply_text(update.message.chat_id)

    # If the environment var is not set, anyone can add rows!
    if 'TG2N_TG_CHAT_ID' in os.environ:
        # Only react to my chat_id
        if update.message.chat_id != int(os.environ['TG2N_TG_CHAT_ID']):
            return
    else:
        update.message.reply_text("Please provide a chat / user id. Otherwise anyone can add rows into your Notion account!")

    text = update.message.text
    todoInfo = text.split("\n\n")

    # We expect title, date and content
    if len(todoInfo) == 3:
        notionutil.addTodoEntry(name=todoInfo[0], dueDate=todoInfo[1], desc=todoInfo[2])
    # We expect the title and a date
    elif len(todoInfo) == 2:
        notionutil.addTodoEntry(name=todoInfo[0], dueDate=todoInfo[1])
    # We expect only the title
    else:
        notionutil.addTodoEntry(name=todoInfo[0])

def main():
    updater = Updater(token=os.environ['TG2N_TG_BOT_TOKEN'])
    dispatcher = updater.dispatcher

    addTodoHandler = MessageHandler(Filters.text, onMessageReceived)
    dispatcher.add_handler(addTodoHandler)

    updater.start_polling()

if __name__ == "__main__":
    main()
