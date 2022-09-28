from typing import Union, List
from pyrogram import filters
from modules.config import COMMAND_PREFIXES

other_filters = filters.group & ~ filters.edited & ~ filters.via_bot & ~ filters.me
other_filters2 = filters.private & ~ filters.edited & ~ filters.via_bot & ~ filters.me


def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)

