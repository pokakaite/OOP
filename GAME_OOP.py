import random

class Menu:
    def __init__(self):
        self.name = input("Введите ваше имя - ")

    def menu(self):
        print(f'Добро пожаловать в игру, {self.name}.')
        choice = int(input('''Что вы хотите сделать?
        1 - Начать новую игру.
        2 - Выйти\n'''))
        return choice

class Player:
    where = ["Из-за дерева", "Из кустов", "Сверху", "Сзади", "Из кареты"]
    what = ["напал", "упал", "выпрыгнул", "выскачил", "свалился", "вылетел", "выкинули"]
    who = ["гоблин", "марадер", "вор", "зомби", "вурдалак", "леший", "вампир", "бес", "рысь"]
    tools = {
                "лук" : 5,
                "меч" : 10,
                "топор" : 15,
                "кирка" : 8,
                "мотыга" : 4,
                "вилы" : 7,
                "кулаки" : 2,
                "молот" : 6,
                "бита" : 6,
                "нож" : 3,
                "палка" : 1,
                "граната" : 30,
                "сюрикен" : 3
                }

    def __init__(self):
        self.health = 100
        self.attack = 20
        self.mana = 10
        self.tool = Player.tools['лук']
        self.level = 1
        self.inventory = 0

    def stats(self):
        print(f'''Ваше текущее состояние -
        Здоровье: {self.health},
        Атака: {self.attack},
        Мана: {self.mana},
        Оружие: {self.tool},
        Уровень: {self.level}''')

    def event(self):
        print("\n\n", random.choice(Player.where), random.choice(Player.what), random.choice(Player.who), '\n')

    def menu2(self):
        choice = int(input("Что вы будете делать? - \n"
                           "1 - Атаковать \n"
                           "2 - Бежать \n"
                           "3 - Инвентарь \n"
                           "4 - Выйти\n"))
        if choice == 1:
            print('Вы атаковали.')
            self.health -= 10

        if choice == 2:
            print('Вы убежали.')
            self.health += 10
        if choice == 3:
            k = []
            for i in Player.tools.keys():
                k.append(i)
            for i in range(len(k)):
                print(f"{i + 1} - {k[i]} с атакой {Player.tools[k[i]]}")
            tool = int(input(f"\nКакое оружие выберете (введите цифру) - "))
            self.tool = Player.tools[k[tool - 1]]
        if choice == 4:
            pass
        return choice

def game():
    menu = Menu()
    choice_menu = menu.menu()
    if choice_menu == 2:
        pass
    else:
        player = Player()
        player.event()
        choice_menu2 = player.menu2()
        while 1:
            if choice_menu2 == 4:
                pass
            else:
                player.stats()
                player.menu2()
game()





