import disnake
from disnake.ext import commands
import datetime

# Внутри команды, прослушивателя событий и т.д.
embed = disnake.Embed(
    title="Заголовок эмбеда",
    description="Описание эмбеда",
    color=disnake.Colour.yellow(),
    timestamp=datetime.datetime.now(),
)

embed.set_author(
    name="Автор эмбеда",
    url="https://disnake.dev/",
    icon_url="https://disnake.dev/assets/disnake-logo.png",
)
embed.set_footer(
    text="Футер эмбеда",
    icon_url="https://disnake.dev/assets/disnake-logo.png",
)

embed.set_thumbnail(url="https://disnake.dev/assets/disnake-logo.png")
embed.set_image(url="https://disnake.dev/assets/disnake-thin-banner.png")

embed.add_field(name="Обычный заголовок", value="Обычное значение", inline=False)
embed.add_field(name="Встроенный заголовок", value="Встроенное значение", inline=True)
embed.add_field(name="Встроенный заголовок", value="Встроенное значение", inline=True)
embed.add_field(name="Встроенный заголовок", value="Встроенное значение", inline=True)

# await ctx.send(embed=embed)