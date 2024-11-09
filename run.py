import asyncio
import discord
from discord import option
from config import config
from generator import generate_secret
import logging

logging.basicConfig(level=config.log_level)
logger = logging.getLogger(__name__)


bot = discord.Bot(
    description="A bot that generates secret keys for users for wiki",
    debug_guilds=config.guild_ids,
)


@bot.slash_command(
    name="request_secret",
    description="Request a secret key for wiki access",
    contexts={discord.InteractionContextType.guild},
)
@option(
    "key",
    description="Your secret key",
    input_type=str,
    required=True,
    min_length=config.key_length,
    max_length=config.key_length,
)
async def request_secret(ctx: discord.ApplicationContext, key: str):
    logger.debug(f"Requesting secret for key: {key} by {ctx.author}")
    secret = generate_secret(key, config.secret_seed)
    await ctx.interaction.response.send_message(secret, ephemeral=True)


@bot.event
async def on_ready():
    logger.info(f"Bot is ready as {bot.user}")


if __name__ == "__main__":
    bot.run(config.discord_bot_token)
