from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
#from aiogram.dispatcher.filters import Text, IDFilter

async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    name = f"{message.from_user.first_name}"
    userid = f"{message.from_user.id}"
    await message.answer(
        "Hello, " + name +". Ur ID:" + userid ,
        reply_markup=types.ReplyKeyboardRemove()
    )

async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Cancel", reply_markup=types.ReplyKeyboardRemove())

def register_handlers_common(dp: Dispatcher, admin_id: int):
    dp.register_message_handler(cmd_start, commands="start", state="*")

