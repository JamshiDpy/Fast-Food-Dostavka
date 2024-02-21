from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, ChatType
from data.config import ChannelOutside


# class IsOutsideChannel(BoundFilter):
#
#     async def check(self, message: Message) -> bool:
#         result = None
#         if message.chat.id ==