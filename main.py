# character_creation_module/main.py
from random import randint

# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().
# from graphic_arts.start_game_banner import run_screensaver

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


# New main class.
class Character:
    # Constant for the range of damage points.
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    # Declaring a class construction.
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'

    # Declaring a metod for attack.
    def attack(self):
        # We describe the method of attack.
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    # Declaring a metod for protection.
    def defence(self):
        # We describe the method of protection.
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона')

    # Declaring a metod for special attack.
    def special(self):
        # We describe the method of special attack.
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL}, {self.SPECIAL_BUFF}".')


# New class for Warrior.
class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


# New class for Mage.
class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = ('Маг — находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом.')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_STAMINA - 35
    SPECIAL_SKILL = 'Атака'


# New class for Healer.
class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = ('Лекарь — могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов.')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_STAMINA - 40
    SPECIAL_SKILL = 'Защита'


warrior = Warrior('Кодослав')
mage = Mage('Мага')
healer = Healer('Здоровес')


def choice_char_class(char_name: str) -> Character:
    """ Returns a string with the selected character class. """
    # Added a dictionary that correlates user input and character class.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    approve_choice: str = None

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        # They brought a description of the character to the terminal.
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


character = choice_char_class(char_name)
def start_training(character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    if char_class == 'warrior':
        print(f'{super().__char_class__.__name__}, ты Воитель — великий мастер '
              f'ближнего боя.')
    if char_class == 'mage':
        print(f'{super().__char_class__.__name__}, ты Маг — превосходный '
              f'укротитель стихий.')
    if char_class == 'healer':
        print(f'{super().__char_class__.__name__}, ты Лекарь — чародей, '
              f'способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        # Замените блок условных операторов на словарь
        # и вынесите его из цикла. Здесь останется одно условие
        # принадлежности введённой команды словарю.
        # В функции print() будет вызываться метод класса,
        # который соответствует введённой команде.
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


print(warrior)
print(warrior.attack())
print()
print(mage)
print(mage.attack())
print()
print(healer)
print(healer.attack())
