import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from items import item
from creat import Creature
API = '5946485689:AAENFA5gQyp3YCMY5i8tjvBz2tfTIhxDU5Q'
bot = Bot(token=API)
main_char = Creature("", 5, 5, 5)
dp = Dispatcher(bot)
floor = 0
item_base = {}
enemy_base = {}
boss_base = {}
inventory = {1: item('пусто',0,0,0,0,0,0,0,0,0,0,0,0),
             2: item('пусто',0,0,0,0,0,0,0,0,0,0,0,0),
             3: item('пусто',0,0,0,0,0,0,0,0,0,0,0,0),
             4: item('пусто',0,0,0,0,0,0,0,0,0,0,0,0),
             5: item('пусто',0,0,0,0,0,0,0,0,0,0,0,0)}
def fight(main_char, enemy_char, floor):
   return
def loot(main_char, item_char):
   return
@dp.message_handler(commands=['start', 'restart'])
async def send_welcome(message: types.Message):
   floor = 0
   await message.answer("Путник, тебе следует выбираться отсюда!\nТы оказался на разделе миров,но я тебе помогу.\nЧтобы ты смог уйти, тебе не помешает выбрать то, с чем ты себя связываешь.")
   await message.answer("☼ Выберите один из трех атрибутов, для получения соответствующего бонуса к связанным характеристикам ☼\n☼ Для выбора СИЛЫ напиши /strength ☼\n☼ Для выбора ЛОВКОСТИ напиши /agility ☼\n☼ Для выбора ИНТЕЛЛЕКТА напиши /intelligence ☼")


@dp.message_handler(commands = ['strength', 'agility', 'intelligence'])
async def main_atr(message: types.Message):
   floor = 0
   if message.text == '/strength':
      main_char.change_name(message.from_user.username)
      main_char.change_strength(8)
      main_char.change_agility(5)
      main_char.change_intelligence(5)
      await message.answer("☼ Вы чувствуете прилив сил ☼")
   if message.text == "/agility":
      main_char.change_name(message.from_user.username)
      main_char.change_strength(5)
      main_char.change_agility(8)
      main_char.change_intelligence(5)
      await message.answer("☼ Вы чувствуете легкость движений ☼")
   if message.text == "/intelligence":
      main_char.change_name(message.from_user.username)
      main_char.change_strength(5)
      main_char.change_agility(5)
      main_char.change_intelligence(8)
      await message.answer("☼ Вы чувствуете, как знания переполняют ваш разум ☼")
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
   await message.answer("☼ Чтобы начать свое путшествие, напиши /start ☼\n☼ Чтобы посмотреть свои характеристики напиши /self ☼\n☼ Чтобы начать заново напиши /restart ☼")

@dp.message_handler(commands = ['next_floor'])
async def next_floor(message: types.Message, floor):
   floor += 1
   if floor == 10:
      fight(main_char, boss_base[random.randrange(1, 3)], 10)
   if random.randrange(0, 100) <= 100 * main_char.avoid_chance:
      next_floor(message, floor)
   dice = random.randrange(1, 6)
   if dice <= 3:
      loot(main_char, item_base[random.randrange(0 + floor, 5 + floor)])
      return
   if dice > 3:
      fight(main_char, enemy_base[random.randrange], floor)

@dp.message_handler(commands=['self'])
async def charact(message: types.Message):
   await message.answer(" ☼ Имя: " + str(main_char.name) + " ☼\n"
                        + " ☼ Сила: " + str(main_char.strength) + " ☼\n"
                        + " ☼ Ловкость: " + str(main_char.agility) + " ☼\n"
                        + " ☼ Интеллект: " + str(main_char.intelligence) + " ☼\n"
                        + " ☼ Максимальное здровье: " + str(main_char.max_health) + " ☼\n"
                        + " ☼ Максимальный запас сил: " + str(main_char.max_stamina) + " ☼\n"
                        + " ☼ Текущее здоровье: " + str(main_char.cur_health) + " ☼\n"
                        + " ☼ Текущий запас сил: " + str(main_char.cur_stamina) + " ☼\n"
                        + " ☼ Шанс уклонения: " + str(main_char.miss_chance_self) + " ☼\n"
                        + " ☼ Шанс крит. урона: " + str(main_char.crit_chance) + " ☼\n"
                        + " ☼ Шанс пропустить этаж: " + str(main_char.avoid_chance) + " ☼\n"
                        + " ☼ Урон: " + str(main_char.hand_damage) + " ☼\n"
                        + " ☼ Коэфициент защиты: " + str(main_char.armour_bonus) + " ☼\n"
                        + "◊ Инвентарь ◊\n"
                        + " ☼ 1 слот: " + inventory[1].name + " ☼\n"
                        + " ☼ 2 слот: " + inventory[2].name + " ☼\n"
                        + " ☼ 3 слот: " + inventory[3].name + " ☼\n"
                        + " ☼ 4 слот: " + inventory[4].name + " ☼\n"
                        + " ☼ 5 слот: " + inventory[5].name + " ☼\n")


@dp.message_handler()
async def any_message(message: types.Message):
   await message.answer("☼ Похоже Оракул не внимает вашим словам ☼\n☼ Попробуйте написать /help, чтобы понять, как с ним общаться. ☼")
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)