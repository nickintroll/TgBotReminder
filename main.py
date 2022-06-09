from aiogram import Bot, Dispatcher, executor

bot = Bot('TOKEN')
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message):
    print(message.from_user.id)
    await message.answer('I just got your ID, and know that now bot is started to work. I\'ll keep working on the project')

if __name__ == '__main__':
    executor.start_polling(dp)
    
