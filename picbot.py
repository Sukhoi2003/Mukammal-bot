from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram import types
from api import api_request

TOKEN = "5807670161:AAHF3UYGHgUYpHYRiyKSEnDCQnDejiDN8pU"



bot = Bot(token=TOKEN)

dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def do_start(message: types.Message):
    await message.answer("Assalomu alaykum botimizga xush kelibsiz")



@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_images_from_user(message: types.Message):
    message_id = await message.answer("Yuklanmoqda...🚀")
    photo_id = message.photo[-1].file_id
    phot_info = await bot.get_file(photo_id)
    file_path = phot_info["file_path"]
    photo_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"


    data = await api_request(photo_url)

    if data is not None:
        await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
        await message.answer_photo(photo=data)
    else:
        await message.answer("Iltimos boshqa rasm kiriting")



if __name__ == "__main__":

    executor.start_polling(dp)

#ishlamadi