from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = '7985037422:AAFqE0kUaD8IRn_2mjPQM1Ikvnndokmf-Cw'
BOT_USERNAME: Final = '@vdtttt003bot'

# Các lệnh command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Chào bạn, tôi là bot hỗ trợ quản lý chi tiêu cá nhân của VDT!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Đây là các lệnh mà tôi hỗ trợ:\n'
                                     '/start - Bắt đầu sử dụng bot\n'
                                     '/help - Hiển thị danh sách các lệnh\n'
                                     '/add - Thêm một khoản chi tiêu\n'
                                     '/list - Hiển thị danh sách các khoản chi tiêu\n'
                                     '/delete - Xóa một khoản chi tiêu\n'
                                     '/total - Hiển thị tổng số tiền đã chi tiêu\n')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Đây là một lệnh custom!')

# Các lệnh xử lý nội dung
def handle_response(txt: str) -> str:
    if txt.lower() == 'xin chào':
        return 'Chào bạn!'
    return 'Tôi không hiểu bạn nói gì!'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    message_text = update.message.text
    print(f'User {update.message.id} in {message_type} chat says: {message_text}')

    if message_type == 'group':
        if BOT_USERNAME in message_text:
            response = 'Bạn cần gì ở tôi à?'
        else:
            return
    else:
        response = handle_response(message_text)
    print('Bot says:', response)
    await update.message.reply_text(response)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()
    # Đăng ký các command
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    # Đăng ký xử lý text
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    # Đăng ký xử lý lỗi
    app.add_error_handler(error_handler)

    print('Polling...')
    app.run_polling(poll_interval=3)