import asyncio
from aiogram import Bot,Dispatcher
from aiogram.client.bot import DefaultBotProperties

from handler.users.private import user_private_router
from handler.group.groups import group_router

BOT_TOKEN = '6717297238:AAE1lAwIuPzG41k-bAcZGJSzBK3SujH9COo'


bot = Bot(token=BOT_TOKEN,default=DefaultBotProperties(parse_mode='HTML'))
ds = Dispatcher()

ds.include_routers(user_private_router,group_router)

async def on_startup(bot):
    print('I work')

async def main():
    ds.startup.register(on_startup)
    await ds.start_polling(bot)

asyncio.run(main())