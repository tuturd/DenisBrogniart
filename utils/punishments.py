import discord
from config.values import USER_ID_ADMIN, BOT_ID, CHANNEL_ID_BOT, COLOR_RED
from utils.logging import get_logger
from utils.bot import bot
import datetime

logger = get_logger(__name__)

async def timeout(member: discord.User, **kwargs):
        if member.id not in [USER_ID_ADMIN,BOT_ID]:
            logger.info(f"fn > timeout > start | Member: {member} (id:{member.id})")
            author = kwargs.get("author", "Denis Brogniart")
            reason_arg = kwargs.get("reason", "unknown")
            reason = reason_arg if reason_arg else "unknown"
            delta = datetime.timedelta(minutes=kwargs.get("minutes",10))
            logger.info(f"fn > timeout > options | Member: {member} (id:{member.id}) | Requested by: {author} | Timedelta: {delta} | Reason: {reason}")
            await member.timeout(delta,reason=reason)
            embed=discord.Embed(title=f":robot: {member} Muted! :moyai:", description=f"by **{author}**\nbecause of **{reason}**\nfor **{delta}**", color=COLOR_RED)
            await bot.get_channel(CHANNEL_ID_BOT).send(embed=embed)
            interaction = kwargs.get("interaction",None)
            if interaction:
                await interaction.followup.send(embed=embed)
            logger.info(f"fn > timeout > OK | Member: {member} (id:{member.id})")