import time

lst_auto = ['Kia K5', 'BMW X5', 'BMW M5 Competition', 'Toyota Camry']
var = ['24 часа', '7 дней', '30 дней']
price_per_day = [6500, 5500, 4500]


def first_time():
    print('Добро пожаловать на сервис по аренде автомобилей!')
    print('1 - Авторизация и аренда авто')
    print('2 - Выход')
    go = int(input('Выберите опцию: '))
    if go == 2:
        print('До новых встреч!')
        return 'exit'
    if go == 1:
        print('Загрузка сервиса...', end='')
        time.sleep(1)
        print('Готово!')
        print()
        return 'continue'


def login():
    name = input('Введите ваше имя: ')
    print(f'Здравствуйте, {name}')
    print()
    age = int(input('Введите ваш возраст: '))
    if age < 18:
        print('Вход воспрещён!')
        return None, None
    else:
        print(f'Успешная авторизация, {name}!')
    print()
    return name, age


def hello():
    print('В нашем сервисе представлены следующие модели:')
    for i, car in enumerate(lst_auto, 1):
        print(f'{i}. {car}')
    auto = input('Введите интересующую модель авто: ')
    if auto in ['1', '2', '3', '4']:
        print(f'{lst_auto[int(auto) - 1]} - отличный выбор!')
        return lst_auto[int(auto) - 1]
    else:
        print('Неверный выбор!')
        return None


def rent():
    print()
    print('Варианты аренды:')
    for i, (v, p) in enumerate(zip(var, price_per_day), 1):
        print(f'{i}. На {v} ({p}р/сутки)')
    print()
    choice = input('Выберите вариант аренды: ')
    if choice in ['1', '2', '3']:
        choice = int(choice)
        if choice == 1:
            total = price_per_day[0]
        elif choice == 2:
            total = price_per_day[1] * 7
        elif choice == 3:
            total = price_per_day[2] * 30
        print(f'Стоимость аренды на {var[choice - 1]} составит {total}р.')
        return choice, total
    else:
        print('Неверный выбор!')
        return None, None


def okay(auto, choice, total):
    res = input('Подтвердить?\n(Да / Нет): ')
    print()
    ok = 'Да'
    nope = 'Нет'
    if res == ok:
        print(
            f'Успешная аренда автомобиля {auto} на {choice}!\n'
            f'Предварительная стоимость аренды: {total}р.\n'
            f'Ожидайте звонка от нашего менеджера.')
    if res == nope:
        print('Оформление аренды прервано.')
    return auto, choice


action = first_time()
if action == 'exit':
    exit()

name, age = login()
if name is not None:
    auto = hello()
    if auto is not None:
        choice_num, total_price = rent()
        if choice_num is not None:
            choice_text = var[int(choice_num) - 1]
            okay(auto, choice_text, total_price)
