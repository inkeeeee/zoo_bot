import random
from utils import get_share_keyboard, get_finish_keyboard
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router, types, F, Bot
from aiogram.types import Message
from animals import animal_list, animals_photo, animals
from token_data import TOKEN, bot_link
from contact_data import admin_id, admin_tag


quiz_router = Router()
bot = Bot(TOKEN)


class Questions(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
    q6 = State()
    q7 = State()
    finish = State()


@quiz_router.message(F.text == 'Пройти викторину')
async def start_quiz(message: Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,text=
        'Давайте как можно скорее узнаем ваше тотемное животное! Для это нужно пройти небольшую викторину, состоящую из *7 вопросов*',
        parse_mode='Markdown')
    kb = [[types.KeyboardButton(text='На суше'), types.KeyboardButton(text='В воде'),
           types.KeyboardButton(text='В небе')]]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboard=True
    )
    await message.answer('Начинаем! *Вопрос №1*\n\nГде вы предпочитаете находиться?', parse_mode='Markdown',
                         reply_markup=keyboard)
    await state.set_state(Questions.q1.state)


@quiz_router.message(Questions.q1)
async def get_q2(message: Message, state: FSMContext):
    result = {animal: 0 for animal in animal_list}
    key, value = 'место', message.text.lower()
    for animal in animal_list:
        if animals[animal][key] == value:
            result[animal] += 1

    await state.set_data({'result': result, 'questions': {key: value}})
    kb = [[types.KeyboardButton(text='Салат'), types.KeyboardButton(text='Орехи'), types.KeyboardButton(text='Мясо'),
           types.KeyboardButton(text='Фрукты')]]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboard=True
    )

    await message.answer('*Вопрос №2*\n\nВаша любимая еда?', parse_mode='Markdown',
                         reply_markup=keyboard)
    await state.set_state(Questions.q2.state)


@quiz_router.message(Questions.q2)
async def get_q3(message: Message, state: FSMContext):
    state_data = await state.get_data()
    result, questions = state_data['result'], state_data['questions']
    key, value = 'еда', message.text.lower()
    questions[key] = value
    for animal in animal_list:
        if animals[animal][key] == value:
            result[animal] += 1

    await state.set_data({'result': result, 'questions': questions})

    kb = [[types.KeyboardButton(text='Да'), types.KeyboardButton(text='Нет')]]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboard=True
    )

    await message.answer('*Вопрос №3*\n\nВы любите плавать?', parse_mode='Markdown',
                         reply_markup=keyboard)
    await state.set_state(Questions.q3.state)


@quiz_router.message(Questions.q3)
async def get_q4(message: Message, state: FSMContext):
    state_data = await state.get_data()
    result, questions = state_data['result'], state_data['questions']
    key, value = 'любит плавать', message.text.lower()
    questions[key] = value
    for animal in animal_list:
        if animals[animal][key] == value:
            result[animal] += 1

    await state.set_data({'result': result, 'questions': questions})
    kb = [[types.KeyboardButton(text='Экстраверт'), types.KeyboardButton(text='Интроверт')]]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboard=True
    )

    await message.answer('*Вопрос №4*\n\nВы экстраверт или интроверт?', parse_mode='Markdown',
                         reply_markup=keyboard)
    await state.set_state(Questions.q4.state)


@quiz_router.message(Questions.q4)
async def get_q5(message: Message, state: FSMContext):
    state_data = await state.get_data()
    result, questions = state_data['result'], state_data['questions']
    key, value = 'личность', message.text.lower()
    questions[key] = value
    for animal in animal_list:
        if animals[animal][key] == value:
            result[animal] += 1

    await state.set_data({'result': result, 'questions': questions})

    kb = [[types.KeyboardButton(text='Да'), types.KeyboardButton(text='Нет')]]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboard=True
    )

    await message.answer('*Вопрос №5*\n\nВам нравится носить яркую одежду?', parse_mode='Markdown',
                         reply_markup=keyboard)
    await state.set_state(Questions.q5.state)


