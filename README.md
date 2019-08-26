# TG2Notion - Telegram to Notion
A tiny Telegram bot that receives a message in a specified format (more on that further down this README) and creates a row in a provided Notion database / table.

I use it to quickly create tasks (I use Notion for everything, including ToDos) on mobile, because the Notion app is so fucking slow that half of the time I forget what task I wanted to add until Notion fully loads.

I usually don't work with Python and just wanted to get it working quick (not the most beautiful code), but since the [unofficial Notion API package](https://github.com/jamalex/notion-py) is written in Python, this was the easiest way.

## Installation
There is a Dockerfile and a docker-compose.yml. The easiest way to use this bot is to `docker-compose up -d`.

If you don't want to use Docker and install it manually, the Dockerfile should give you everything you need (especially the dependencies of this project).

Please keep in mind that you will still need to set the environment vars even if you don't use Docker.

## Configuration
You need to have an inline / a full page table inside of Notion set up like this: [Screenshot](https://imgur.com/a/M1jbUIJ).

It's important to have exactly the same column names (otherwise you have to alter src/notionutil/notionutil.py).

Several environment variables have to be set in order for this bot to work.

Rename `tg2n.env.sample` to `tg2n.env`

* TG2N_TG_BOT_TOKEN
  * The API token for your Telegram bot that was provided by @BotFather
* TG2N_TG_CHAT_ID
  * The Telegram User ID that you want to allow creating Notion rows. Basically a whitelist.
  * You can uncomment the first line of the `onMessageReceived` function in src/bot.py to receive your Uer ID as a response to the message you send to the bot.
* TG2N_NOTION_TOKEN
  * Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
* TG2N_NOTION_CV_LINK
  * A link to the database in Notion (not the page that contains the database but a link to the database itself)
  * If you hover with your mouse over your database, the `New` button should appear. Left to this button there are three horizontally aligned dots: Click on those dots and click "Copy link".
* TG2N_TIMEZONE
  * Your timezone. Will be used for the date column of your database to set the correct date and time.

## How to use the bot
The bot expects the format of the message to be one of these:

*First line*: Title of the table row

*Second line*: empty!

*Third line*: A date in one of these formats: "YYYYMMDD" OR "YYYYMMDD HHmm"

*Fourth line*: empty!

*Fifth line*: Any text content that will be shown once you click into this created row

**OR**

*First line*: Title

*Second line*: empty!

*Third line*: A date in one of these formats: "YYYYMMDD" OR "YYYYMMDD HM"

**OR**

*First line*: Title

### Example
"Test Todo

20190925 1405

Contents of that ToDo entry here :)"

Now a new ToDo entry will be created in the provided Notion page with a due date of 2019/09/25 02:05 pm.

## ToDo
- [ ] Allow to set reminders while setting a due date (have not found out yet how to do that programmatically)

## License
MIT
