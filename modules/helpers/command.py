from typing import Union, List
from pyrogram import filters

other_filters = filters.group & ~ filters.edited & ~ filters.via_bot & ~ filters.me
other_filters2 = filters.private & ~ filters.edited & ~ filters.via_bot & ~ filters.me


def commandpro(commands: Union[str, List[str]]):
    return filters.command(commands,"")
