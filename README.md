# MEERKATBOT LIBRARY
> It is an extra layer to discord.py library, writen to improve the discord bots architecture.


# A Simple Example

```python


from meerkatbot import MeerkatBot

token = input('YOUR DISCORD BOT TOKEN IS ... ')

meerkat = MeerkatBot(
    token=token,
    prefix="@",
    # * The meerkat has a logger as well, but you can send
    # * a custom one to MeerkatBot instance -> logger = logger(color, text): void
    #logger=lambda color, text: print(text)
)

# * Example - Commands


async def helloCommand(context):
    await context.send('Hi!, how are you?')


async def byeCommand(context):
    await context.send('See you!')

# * Example - EVENTS


async def onReadyEvent():
    meerkat.logger('bold', 'IT IS READY')


async def onMessageEvent(message):
    meerkat.logger('warning', 'MESSAGE - {}'.format(message.content))

# ? Two ways to do the same
# meerkat.use('hello', helloCommand).use('bye', byeCommand)
meerkat.bulkUse([
    ('hello', helloCommand),
    ('bye', byeCommand)
])

# ? Two ways to do the same
# meerkat.on('ready', onReadyEvent).on('message', onMessageEvent)
meerkat.bulkOn([
    ('ready', onReadyEvent),
    ('message', onMessageEvent)
])

# * With this command, the meerkat can start digging!
meerkat.run()

```