
from aiogram.types import Message
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.choose_auth import menu_editors

from keyboards.default.choose_auth import uzb_editors, arab_editors
from loader import dp, bot
from states.editors import ShayxMSMY, ShayxMansur, QuranLa, Jalaladdinalmah
from utils.producer import Send_message
from utils.quran_api import MSMYeditor, AlouddinMeditor, Quran_la, Jalaliddin

@dp.message_handler(text="🇺🇿 Uzbek editors")
async def services_info(message: Message):
    await message.answer(text = "Choose uzbek editors", reply_markup=uzb_editors)


@dp.message_handler(text="Shayx Muhammad Sodiq Muhammad Yusuf")
async def MSMY_text(message: Message):
    await message.answer(text = "Enter number of the chapter (1 - 114)")
    await ShayxMSMY.chapter.set()

@dp.message_handler(state=ShayxMSMY.chapter)
async def MSMY_chapter(message: types.Message, state: FSMContext):
    try:
        if int(message.text) > 0 and int(message.text) < 115:
            global CHAPTER
            CHAPTER = str(message.text)
            await message.answer("Please enter the number of verse")
            await ShayxMSMY.verse.set()
        else:
            await message.answer("Enter the number between 1 and 114")
    except:
        await message.answer("Incorrect message. Please enter the number. Try again")
        await state.finish()
        await bot.send_message(message.from_user.id, text="Select the desired button!", reply_markup=menu_editors)

@dp.message_handler(state=ShayxMSMY.verse)
async def MSMY_verse(message: types.Message, state: FSMContext):
    try:
        Verse = str(message.text)
        chapter, verse, text = MSMYeditor(CHAPTER, Verse)
        await message.answer(f"-Chapter: {chapter}\n\n-Verse: {verse}\n\n-Text: {text}")
        Send_message(chapter, verse, text, message.from_user.full_name)
        print(text)
        await state.finish()
        await bot.send_message(message.from_user.id, text="Select the desired button!", reply_markup=menu_editors)
    except:
        await message.answer("Incorrect message. Please enter the number. Try again")
        await state.finish()
        await bot.send_message(message.from_user.id, text="Select the desired button!", reply_markup=menu_editors)


#Shayx Mansur
@dp.message_handler(text="Shayx Alouddin Mansur")
async def MSMY_text(message: Message):
    await message.answer(text = "Enter number of the chapter (1 - 114)")
    await ShayxMansur.chapter.set()

@dp.message_handler(state=ShayxMansur.chapter)
async def MSMY_chapter(message: types.Message, state: FSMContext):
    try:
        if int(message.text) > 0 and int(message.text) < 115:
            global CHAPTER
            CHAPTER = str(message.text)
            await message.answer("Please enter the number of verse")
            await ShayxMansur.verse.set()
        else:
            await message.answer("Enter the number between 1 and 114")
    except:
        await message.answer("Incorrect message. Please enter the number. Try again")
        await state.finish()
        await bot.send_message(message.from_user.id, text="Select the desired button!", reply_markup=menu_editors)

@dp.message_handler(state=ShayxMansur.verse)
async def MSMY_verse(message: types.Message, state: FSMContext):
    try:
        Verse = str(message.text)
        chapter, verse, text = AlouddinMeditor(CHAPTER, Verse)
        await message.answer(f"-Chapter: {chapter}\n\n-Verse: {verse}\n\n-Text: {text}")
        Send_message(chapter, verse, text, message.from_user.full_name)
        await state.finish()
        await bot.send_message(message.from_user.id, text="Select the desired button!", reply_markup=menu_editors)
    except:
        await message.answer("Incorrect message. Please enter the number. Try again")
        await state.finish()
        await bot.send_message(message.from_user.id, text="Select the desired button!", reply_markup=menu_editors)


# Arabic editors
@dp.message_handler(text="🇸🇦 Arabic editors")
async def services_info(message: Message):
    await message.answer(text = "Choose arabic editors", reply_markup=arab_editors)


@dp.message_handler(text="Quran-la (en)")
async def QuranLA_text(message: Message):
    await message.answer(text = "Enter number of the chapter (1 - 114)")
    await QuranLa.chapter.set()

@dp.message_handler(state=QuranLa.chapter)
async def QuranLA_chapter(message: types.Message, state: FSMContext):
    try:
        if int(message.text) > 0 and int(message.text) < 115:
            global CHAPTERQ
            CHAPTERQ = str(message.text)
            await message.answer("Please enter the number of verse")
            await QuranLa.verse.set()
        else:
            await message.answer("Enter the number between 1 and 114")
    except:
        await message.answer("Incorrect message. Please enter the number. Try again")
        await state.finish()
        await bot.send_message(message.from_user.id, text="Select the desired button!", reply_markup=menu_editors)

@dp.message_handler(state=QuranLa.verse)
async def Quranla_verse(message: types.Message, state: FSMContext):
    try:
        verse = str(message.text)
        chapter, verse, text = Quran_la(CHAPTERQ, verse)
        await message.answer(f"-Chapter: {chapter}\n\n-Verse: {verse}\n\n-Text: {text}")
        Send_message(chapter, verse, text, message.from_user.full_name)
        await state.finish()
        await bot.send_message(message.from_user.id, text="Select the desired button!", reply_markup=menu_editors)
    except:
        await message.answer("Incorrect message. Please enter the number. Try again")
        await state.finish()
        await bot.send_message(message.from_user.id, text="Select the desired button!", reply_markup=menu_editors)


#Shayx Jalaladdinalmah (abar)
@dp.message_handler(text="Shayx Jalaladdinalmah (abar)")
async def Jalaliddin_text(message: Message):
    await message.answer(text = "Enter number of the chapter (1 - 114)")
    await Jalaladdinalmah.chapter.set()

@dp.message_handler(state=Jalaladdinalmah.chapter)
async def Jalaliddin_chapter(message: types.Message, state: FSMContext):
    try:
        if int(message.text) > 0 and int(message.text) < 115:
            global CHAPTERJ
            CHAPTERJ = str(message.text)
            await message.answer("Please enter the number of verse")
            await Jalaladdinalmah.verse.set()
        else:
            await message.answer("Enter the number between 1 and 114")
    except:
        await message.answer("Incorrect message. Please enter the number. Try again")
        await state.finish()
        await bot.send_message(message.from_user.id, text="Select the desired button!", reply_markup=menu_editors)

@dp.message_handler(state=Jalaladdinalmah.verse)
async def Jalaliddin_verse(message: types.Message, state: FSMContext):
    try:
        Verse = str(message.text)
        chapter, verse, text = Jalaliddin(CHAPTER, Verse)
        await message.answer(f"-Chapter: {chapter}\n\n-Verse: {verse}\n\n-Text: {text}")
        Send_message(chapter, verse, text, message.from_user.full_name)
        await state.finish()
        await bot.send_message(message.from_user.id, text="Select the desired button!", reply_markup=menu_editors)
    except:
        await message.answer("Incorrect message. Please enter the number. Try again")
        await state.finish()
        await bot.send_message(message.from_user.id, text="Select the desired button!", reply_markup=menu_editors)
