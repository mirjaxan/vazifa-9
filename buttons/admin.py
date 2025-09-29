from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Admin panel asosiy
admin_main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📖 Menu")],
        [KeyboardButton(text="🛒 Order"), KeyboardButton(text="📊 Dashboard")]
    ],
    resize_keyboard=True
)

# Menu tugmalari
admin_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Add"), KeyboardButton(text="📚 All")],
        [KeyboardButton(text="⬅️ Back")]
    ],
    resize_keyboard=True
)

# Add bo‘limi tugmalari
add_book_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💾 Save")],
        [KeyboardButton(text="⬅️ Back")]
    ],
    resize_keyboard=True
)

# Order tugmalari
admin_order_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🆕 New"), KeyboardButton(text="🔄 In Progress")],
        [KeyboardButton(text="📚 All")],
        [KeyboardButton(text="✏️ Update"), KeyboardButton(text="❌ Delete")],
        [KeyboardButton(text="⬅️ Back")]
    ],
    resize_keyboard=True
)
