import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from telegram.error import TimedOut

# Load environment variables
load_dotenv()

# Get the bot API token from the environment
BOT_API = os.getenv('BOT_API')

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the application object with timeout set
application = Application.builder().token(BOT_API).build()

# Define the start command handler
async def start(update: Update, context: CallbackContext):
    try:
        await update.message.reply_text("Welcome to the best Bot on Telegram")
    except TimedOut:
        logger.error("Timed out while replying to user")

# Define the help command handler
async def help(update: Update, context: CallbackContext):
    await update.message.reply_text("Your Message")

# Define the Gmail URL handler
async def gmail_url(update: Update, context: CallbackContext):
    await update.message.reply_text("gmail link here")

# Define the YouTube URL handler
async def youtube_url(update: Update, context: CallbackContext):
    await update.message.reply_text("youtube link")

# Define the LinkedIn URL handler
async def linkedIn_url(update: Update, context: CallbackContext):
    await update.message.reply_text("Your linkedin profile url")

# Define handler for unknown text
async def unknown_text(update: Update, context: CallbackContext):
    await update.message.reply_text("Sorry I can't recognize you, you said '%s'" % update.message.text)

# Define handler for unknown commands
async def unknown(update: Update, context: CallbackContext):
    await update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)

# Add handlers for commands
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('help', help))
application.add_handler(CommandHandler('gmail', gmail_url))
application.add_handler(CommandHandler('youtube', youtube_url))
application.add_handler(CommandHandler('linkedin', linkedIn_url))

# Add handler for unknown text
application.add_handler(MessageHandler(filters.TEXT, unknown_text))

# Add handler for unknown commands
application.add_handler(MessageHandler(filters.COMMAND, unknown))

# Error handler for timeout or other errors
async def error_handler(update: Update, context: CallbackContext):
    try:
        raise context.error
    except TimedOut:
        logger.error(f"Timed out while processing update {update}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

application.add_error_handler(error_handler)

# Start polling for updates
application.run_polling(timeout=30)  # Increase the timeout to 30 seconds
