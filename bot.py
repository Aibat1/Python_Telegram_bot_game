import sqlite3
from aiogram import Bot, Dispatcher, types, executor
from config import tok
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from DBase import *
import random
from random import randint
import time
from time import sleep

storage = MemoryStorage()

bot = Bot(token=tok)
dp = Dispatcher(bot, storage=storage)

helper = 1689403986

db = sqlite3.connect('DBases.db')
sql = db.cursor()

async def notification(dp: Dispatcher):
    await bot.send_message(chat_id=helper, text="Бот успешно запущен")

class UserState(StatesGroup):
    start = State()
    imena = State()
    game = State()
    developer = State()
    rename = State()
    add_xp = State()
    add_lvl = State()
    add_money = State()
    fight = State()
    search = State()
    select_button = State()

def user_add(user_id: int):
    sql.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    if sql.fetchone() is None:
        sql.execute("INSERT INTO users VALUES (?, ?, ?)", (user_id, 0, 0))
        db.commit()

def user_info(user_id: int):
    global name
    name = sql.execute(f"SELECT nick FROM users WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    players = sql.execute(f"SELECT players FROM users WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    return name

def CreatePerson(user_id: int):
    sql.execute(f"SELECT user_id FROM person WHERE user_id = '{user_id}'")
    if sql.fetchone() is None:
        sql.execute("INSERT INTO person VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_id, 1, 100, 100, 500, 20, 10, 0, 100, 5, 5, 0))
        db.commit()

def person_info(user_id: int):
    global level,hp,max_hp,money,attack,magic_attack,xp,max_xp,armor,magic_armor,location_id
    level = sql.execute(f"SELECT level FROM person WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    hp = sql.execute(f"SELECT hp FROM person WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    max_hp = sql.execute(f"SELECT max_hp FROM person WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    money = sql.execute(f"SELECT money FROM person WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    attack = sql.execute(f"SELECT attack FROM person WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    magic_attack = sql.execute(f"SELECT magic_attack FROM person WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    xp = sql.execute(f"SELECT xp FROM person WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    max_xp = sql.execute(f"SELECT max_xp FROM person WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    armor = sql.execute(f"SELECT armor FROM person WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    magic_armor = sql.execute(f"SELECT magic_armor FROM person WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    location_id = sql.execute(f"SELECT location_id FROM person WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    return level,hp,max_hp,money,attack,magic_attack,xp,max_xp,armor,magic_armor,location_id

def CreateMob(user_id: int):
    sql.execute(f"SELECT user_id FROM mob WHERE user_id = '{user_id}'")
    if sql.fetchone() is None:
        sql.execute("INSERT INTO mob VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_id, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        db.commit()
        q = randint(1, 3)
        if q == 1:
            mob_id = 1
            mob = "Кабан"
            hp = 60
            max_hp = 60
            lvl = 1
            p_attack = 25
            m_attack = 1
            armor = 3
            m_armor = 0
            sql.execute(f"UPDATE mob SET mob_id == '{mob_id}', mob == '{mob}', hp_mob == '{hp}', max_hp == '{max_hp}', reg_level == '{lvl}', phisik_attack == '{p_attack}', magic_attack == '{m_attack}', armor == '{armor}', magick_armor == '{m_armor}' WHERE user_id = '{user_id}'")
            db.commit()
        if q == 2:
            mob_id = 2
            mob = "Змей"
            hp = 35
            max_hp = 35
            lvl = 1
            p_attack = 40
            m_attack = 7
            armor = 1
            m_armor = 5
            sql.execute(f"UPDATE mob SET mob_id == '{mob_id}', mob == '{mob}', hp == '{hp}', max_hp == '{max_hp}', reg_level == '{lvl}', phisik_attack == '{p_attack}', magic_attack == '{m_attack}', armor == '{armor}', magick_armor == '{m_armor}' WHERE user_id = '{user_id}'")
            db.commit()
        if q == 3:
            mob_id = 3
            mob = "Гоблин"
            hp = 70
            max_hp = 70
            lvl = 1
            p_attack = 30
            m_attack = 15
            armor = 10
            m_armor = 5
            sql.execute(f"UPDATE mob SET mob_id == '{mob_id}', mob == '{mob}', hp == '{hp}', max_hp == '{max_hp}', reg_level == '{lvl}', phisik_attack == '{p_attack}', magic_attack == '{m_attack}', armor == '{armor}', magick_armor == '{m_armor}' WHERE user_id = '{user_id}'")
            db.commit()

def mob_info(user_id: int):
    global mob_id,mob,hp,max_hp,reg_level,phisik_attack,magic_attack,armor,magic_armor
    mob_id = sql.execute(f"SELECT mob_id FROM mob WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    mob = sql.execute(f"SELECT mob FROM mob WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    hp_mob = sql.execute(f"SELECT hp FROM mob_mob WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    max_hp = sql.execute(f"SELECT max_hp FROM mob WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    reg_level = sql.execute(f"SELECT reg_level FROM mob WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    phisik_attack = sql.execute(f"SELECT phisik_attack FROM mob WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    magic_attack = sql.execute(f"SELECT magic_attack FROM mob WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    armor = sql.execute(f"SELECT armor FROM mob WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    magic_armor = sql.execute(f"SELECT magic_armor FROM mob WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    return mob_id,mob,hp,max_hp,reg_level,phisik_attack,magic_attack,armor,magic_armor

def CreateLocation(user_id: int):
    sql.execute(f"SELECT user_id FROM location WHERE user_id = '{user_id}'")
    if sql.fetchone() is None:
        sql.execute("INSERT INTO location VALUES (?, ?, ?, ?)", (user_id, 0, 0, "Стратовый город"))
        db.commit()

def location_info(user_id: int):
    global lock_x,lock_y,location_name
    lock_x = sql.execute(f"SELECT lock_x FROM location WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    lock_y = sql.execute(f"SELECT lock_y FROM location WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    location_name = sql.execute(f"SELECT location_name FROM location WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    return lock_x,lock_y,location_name

def CreateItem(user_id: int):
    sql.execute(f"SELECT user_id FROM items WHERE user_id = '{user_id}'")
    if sql.fetchone() is None:
        sql.execute("INSERT INTO items VALUES ()", (user_id, 0, 0, 0, "Пусто", 0, 0, 0, 0, 0, 0, 0))
        db.commit()
        q = randint(1, 3)
        if q == 1:
            item_id = 1
            cost = 300
            cost_sale = 120
            item_type = "Меч рыцаря"
            item_hp = 10
            item_mana = 10
            item_attack = 30
            item_MagikAttack = 20
            item_armor = 5
            item_MagikArmor = 5
            reg_level = 1
            sql.execute(f"UPDATE items SET item_id == '{item_id}', cost == '{cost}', cost_sale == '{cost_sale}', item_type == '{item_type}', item_hp == '{item_hp}', item_mana == '{item_mana}', item_attack == '{item_attack}', item_MagikAttack == '{item_MagikAttack}', item_armor == '{item_armor}', item_MagikArmor == '{item_MagikArmor}', reg_level == '{reg_level}' WHERE user_id = '{user_id}'")
            db.commit()
        elif q == 2:
            item_id = 2
            cost = 550
            cost_sale = 320
            item_type = "Посох архимага"
            item_hp = 40
            item_mana = 57
            item_attack = 60
            item_MagikAttack = 70
            item_armor = 30
            item_MagikArmor = 55
            reg_level = 3
            sql.execute(f"UPDATE items SET item_id == '{item_id}', cost == '{cost}', cost_sale == '{cost_sale}', item_type == '{item_type}', item_hp == '{item_hp}', item_mana == '{item_mana}', item_attack == '{item_attack}', item_MagikAttack == '{item_MagikAttack}', item_armor == '{item_armor}', item_MagikArmor == '{item_MagikArmor}', reg_level == '{reg_level}' WHERE user_id = '{user_id}'")
            db.commit()
        elif q == 3:
            item_id = 3
            cost = 1500
            cost_sale = 1000
            item_type = "опье грамовержца"
            item_hp = 170
            item_mana = 100
            item_attack = 210
            item_MagikAttack = 170
            item_armor = 92
            item_MagikArmor = 97
            reg_level = 5
            sql.execute(f"UPDATE items SET item_id == '{item_id}', cost == '{cost}', cost_sale == '{cost_sale}', item_type == '{item_type}', item_hp == '{item_hp}', item_mana == '{item_mana}', item_attack == '{item_attack}', item_MagikAttack == '{item_MagikAttack}', item_armor == '{item_armor}', item_MagikArmor == '{item_MagikArmor}', reg_level == '{reg_level}' WHERE user_id = '{user_id}'")
            db.commit()

def proverkaNick(user_id: int, nick: str):
    global a
    try:
        nick = nick
        print('DJN ' + str(nick))
        a = 0
        result = sql.execute(f"SELECT nick FROM users WHERE nick = '{nick}'").fetchone()
        db.commit()
        print(result)
        for i in result:
            if i == nick:
                a += 1
                print('add no nick')
            else:
                pass
            return a
    except Exception as e:
        pass

def item_info(user_id: int):
    global item_type,cost,cost_sale,item_hp,item_mana,item_attack,item_MagikAttack,item_armor,item_MagikArmor,reg_level
    item_type = sql.execute(f"SELECT item_type FROM items WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    cost = sql.execute(f"SELECT cost FROM items WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    cost_sale = sql.execute(f"SELECT cost_sale FROM items WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    item_hp = sql.execute(f"SELECT item_hp FROM items WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    item_mana = sql.execute(f"SELECT item_mana FROM items WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    item_attack = sql.execute(f"SELECT item_attack FROM items WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    item_MagikAttack = sql.execute(f"SELECT item_MagikAttack FROM items WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    item_armor = sql.execute(f"SELECT item_armor FROM items WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    item_MagikArmor = sql.execute(f"SELECT item_MagikArmor FROM items WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    reg_level = sql.execute(f"SELECT reg_level FROM items WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    return item_type,cost,cost_sale,item_hp,item_mana,item_attack,item_MagikAttack,item_armor,item_MagikArmor,reg_level

def CreateDvTable(user_id: int):
    sql.execute(f"SELECT user_id FROM developer_mode WHERE user_id = '{user_id}'")
    if sql.fetchone() is None:
        sql.execute("INSERT INTO developer_mode VALUES (?, ?)", (user_id, 0))
        db.commit()

def dev_info(user_id: int):
    global shop
    shop = sql.execute(f"SELECT shop FROM developer_mode WHERE user_id = '{user_id}'").fetchone()[0]
    db.commit()
    return shop

def rating(user_id: int):
    global text
    sql.execute(f"SELECT user_id, level FROM person ORDER BY level DESC")
    data = sql.fetchall()
    text = f"Рейтинг тоа 10 игроков по уровню: \n"
    for values, item in enumerate(data):
        values += 1
        sql.execute(f"SELECT nick FROM users WHERE user_id = '{item[0]}'")
        if values <= 10:
            text += f"{values}) {sql.fetchall()[0][0]} уровень {item[1]}"
        elif values > 10:
            pass
    return text

def lvl_ups(user_id: int):
    data = sql.execute(f"SELECT xp, level, hp, max_hp, attack, magic_attack FROM person WHERE user_id = '{user_id}'").fetchall()[0]
    db.commit()
    for xp,max_xp,level,hp,max_hp,attack,magic_attack in data:
        if exp >= max_xp:
            xp -= max_xp
            max_xp += 100
            hp += 50
            max_hp += 50
            level += 1
            attack += 10
            magic_attack += 10
            sql.execute(f"UPDATE person SET xp == '{xp}', max_xp == '{max_xp}', hp == '{hp}', max_hp == '{max_hp}', level == '{level}', attack == '{attack}', magic_attack == '{magic_attack}' WHERE user_id = '{user_id}'")
            db.commit()
        else:
            break



@dp.message_handler(commands=['start'], state=None)
async def start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if message.text.lower() == '/start':
        sql.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
        if sql.fetchone() is None:
            await message.answer('Приветствую тебя игрок, пожалуйста назови мне свое имя...')
            user_add(user_id=user_id)
            await UserState.imena.set()
        else:
            rating(user_id=user_id)
            await message.answer(text)
            pass

@dp.message_handler(content_types=['text'], state=UserState.imena)
async def user_name(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text
    proverkaNick(user_id=user_id, nick=text)
    if a == 0:
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn = KeyboardButton("Далее")
        markup.add(btn)
        await message.answer(f'Приветствую тебя {text}', reply_markup=markup)
        sql.execute(f"UPDATE users SET nick == '{text}' WHERE user_id = '{user_id}'")
        db.commit()
        await UserState.game.set()
    elif a == 1:
        await message.answer('Увы такое имя пользователя уже используется придумайте другой...')

@dp.message_handler(content_types=['text'], state=UserState.game)
async def games(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    CreatePerson(user_id=user_id)
    CreateLocation(user_id=user_id)
    if message.text.lower() == 'далее':
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn = KeyboardButton("Персонаж")
        btn1 = KeyboardButton("Магазин")
        btn2 = KeyboardButton("В бой")
        btn3 = KeyboardButton("Меню разработчика")
        markup.add(btn2, btn, btn1, btn3)
        await message.answer('Добро пожаловвать в игру...', reply_markup=markup)
        await UserState.select_button.set()

@dp.message_handler(content_types=['text'], state=UserState.select_button)
async def selected_button(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_info(user_id=user_id)
    person_info(user_id=user_id)
    location_info(user_id=user_id)
    if message.text.lower() == "персонаж":
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn = KeyboardButton("Назад")
        markup.add(btn)
        await message.answer(f'{name} Ваш персонаж:\n\nLevel:{level}\nXp: {xp}/{max_xp}\nHp: {hp}/{max_hp}\nAttack: {attack}\nMagic: {magic_attack}\nArmor: {armor}\nMagic Armor: {magic_armor}\nLocation: {location_name}', reply_markup=markup)
        await UserState.developer.set()
    elif message.text.lower() == 'меню разработчика':
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        btn = KeyboardButton("Добавить денег")
        btn1 = KeyboardButton("Level up")
        btn2 = KeyboardButton("Добавить опыта")
        btn3 = KeyboardButton("Напасть на монстра")
        btn4 = KeyboardButton("Сменить имя")
        btn5 = KeyboardButton("Бесконечное хп")
        btn6 = KeyboardButton("Бесконечная мана")
        btn7 = KeyboardButton("Бесплатный магазин")
        btn8 = KeyboardButton("Назад")
        markup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        await message.answer('Вы в меню разработчика...', reply_markup=markup)
        await UserState.developer.set()
    elif message.text.lower() == 'магазин':
        await message.answer('В разработке...')
    elif message.text.lower() == 'в бой':
        await message.answer('В разработке...')

@dp.message_handler(content_types=['text'], state=UserState.developer)
async def dev(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if message.text.lower() == 'добавить денег':
        await message.answer('Введите кол-во сколько хотите добавить денег...', reply_markup=ReplyKeyboardRemove())
        await UserState.add_money.set()
    elif message.text.lower() == 'level up':
        await message.answer('Введите на какой уровень хотите себе поставить...', reply_markup=ReplyKeyboardRemove())
        await UserState.add_lvl.set()
    elif message.text.lower() == 'добавить опыта':
        await message.answer('Ввкдите сколько хотите добавить опыта...', reply_markup=ReplyKeyboardRemove())
        await UserState.add_xp.set()
    elif message.text.lower() == 'напасть на монстра':
        await message.answer('Идет поиск монстров...', reply_markup=ReplyKeyboardRemove())
        await asyncio.sleep(3)
        CreateMob(user_id=user_id)
        mob_info(user_id=user_id)
        user_info(user_id=user_id)
        if reg_level == level:
            markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn = KeyboardButton("Удар")
            markup.add(btn)
            await message.answer(f'Обнаружен монстр: {mob}\nHP: {hp}/{max_hp}', reply_markup=markup)
            await UserState.fight.set()
        else:
            markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn = KeyboardButton("Напасть на монстра")
            btn1 = KeyboardButton("Назад") 
            markup.add(btn, btn1)
            await message.answer('Монстры не обнаружены, хотите продолжить поиски?', reply_markup=markup)
            await UserState.search.set()
    elif message.text.lower() == 'сменить имя':
        await message.answer('Ввкдите имя которое хотите установить...', reply_markup=ReplyKeyboardRemove())
        await UserState.rename.set()
    elif message.text.lower() == 'бесконечное хп':
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn = KeyboardButton("Персонаж")
        btn1 = KeyboardButton("Магазин")
        btn2 = KeyboardButton("В бой")
        btn3 = KeyboardButton("Меню разработчика")
        markup.add(btn2, btn, btn1, btn3)
        await message.answer('Ваше хп стало бесконечным...', reply_markup=markup)
        await UserState.select_button.set()
    elif message.text.lower() == 'бесконечная мана':
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn = KeyboardButton("Персонаж")
        btn1 = KeyboardButton("Магазин")
        btn2 = KeyboardButton("В бой")
        btn3 = KeyboardButton("Меню разработчика")
        markup.add(btn2, btn, btn1, btn3)
        await message.answer('Ваша мана стала бесконечной...', reply_markup=markup)
        await UserState.select_button.set()
    elif message.text.lower() == 'бесплатный магазин':
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn = KeyboardButton("Персонаж")
        btn1 = KeyboardButton("Магазин")
        btn2 = KeyboardButton("В бой")
        btn3 = KeyboardButton("Меню разработчика")
        markup.add(btn2, btn, btn1, btn3)
        await message.answer('Магазин стал бесплатным...', reply_markup=markup)
        await UserState.select_button.set()
    elif message.text.lower() == 'назад':
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn = KeyboardButton("Персонаж")
        btn1 = KeyboardButton("Магазин")
        btn2 = KeyboardButton("В бой")
        btn3 = KeyboardButton("Меню разработчика")
        markup.add(btn2, btn, btn1, btn3)
        await message.answer('Вы вернулись в обычное меню...', reply_markup=markup)
        await UserState.select_button.set()

@dp.message_handler(content_types=['text'], state=UserState.fight)
async def fighting(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if message.text.lower() == 'удар':
        if hp > hp_mob:
            if hp_mob >= 1:
                удар = randint(5, 20)
                удар_mob = randint(1, 10)
                hp -= удар_mob
                hp_mob -= удар
                sql.execute(f"UPDATE mob SET hp_mob == '{hp_mob}' WHERE user_id = '{user_id}'")
                db.commit()
                sql.execute(f"UPDATE person SET hp == '{hp}' WHERE user_id = '{user_id}'")
                db.commit()
                await message.answer(f'Mob hp: {hp_mob}\nYour hp: {hp}/{max_hp}')
            else:
                markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn = KeyboardButton("Персонаж")
                btn1 = KeyboardButton("Магазин")
                btn2 = KeyboardButton("В бой")
                btn3 = KeyboardButton("Меню разработчика")
                markup.add(btn2, btn, btn1, btn3)
                await message.answer(f'You win mobs {mob}', reply_markup=markup)
                await UserState.select_button.set()
        else:
            markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn = KeyboardButton("Персонаж")
            btn1 = KeyboardButton("Магазин")
            btn2 = KeyboardButton("В бой")
            btn3 = KeyboardButton("Меню разработчика")
            markup.add(btn2, btn, btn1, btn3)
            await message.answer('You dead...', reply_markup=markup)
    else:
        await message.answer('Я не понимаю команды...\nПроверьте правильно ли написанна команда!')


if __name__ == "__main__":
    print("bot is started")
    executor.start_polling(dp, skip_updates=True, on_startup=notification)
