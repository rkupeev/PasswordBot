from aiogram.filters import BaseFilter
from aiogram.types import Message, ContentType

class QuantityFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text.isdigit() and int(message.text) in range(1, 21)

class LenghtFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text.isdigit() and int(message.text) in range(6, 26)

