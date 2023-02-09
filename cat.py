import enum
import time
from random import randint

class Pets:
    states =[{'id': 1, 'eng': 'playing', 'rus': 'играет', 'period': 10},
             {'id': 2, 'eng': 'eating', 'rus': 'кушает', 'period': 10},
             {'id': 3, 'eng': 'sleeping', 'rus': 'спит', 'period': 30},
             {'id': 4, 'eng': 'resting', 'rus': 'отдыхает', 'period': 15},
             {'id': 5, 'eng': 'walking', 'rus': 'гуляет', 'period': 15},
             {'id': 6, 'eng': 'angry', 'rus': 'злится', 'period': 5}
             ]

    def __init__(self, name):
        self.name = name
        self.age = randint(2, 15)
        self.happiness = randint(20, 80)
        self.satiety = randint(20, 80)
        self.state = 4
        self.begin_action = time.time()
        self.period = 0

    def get_state(self):
        end_time = time.time()
        begin_time = self.begin_action
        diff_time = end_time - begin_time
        self.period = diff_time
        match self.state:
            case 1:
                if diff_time > 10:
                    self.state = 5
                    self.begin_action = time.time()
            case 2:
                if diff_time > 10:
                    self.state = 4
                    self.begin_action = time.time()
            case 3:
                if diff_time > 30:
                    self.state = 5
                    self.begin_action = time.time()
            case 4:
                if diff_time > 15 and randint(0, 1):
                    self.state = 5
                    self.begin_action = time.time()
            case 5:
                if diff_time > 15 and randint(0, 1):
                    self.state = 4
                    self.begin_action = time.time()
            case 6:
                if diff_time > 5:
                    self.state = 4
                    self.begin_action = time.time()
        diff_time = (time.time() - self.begin_action)
        period = self.states[self.state-1]['period'] - diff_time
        period = max(period, 0)
        return [self.states[self.state-1]['rus'], self.states[self.state-1]['eng'], period]

    def cat_play(self):
        self.begin_action = time.time()
        self.satiety -= 10
        if not randint(0, 2):
            self.happiness = 0
            self.state = 6
        else:
            if self.state == 3:
                self.happiness -= 5
            else:
                self.happiness += 15
            self.state = 1
        self.happiness = max(self.happiness, 0)
        self.satiety = max(self.satiety, 0)

    def cat_eat(self):
        if self.state != 3:
            self.begin_action = time.time()
            self.satiety += 15
            self.happiness += 5
            if self.satiety > 100:
                self.happiness -= 30
            self.state = 2
        self.happiness = max(self.happiness, 0)

    def cat_sleep(self):
        if self.state != 3:
            self.begin_action = time.time()
            self.state = 3

    def cat_free(self):
        if self.state != 3:
            self.begin_action = time.time()
            if randint(0, 1):
                self.state = 4
            else:
                self.state = 5

    def action_to_cat(self, action):
        match action:
            case 0:
                pass
            case 1:
                self.cat_play()
            case 2:
                self.cat_eat()
            case 3:
                self.cat_sleep()
            case 4:
                self.cat_free()
            case 5:
                pass
            case 6:
                pass


class Menu(enum.Enum):
    def __init__(self, id, title):
        self.id = id
        self.title = title

    cat_act = (0, "Выберите действие для кота")
    cat_play = (1, "Играть с котом")
    cat_eat = (2, "Кормить кота")
    cat_sleep = (3, "Уложить спать кота")
    cat_rest = (4, "Оставить в покое кота")
    cat_state = (5, "Узнать, что делает кот")


def main_menu():
    item_list = []
    title_list = []
    for menu in Menu:
        item_list.append(menu.name)
        title_list.append(menu.title)
        print('\t', menu.id, menu.title)
    while True:
        item = input("Выберите номер пункта меню : ")
        if item.isdigit():
            if int(item) <= len(item_list):
                index = int(item) - 1
                item = item_list[index]
            else:
                print("Неправильно введен номер меню")
        if item not in item_list:
            print("Неправильно введено наименование меню!")
        else:
            ind = item_list.index(item)
            print("Вы выбрали :", title_list[ind])
            if item == 'exit':
                item = ""
            break
    return ind + 1

class Menu_actions:
    def __init__(self):
        self.menu_act = []

    def set_menu(self):
        for menu in Menu:
            dic = {"id": menu.id, 'title': menu.title}
            self.menu_act.append(dic)

