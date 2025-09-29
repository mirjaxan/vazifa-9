from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Registratsiya uchun
register_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Registration")]
    ],
    resize_keyboard=True
)

# Asosiy menyu
main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📖 Menu")],
        [KeyboardButton(text="🛒 Order"), KeyboardButton(text="☎️ Contact")]
    ],
    resize_keyboard=True
)

# Menu tugmasi ichidagi menyu
menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔍 Search"), KeyboardButton(text="🆕 New")],
        [KeyboardButton(text="💸 Discount"), KeyboardButton(text="📚 All")],
        [KeyboardButton(text="⬅️ Back")]
    ],
    resize_keyboard=True
)

# Search tugmasi ichidagi menyu
search_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📂 Genre"), KeyboardButton(text="✍️ Author")],
        [KeyboardButton(text="📖 Title")],
        [KeyboardButton(text="⬅️ Back")]
    ],
    resize_keyboard=True
)
