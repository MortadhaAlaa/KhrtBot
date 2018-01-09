from telegram import InputTextMessageContent, InlineQueryResultArticle
from telegram.ext import InlineQueryHandler, Updater
import random, os


arabic = "ابتثجحخدذرزسشصضطظعغفقكلمنهويىﻻ"
def inline_query(bot, update):
     query = update.inline_query.query
     if not query.isdigit():
         return
     query = min(int(query), 2000)
     bot.answer_inline_query(
         update.inline_query.id,
         [
             InlineQueryResultArticle(
                 id=update.inline_query.id,
                 title='خرط',
                 input_message_content=InputTextMessageContent(''.join([random.choice(arabic) for _ in range(query)]))
             )
         ],
         cache_time=0
     )


u = Updater(os.environ['TELEGRAM_TOKEN'])
d = u.dispatcher
d.add_handler(InlineQueryHandler(inline_query))

u.start_polling()
u.idle()