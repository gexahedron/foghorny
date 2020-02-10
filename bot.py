#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from telethon import TelegramClient, events, connection

api_id = # FIXME: use your api_id here
api_hash = # FIXME: use your api_hash here

phone = # FIXME: use your phone number here
# also, if you use 2FA, then you would need to pass it to client.start function
session_file = 'autoreplier'

# content of the automatic reply
message = "Вас приветствует gpt2-бот!"

proxy = ('proxy.digitalresistance.dog',
         443,
         'd41d8cd98f00b204e9800998ecf8427e')

if __name__ == '__main__':
    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    client = TelegramClient('autoreplier', api_id, api_hash,
        connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
        proxy=proxy,
        sequential_updates=True)

    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:  # only auto-reply to private chats
            from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
            if not from_.bot:  # don't auto-reply to bots
                print(time.asctime(), '-', event.message)  # optionally log time and message
                time.sleep(1)  # pause for 1 second to rate-limit automatic replies
                await event.respond(message)

    print(time.asctime(), '-', 'Auto-replying...')
    client.start(phone)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')

