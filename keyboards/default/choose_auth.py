from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_editors = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="🇺🇿 Uzbek editors"),
            KeyboardButton(text="🇸🇦 Arabic editors"),
        ]

    ], resize_keyboard=True
)

uzb_editors = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Shayx Muhammad Sodiq Muhammad Yusuf"),

        ],
        [
            KeyboardButton(text="Shayx Alouddin Mansur"),
        ]

    ], resize_keyboard=True
)

arab_editors = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Quran-la (en)"),

        ],
        [
            KeyboardButton(text="Shayx Jalaladdinalmah (abar)"),
        ]

    ], resize_keyboard=True
)