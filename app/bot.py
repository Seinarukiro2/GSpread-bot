from asyncio import exceptions
from telethon import TelegramClient, events, Button, types
import config # config file "config.py" with constants TELEGRAM_API_ID, TELEGRAM_API_HASH, BOT_TOKEN
import gs_main

admins = [] # write admins ids here 

menu = [
    Button.text("Income ➕", resize=True),
    Button.text("Total profit 📊", resize=True),
    Button.text("Expense ➖", resize=True)
    ]

cancel = [
    Button.text("Cancel ❌", resize=True)
]
    

client = TelegramClient('bot', config.TELEGRAM_API_ID, config.TELEGRAM_API_HASH)
client.parse_mode = "html"

@client.on(events.NewMessage(pattern=r'^(/start)'))
async def my_status(event):
    sender = await event.get_sender()
    user_id = sender.id
    if user_id in admins:
        await event.respond(f'Welcome.', buttons=menu)


@client.on(events.NewMessage(pattern=r'^(/url)'))
async def my_status(event):
    sender = await event.get_sender()
    user_id = sender.id
    if user_id in admins:
        url = gs_main.get_document_link()
        await event.respond(f'Documet link: \n\n{url}', buttons=menu)


@client.on(events.NewMessage(pattern=r'^(Total profit 📊)'))
async def my_status(event):
    sender = await event.get_sender()
    user_id = sender.id
    if user_id in admins:
        total = await gs_main.get_total()
        await event.respond(f'Your totoal profit - {total}.')


@client.on(events.NewMessage(pattern=r'^(Income ➕)'))
async def my_status(event):
    sender = await event.get_sender()
    user_id = sender.id
    if user_id in admins:
        async with client.conversation(event.chat.id) as conv:
            try:
                msg1 = await conv.send_message(f'Enter income: ', buttons=cancel)
                value = await conv.get_response(timeout=100)
                if value.text == 'Cancel ❌':
                    await event.reply(f'Сanceled.', buttons=menu)
                    return
            except exceptions.TimeoutError:
                await conv.send_message(f"Time's up...", buttons=menu)

        await gs_main.add_new_earnings(value.text)
        await event.reply(f'Added.', buttons=menu)


@client.on(events.NewMessage(pattern=r'^(Expense ➖)'))
async def my_status(event):
    sender = await event.get_sender()
    user_id = sender.id
    if user_id in admins:
        async with client.conversation(event.chat.id) as conv:
            try:
                msg1 = await conv.send_message(f'Enter expense: ', buttons=cancel)
                value = await conv.get_response(timeout=100)
                if value.text == 'Cancel ❌':
                    await event.reply(f'Сanceled.', buttons=menu)
                    return
            except exceptions.TimeoutError:
                await conv.send_message(f"Time's up...", buttons=menu)

        await gs_main.add_new_expenditure(value.text)
        await event.reply(f'Added.', buttons=menu)


client.start(bot_token=config.BOT_TOKEN)
client.run_until_disconnected()