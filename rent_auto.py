def login():
    name = input('Введите ваше имя: ')
    print(f'Здравствуйте, {name}')
    print()
    age = int(input('Введите ваш возраст: '))
    if age < 18:
        print('Вход воспрещён!')
        return None, None
    else:
        print(f'Добро пожаловать на сервис, {name}!')
    print()
    return name, age


def hello():
    print('Добро пожаловать на сервис по аренде автомобилей!')
    print()
    auto = input('Введите интересующую модель авто: ')
    print(f'{auto} - отличный выбор!')
    print()
    return auto


var = ['24 часа', '7 дней', '30 дней']


def rent():
    print('Варианты аренды:')
    print(f'1 - На {var[0]} (6500р)')
    print(f'2 - На {var[1]} (5500р/сутки)')
    print(f'3 - На {var[2]} (4500р/сутки)')
    print()
    choice = input('Выберите вариант аренды: ')
    if choice in ['1', '2', '3']:
        print(f'Подтвердите аренду на {var[int(choice) - 1]}!')
        return choice
    else:
        print('Неверный выбор!')
        return None


def okay(auto, choice):
    res = input('Подтвердить? (Да / Нет): ')
    print()
    ok = 'Да'
    nope = 'Нет'
    if res == ok:
        print(
            f'Успешная аренда автомобиля {auto} на {choice}! Ожидайте звонка от нашего менеджера.')
    if res == nope:
        print('Оформление аренды прервано.')
    return auto, choice


name, age = login()
if name is not None:
    auto = hello()
    choice_num = rent()
    if choice_num is not None:
        choice_text = var[int(choice_num) - 1]
        okay(auto, choice_text)
