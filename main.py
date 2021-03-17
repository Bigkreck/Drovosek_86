import button
import os
import logging
import callback_button
from dotenv import load_dotenv
from aiogram.types import CallbackQuery, InputMediaPhoto
from aiogram import Bot, Dispatcher, executor, types
from act_file import get_file
from sqliconnect import SQLiconnect

load_dotenv()

bot = Bot(str(os.getenv('API_TOKEN')))
dp = Dispatcher(bot)

db = SQLiconnect('db/db.db')


@dp.message_handler(commands=['start', 'help', 'uploadimage'])
async def start_bot(message: types.Message):

    if message.text == '/start':
        if not db.get_user(message.from_user.id):
            db.add_user(message.from_user.id, message.from_user.username, message.from_user.first_name)
        info_file = get_file('info/info.txt')
        await message.answer(info_file, reply_markup=button.button_start)
    elif message.text == '/uploadimage':
        await message.answer('Выбери изображения:')


@dp.message_handler(content_types=['text'])
async def change_button(message: types.Message):
    if message.text == 'Слэбы':
        text_sleb = get_file('info/info_sleb.txt')
        await bot.send_message(message.from_user.id, text_sleb, reply_markup=button.inline_button_sleb)
    elif message.text == 'Готовые изделия':
        text_product = get_file('info/info_product.txt')
        await bot.send_message(message.from_user.id, text_product, reply_markup=button.inline_markup)


@dp.callback_query_handler(callback_button.see_calback.filter())
async def see_product(call: CallbackQuery, callback_data: dict):
    item = str(callback_data.get('item'))
    type = str(callback_data.get('type'))
    await call.message.delete_reply_markup()
    await call.message.delete()
    callback_data = call.data
    logging.info(f'call={callback_data}')
    str_item = item.lower()
    load_photo = db.get_product_image(str_item)
    group_image = []
    for i in load_photo:
        group_image.append(InputMediaPhoto(i[1], get_file(f'info/{item.lower()}_info.txt')))
    await call.message.answer_media_group(group_image)
    await call.message.answer(text=get_file(f'info/{item.lower()}_info.txt'),
                              reply_markup=button.inline_button_sleb if type=='sleb' else button.inline_markup)


@dp.message_handler(content_types=['photo'])
async def photo_upload(message: types.Message):

    db.add_image(message.photo[-1].file_id, message.caption)

if __name__ == '__main__':
    executor.start_polling(dp)
