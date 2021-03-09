from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup
from callback_button import see_calback

#Кнопки выбора типа изделия
button_sleb = KeyboardButton('Слэбы')
button_product = KeyboardButton('Готовые изделия')

#Кнопки выбора типа дерева
button_type_dub = KeyboardButton('Дуб 🌳')
button_type_klen = KeyboardButton('Клен 🌳')
button_type_kaagach = KeyboardButton('Карагачь 🌳')
button_type_olha = KeyboardButton('Ольха🌳')

#Фиксированные кнопки при старте
button_start = ReplyKeyboardMarkup(resize_keyboard=True).row(button_sleb, button_product)

#инлайн кнопки
inline_button_sleb = InlineKeyboardMarkup()
inline_button_dub = InlineKeyboardButton('Посмотреть Дуб 🌳',
                                         callback_data=see_calback.new(item='Dub', type='sleb'))
inline_button_klen = InlineKeyboardButton('Посмотреть Клен 🌳',
                                          callback_data=see_calback.new(item='Klen', type='sleb'))
inline_button_karagach = InlineKeyboardButton('Посмотреть Карагачь 🌳',
                                          callback_data=see_calback.new(item='karagach', type='sleb'))
inline_button_sleb.add(inline_button_dub)
inline_button_sleb.add(inline_button_klen)
inline_button_sleb.add(inline_button_karagach)

#
inline_button_wine = InlineKeyboardButton('Винные подставки',
                                          callback_data=see_calback.new(item='wine', type='product'))
inline_button_board = InlineKeyboardButton('Разделочные доски',
                                           callback_data=see_calback.new(item='board',type='product'))
inline_button_tile = InlineKeyboardButton('Декоративная плитка',
                                          callback_data=see_calback.new(item='tiles', type='product'))
inline_button_table = InlineKeyboardButton('Журнальные столики',
                                          callback_data=see_calback.new(item='table', type='product'))
inline_markup = InlineKeyboardMarkup(
    inline_keyboard = [
        [inline_button_wine, inline_button_board],
        [inline_button_table, inline_button_tile]
    ]
)
