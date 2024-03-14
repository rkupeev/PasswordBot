from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.enums import ParseMode

from random import choice

router = Router()


class CreatePasswords(StatesGroup):
    quantity = State()
    lenght = State()



def generation(lenght):
    chars = "123456789abcdefghjkmnpqrstuvwxyzABCDEFGHIJKMNPQRSTUVWXYZ"
    return ''.join(choice(chars) for _ in range(lenght))



@router.message(StateFilter(None), Command('new'))
async def new_password(message: Message, state: FSMContext):
    await message.answer(
        text="💭 Для начала генерации надо определить, сколько паролей необходимо сгенерировать и какой длины они будут.")

    await message.answer(
        text="Введите количество паролей, которые необходимо сгенерировать (макс. количество — 20). Для отмены генерации введите команду /cancel."
    )
    await state.set_state(CreatePasswords.quantity)


#quantity
@router.message(CreatePasswords.quantity, 
                lambda message: message.text.isdigit() and int(message.text) in range(1, 21))
async def lenght(message: Message, state: FSMContext):
    await state.update_data(quantity=message.text)
    await message.answer("✅ Готово, теперь введите длину каждого пароля (она должна быть не меньше 6 символов и не больше 25).")
    await state.set_state(CreatePasswords.lenght)


#lenght
@router.message(CreatePasswords.lenght, 
                lambda message: message.text.isdigit() and int(message.text) in range(6, 26))
async def lenght(message: Message, state: FSMContext):
    await state.update_data(lenght=message.text)
    user_data = await state.get_data()

    for _ in range(int(user_data["quantity"])):
        await message.answer(
            text=f'`{generation(int(user_data["lenght"]))}`',
            parse_mode=ParseMode.MARKDOWN_V2
            )
    await message.answer(f"✅ Паролей сгенерировано: {user_data['quantity']}")
    await state.clear()



#cancel handlers
@router.message(CreatePasswords.lenght, Command("cancel"))
@router.message(CreatePasswords.quantity, Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("❌ Вы отменили процесс генерации паролей.")


@router.message(StateFilter(None), Command("cancel"))
async def cmd_cancel_no_state(message: Message, state: FSMContext):
    await state.set_data({}) #data reset
    await message.answer(
        text="⚙️ Данная команда работает только в процессе генерации пароля...")


#incorrect-handlers
@router.message(CreatePasswords.quantity)
async def quantity_incorrect(message: Message):
    if not message.text.isdigit():
        await message.answer('⚠️ Введите целое положительное число.')
    elif message.text.isdigit() and int(message.text) == 0:
        await message.answer('⚠️ Ошибка. Нужно сгенерировать хотя бы один пароль. Повторите попытку...')
    elif message.text.isdigit() and int(message.text) not in range(1, 21):
        await message.answer('⚠️ Количество запрашиваемых паролей не соответствует необходимым критериям. Повторите попытку...')
    

@router.message(CreatePasswords.lenght)
async def lenght_incorrect(message: Message):
    if message.text.isdigit() and int(message.text) not in range(6, 26):
        await message.answer('⚠️ Длина паролей не соответствует необходимым критериям. Повторите попытку...')

    elif not message.text.isdigit():
        await message.answer('⚠️ Введите целое положительное число.')

   


    