@quiz_router.message(Questions.q5)
async def get_q6(message: Message, state: FSMContext):
    state_data = await state.get_data()
    result, questions = state_data['result'], state_data['questions']
    key, value = 'яркая одежда', message.text.lower()
    questions[key] = value
    for animal in animal_list:
        if animals[animal][key] == value:
            result[animal] += 1

    await state.set_data({'result': result, 'questions': questions})
    kb = [[types.KeyboardButton(text='Да'), types.KeyboardButton(text='Нет')]]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboard=True
    )

    await message.answer('*Вопрос №6*\n\nВы ведете активный образ жизни?', parse_mode='Markdown',
                         reply_markup=keyboard)
    await state.set_state(Questions.q6.state)


@quiz_router.message(Questions.q6)
async def get_q7(message: Message, state: FSMContext):
    state_data = await state.get_data()
    result, questions = state_data['result'], state_data['questions']
    key, value = 'активный образ жизни', message.text.lower()
    questions[key] = value
    for animal in animal_list:
        if animals[animal][key] == value:
            result[animal] += 1

    await state.set_data({'result': result, 'questions': questions})
    kb = [[types.KeyboardButton(text='Да'), types.KeyboardButton(text='Нет')]]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboard=True
    )

    await message.answer('*Вопрос №7*\n\nВы разговорчивый человек?', parse_mode='Markdown',
                         reply_markup=keyboard)
    await state.set_state(Questions.q7.state)


@quiz_router.message(Questions.q7)
async def get_result(message: Message, state: FSMContext):
    state_data = await state.get_data()
    result, questions = state_data['result'], state_data['questions']
    key, value = 'разговорчивый', message.text.lower()
    questions[key] = value
    your_animal = ('', 0)
    for animal in animal_list:
        if animals[animal][key] == value:
            result[animal] += 1
        if result[animal] > your_animal[1]:
            your_animal = (animal, result[animal])
    if your_animal[0] == '':
        your_animal = (random.choice(animal_list), 0)

    keyboard = get_finish_keyboard()
    await bot.send_photo(message.chat.id, caption=f'Поздравляем!!! Ваше тотемное животное - {your_animal[0]}',
                         photo=animals_photo[your_animal[0]], reply_markup=keyboard.as_markup())

    await state.set_state(Questions.finish.state)
    await state.set_data({'users_animal': your_animal[0]})


@quiz_router.message(F.text == 'Попробовать ещё раз')
async def try_again(message: Message, state: FSMContext):
    await start_quiz(message, state)


@quiz_router.message(F.text == 'Связаться с сотрудником')
async def contact(message: Message, state: FSMContext):
    username = f'@{message.from_user.username}'
    state_data = (await state.get_data())
    await message.answer(f'Вы можете связаться с сотрудником зоопарка для уточнения важных моментов: {admin_tag}')

    if 'users_animal' in state_data:
        result = state_data['users_animal']
        await bot.send_message(chat_id=admin_id,
                               text=f'Вскоре с вами свяжется пользователь {username}, результат прохождения викторины: {result}')
    else:
        await bot.send_message(chat_id=admin_id,
                               text=f'Вскоре с вами свяжется пользователь {username}, который не проходил викторину')


@quiz_router.message(F.text == 'Поделиться результатом')
async def share(message: Message, state: FSMContext):
    state_data = await state.get_data()
    if state_data is None:
        await message.answer(
            'Вы еще не прошли викторину, чтобы поделиться результатом :(\n\nДля запуска викторины напишите: /quiz')
        return

    else:
        repost = f'Моё тотемное животное - {state_data["users_animal"]}. Предлагаю вам тоже пройти викторину от Московского зоопарка!!!'
        keyboard = get_share_keyboard(repost, bot_link)

        await message.answer(text='Выберете в какой соцсети вы хотите поделиться', reply_markup=keyboard.as_markup())
