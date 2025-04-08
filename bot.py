





from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# TOKEN: final = '8053469306:AAFv-9qj3_4H2NRYstPW9uwW49F_Mxx8BKw'
TOKEN: final = '6482255236:AAEScgnZK3hsIpOQ-sxlHGAxK1H5R0e3UXI'
BOT_USERNAME: final = '@rewarddistributionbot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your bot. You can talk to me here:')
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! how can i help you?')
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello!This is a custom commmand')

#Responses
                                    
async def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'hello' in processed:
        return 'Hello! How can I assist you today?'
    
    if 'how are you' in processed:
        return 'I am good!'
    
    if 'python' in processed:
        return 'Python is a great programming language!'
    
    return 'I am not sure how to respond to that.'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.messageg.chat.type
    text: str = update.message.text
    
    print(f"User({update.effective_user.id}) in {message_type} sent: {text}")
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    
    
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    
    
    #commands
    
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
    #messages
    
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    
    #errors
    
    app.add_error_handler(error)
    
    #Polls tthe bot
    print('Bot started!')

    app.run_polling(poll_interval=1)