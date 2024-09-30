from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def CreateInline(*args,**kwargs) -> InlineKeyboardBuilder:
    bulder = InlineKeyboardBuilder()
    for i in args:
        bulder.add(InlineKeyboardButton(text=i,callback_data=i))
    for l,g in kwargs.items():
        bulder.add(InlineKeyboardButton(text=g,callback_data=l))
    bulder.adjust(2)
    return bulder.as_markup()

def CreateBut(*args,**kwargs) -> InlineKeyboardBuilder:
    bulder = InlineKeyboardBuilder()
    for i in args:
        for t in i:
            bulder.add(InlineKeyboardButton(text=t,callback_data=t))
    
    for l,g in kwargs.items():
        bulder.add(InlineKeyboardButton(text=g,callback_data=l))
    bulder.adjust(2)
    return bulder.as_markup()

