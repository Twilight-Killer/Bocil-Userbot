from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta
import asyncio


from PyroUbot import*


@PY.UBOT("createpoll")
async def create_poll_cmd(client: Client, message: Message):
    try:
        command_parts = message.text.split("\n", 1)
        if len(command_parts) < 2:
            await message.reply_text("Gunakan format: .createpoll <pertanyaan>\n<option 1>\n<option 2>\n... ")
            return
        
        question = command_parts[0].split(maxsplit=1)[1]
        options = command_parts[1].split("\n")
        
        poll_id = await create_poll(message.chat.id, question, options)
        options_buttons = [
            [InlineKeyboardButton(option, callback_data=f"vote_{poll_id}_{option}")]
            for option in options
        ]
        
        await message.reply_text(
            f"Polling dibuat:\n\n<b>{question}</b>",
            reply_markup=InlineKeyboardMarkup(options_buttons)
        )
    except Exception as e:
        await message.reply_text(f"Terjadi kesalahan: {str(e)}")

@PY.UBOT("pollresult")
async def poll_result_cmd(client: Client, message: Message):
    try:
        poll_id = message.text.split(maxsplit=1)[1]
        poll = await get_poll(poll_id)
        
        if not poll:
            await message.reply_text("Polling tidak ditemukan.")
            return
        
        result_text = f"Polling: {poll['question']}\n\n"
        for option, votes in poll['options'].items():
            result_text += f"{option}: {votes} suara\n"
        
        await message.reply_text(result_text)
    except Exception as e:
        await message.reply_text(f"Terjadi kesalahan: {str(e)}")


@ubot.on_callback_query(filters.regex(r"^vote_"))
async def handle_vote(client: Client, callback_query):
    try:
        data_parts = callback_query.data.split("_")
        poll_id, option = data_parts[1], data_parts[2]
        
        await vote_poll(poll_id, option)
        
        poll = await get_poll(poll_id)
        result_text = f"Polling: {poll['question']}\n\n"
        for opt, votes in poll['options'].items():
            result_text += f"{opt}: {votes} suara\n"
        
        await callback_query.message.edit_text(result_text)
        await callback_query.answer("Terima kasih atas suaranya!")
    except Exception as e:
        await callback_query.answer(f"Terjadi kesalahan: {str(e)}")
