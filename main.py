from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands import *
from read import readfile



app = ApplicationBuilder().token(readfile()).build()
print('start')
app.add_handler(CommandHandler("plus", addition))
app.add_handler(CommandHandler("minus", subtraction))
app.add_handler(CommandHandler("mult", multiplication))
app.add_handler(CommandHandler("div", division))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("comp", compl))
app.run_polling()