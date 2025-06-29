import discord
from discord.ext import commands
from config import token
from ai import meslek_oner,meslek_aciklama
from personality import sorular, en_baskin_ozellik
from data import DataBase
import os
import secrets

db = DataBase()

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
            await dm.send(f"**{s['soru']}**\n a) {s['secenekler']['a']}\n b) {s['secenekler']['b']}")

            def check(m):
                return m.author == ctx.author and m.channel == dm and m.content.lower() in ["a", "b"]

            mesaj = await bot.wait_for("message", check=check)
            cevaplar.append(s["secenekler"][mesaj.content.lower()])

        ozellikler = en_baskin_ozellik(cevaplar)
        await dm.send(f"🔍 Kişilik özelliklerin: {', '.join(ozellikler)}")

        aciklama = await meslek_oner(ozellikler)
        await dm.send(f"🎯 Meslek önerisi:\n{aciklama}")

        eski = db.getir(str(ctx.author.id))
        if eski:
            await dm.send(f"📂 Daha önce analiz yapmışsın!\n🧠 Özellikler: {eski[2]}\n🎯 Meslek: {eski[3]}\n📅 Tarih: {eski[4]}")

        db.kaydet(str(ctx.author.id), cevaplar, ozellikler, aciklama)

    except Exception as e:
        await ctx.author.send(f"❌ Bir hata oluştu:\n{e}")

@bot.command()
async def meslek(ctx, *, meslek_adi: str):
    try:
        await ctx.message.delete()
        dm = await ctx.author.create_dm()
        await dm.send(f"📌 **{meslek_adi}** hakkında bilgi getiriliyor...")

        aciklama = await meslek_aciklama(meslek_adi=meslek_adi)

        if len(aciklama) <= 2000:
            await dm.send(f"📖 {meslek_adi.upper()} hakkında bilgi:\n{aciklama}")
        else:
            for i in range(0, len(aciklama), 1990):
                await dm.send(aciklama[i:i+1990])

    except Exception as e:
        await ctx.author.send(f"❌ Bir hata oluştu:\n{e}")

# Kelime listeleri
kelimeler = {
    "meme": ["iş", "job", "işler", "işlerim", "işim", "işe"],
    "invisible": ["görünmez", "invisible", "gorunmez", "snake", "solid snake"],
    "invincible": ["invincible", "yok edilemez", "ölümsüz", "sundowner"]
}

@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    for klasor, anahtarlar in kelimeler.items():
        if any(kelime in content for kelime in anahtarlar):
            try:
                dosya = secrets.choice(os.listdir(klasor))
                with open(os.path.join(klasor, dosya), "rb") as f:
                    await message.channel.send(file=discord.File(f))
            except Exception as e:
                print(f"❌ Meme gönderilemedi: {e}")
            break

bot.run(token)
