import discord
from deckImgGen import fetchDeckImage
import os

# 自分のBotのアクセストークンを設定すること
TOKEN = os.environ['DISCORD_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    print('ログイン')

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # チャットで "/ideck LOR_DECK_CODE" を検出してデッキ画像を送信する
    # e.g. /ideck CICACAYGBAAQGBIQAMAQKEZRGUCQEBQEDIOSMOQEAEAQKHIBAIDASAIEAYFACBIFBYAQEAIFAEQA
    if '/ideck' in message.content:
        _ = message.content.split(" ")
        if len(_) < 2:
            return
        deckcode = _[1]
        # print(deckcode)
        img_path = fetchDeckImage(deckcode)
        file = discord.File(img_path, filename='deck.png')
        await message.channel.send(deckcode, file=file)

client.run(TOKEN)