from __future__ import annotations

from typing import TYPE_CHECKING

import discord
from discord.ext import commands

from .command_error import CommandErrors
from .command_logs import CommandLogs
from .tasks import Tasks
from .auto_download import AutoDownload
if TYPE_CHECKING:
    from core import Fishie


class Events(CommandErrors, CommandLogs, Tasks, AutoDownload):
    emoji = discord.PartialEmoji(name="\U0001f3a7")

    def __init__(self, bot: Fishie):
        super().__init__()
        self.bot = bot
        self.cd_mapping = commands.CooldownMapping.from_cooldown(
            1, 5, commands.BucketType.member
        )


async def setup(bot: Fishie):
    await bot.add_cog(Events(bot))