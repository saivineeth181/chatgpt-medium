from telegram import ForceReply, Update
from telegram.ext import (Application, CommandHandler, ContextTypes, MessageHandler,
filters)

from chatgpt_api import generate_text

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	user = update.effective_user
	await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def chatgpt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	print(update.message.reply_to_message)
	print(update.message.reply_to_message.text)
	text = generate_text(update.message.text)
	await update.message.reply_text(text)

def main() -> None :
	application = Application.builder().token("5821602894:AAEdLsWJnIlIHVQkeebkQFqMpWxQgmHpErg").build()
	application.add_handler(CommandHandler("start", start))
	application.add_handler(CommandHandler("help", help_command))
	application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chatgpt))
	application.run_polling()

if __name__ == "__main__":
    main()