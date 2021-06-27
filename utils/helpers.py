import discord

     
async def quick_embed(ctx, reply=True, send=True, **kwargs):
    title = kwargs.get("title", "")
    description = kwargs.get("description", "")
    timestamp = kwargs.get("timestamp")
    color = kwargs.get("color", discord.Color.random())
    thumbnail = kwargs.get("thumbnail")
    author = kwargs.get("author")
    footer = kwargs.get("footer", {})
    fields = kwargs.get("fields")
    bimage = kwargs.get("bimage")
    image_url = kwargs.get("image_url", "")
    url = kwargs.get("url", "")


    embed = discord.Embed(title=title, description=description, color=color, url=url)
    if timestamp:
        embed.timestamp = timestamp

    file = None
    if image_url:
        embed.set_image(url=image_url)

    if thumbnail:
        embed.set_thumbnail(url=thumbnail)

    if author:
        embed.set_author(
            name=author.get("name", "\u200b"),
            url=author.get("url", ""),
            icon_url=author.get("icon_url", ""),
        )

    if footer:
        text = footer.get("text", "\u200b")
        embed.set_footer(
            text=text,
            icon_url=footer.get("icon_url", ""),
        )

    if fields:
        for f in fields:
            embed.add_field(
                name=f.get("name", "\u200b"),
                value=f.get("value", "\u200b"),
                inline=f.get("inline", True),
            )

    if send:
        if reply:
            msg = await ctx.reply(embed=embed, mention_author=False)
        else:
            msg = await ctx.send(embed=embed)

    if send:
        return msg
    else:
        return embed

