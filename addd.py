import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("뭐")
    if message.content.startswith("야 뭐해"):
        await message.channel.send("나 디스코드 대화")
    if message.content.startswith("잘생김?"):
        await message.channel.send("니보단 잘생김")
    if message.content.startswith("너 현피뜨자"):
        await message.channel.send("나한테 살작 맞아도 뼈뿌려지는 약한애가")
    if message.content.startswith("사람이야?"):
        await message.channel.send("들켰네 튀자")
    if message.content.startswith("야 노래해줘"):
        await message.channel.send("니가알아서 노래 부르던지 노래듣던지 혀!!")
    if message.content.startswith("너 아이큐 몆?"):
        await message.channel.send("279960IQ야")
    if message.content.startswith("민든지"):
        await message.channel.send("오타쓰면 미래에 니 봇됨")
    if message.content.startswith("러랔"):
        await message.channel.send("경고야 한 번더 하면 닌 나랑 현피떠 ^^")


access_token - os.environ["BOT_TOKEN"]       
client.run(access_token)
