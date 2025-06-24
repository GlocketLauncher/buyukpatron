import discord
from discord.ext import commands
from config import token
from ai import meslek, meslek_bilgi  # meslek(ozellikler) + meslek_bilgi(meslek_adi)
from personality import sorular, en_baskin_ozellik
import random
import os
import secrets

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak başlatıldı')

@bot.command()
async def analiz(ctx):
    try:
        await ctx.message.delete()
        dm = await ctx.author.create_dm()
        await dm.send("🧠 Kişilik analizine hoş geldin! Lütfen soruları 'a' ya da 'b' olarak cevapla.")

        cevaplar = []

        for s in sorular:
            await dm.send(f"**{s['soru']}**\n a) {s['secenekler']['a']} \n b) {s['secenekler']['b']}")

            def check(m):
                return m.author == ctx.author and m.channel == dm and m.content.lower() in ["a", "b"]

            cevap = await bot.wait_for("message", check=check)
            cevaplar.append(s["secenekler"][cevap.content.lower()])

        ozellikler = en_baskin_ozellik(cevaplar)
        await dm.send(f"🔍 Kişilik özelliklerin: {', '.join(ozellikler)}")

        aciklama = await meslek(ozellikler)
        await dm.send(f"🎯 Meslek önerisi:\n{aciklama}")

    except Exception as e:
        await ctx.author.send(f"❌ Bir hata oluştu: {e}")

@bot.command()
async def meslek(ctx, *, meslek_adi: str):
    try:
        await ctx.message.delete()
        dm = await ctx.author.create_dm()
        await dm.send(f"📌 Bilgi istenen meslek: **{meslek_adi}**\n⏳ Bilgi getiriliyor...")

        aciklama = await meslek_bilgi(meslek_adi)

        if len(aciklama) <= 2000:
            await dm.send(f"📖 {meslek_adi.upper()} hakkında bilgi:\n{aciklama}")
        else:
            for i in range(0, len(aciklama), 1990):
                await dm.send(aciklama[i:i+1990])

    except Exception as e:
        await ctx.author.send(f"❌ Bir hata oluştu: {e}")


job = ["iş","job"]

@bot.listen()
async def on_message(message):
    if message.author != bot.user:
        content = message.content.lower()
        for kelime in job:
            if kelime in content:
                randomMem = secrets.choice(os.listdir('meme'))
                with open(f"meme/{randomMem}","rb") as f:
                    pic = discord.File(f)

                    await message.channel.send(file = pic)
                    break



bot.run(token)
