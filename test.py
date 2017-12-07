# Diese Datei ist für den Schwesterbot der Pixeldrohne, PixelDev gedacht.

import discord
import sys
import asyncio
import keys

client = discord.Client()


@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')
    await client.change_presence(game=discord.Game(name='mit p.help', type=1))


@client.event
async def on_message(message):
    # Hilfe für Dev-Branch und Cutting Edge
    if message.content.lower().startswith('p.help test'):
        user = message.author
        embed = discord.Embed(
            title="Kategorie: Test",
            description="Alle Befehle in dieser Kategorie müssen noch getestet werden und können auch nur auf dem Heimat-/"
                        "Testserver genutzt werden. Um viele dieser Befehle nutzen zu können, ist der Schwesterbot PixelDev"
                        "nötig. Die Befehle habe Tags:\n[Alpha] Cutting Edge\n[Beta] Early Access"
        )
        await client.send_message(user, embed=embed)

    if message.content.lower().startswith('dev.halt') and (message.author.id == keys.pmcid or message.author.id == keys.m3lid):
        await client.logout()
        await asyncio.sleep(1)
        await sys.exit(1)

client.run(keys.dev)
