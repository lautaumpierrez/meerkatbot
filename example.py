from meerkatbot import MeerkatBot

token = input('YOUR DISCORD BOT TOKEN IS ... ')

meerkat = MeerkatBot(
    token=token, prefix="@"
)


async def helloCommand(context):
    await context.send('Hi!, how are you?')

meerkat.use('hello', helloCommand).run()
