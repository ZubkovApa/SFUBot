import asyncio
from .bot import dp, bot
from .handlers import start as start_handler
from .handlers import faq as faq_handler
from .handlers import survey as survey_handler
from .db import init_db

dp.include_router(start_handler.router)
dp.include_router(faq_handler.router)
dp.include_router(survey_handler.router)

async def main():
    init_db()
    print('Bot is starting...')
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
