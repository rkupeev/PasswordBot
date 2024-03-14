from aiogram import Router #, F
from aiogram.filters import Command 
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        text=f"<b>Здравствуйте, {message.from_user.full_name}!</b>\nДобро пожаловать в Password Bot. Это удобный инструмент для генерации паролей. \n\nДля быстрого ознакомления с функционалом бота введите команду /help.\n\nДля генерации паролей введите команду /new.", 
        parse_mode=ParseMode.HTML
    )
    await state.clear()


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        text="🤖 <b>Password Bot</b> — инструмент для генерации надежных паролей на основании ваших предпочтений: вы можете указать количество паролей и их длину.\n\n⚙️ <b>Основные команды</b>:\n  1. /start – начало или возобновление работы с ботом;\n  2. /help – краткая справка;\n  3. /new – создание паролей;\n  4. /cancel – отмена процесса создания паролей.\n\nℹ️ Если возникнут какие-либо вопросы по работе бота, вы можете написать разработчику (ссылку на его профиль оставили в описании).", 
        parse_mode=ParseMode.HTML
    )

