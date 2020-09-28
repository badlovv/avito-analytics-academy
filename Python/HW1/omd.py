import time


def step1(again=False):
    if again:
        print('Безумец!')
        time.sleep(1)

    print(
        'Утка-маляр 🦆 решила выпить зайти в бар.'
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {} / {}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Утка: кря, спасибо за ☂')
    return step3()


def step2_no_umbrella():
    print('Правильно, утки не мокнут. А себе взял зонтик?')
    option = ''
    options = {'да, как видишь': True, 'нет': False}
    while option not in options:
        print('Выберите: {} / {}'.format(*options))
        option = input()
    if options[option]:
        print('А тебя нет в сеттинге этой игры')
        return step3_whoyouare()
    print('Ну и правильно, ты же просто игрок-наблюдатель за уткой-маляром))')
    time.sleep(2)
    return step3()


def step3_whoyouare():
    print('Ты: а кто я?')
    for _ in range(3):
        print('.')
        time.sleep(0.5)
    print('Ты просто игрок-наблюдатель за уткой-маляром, играть-то будешь?')
    time.sleep(1)
    option = ''
    options = {'да': True, 'а какой смысл...': False}
    while option not in options:
        print('Выберите: {} / {}'.format(*options))
        option = input('Ты:')
    if options[option]:
        print('Просто бы брал себе зонт и все!')
        time.sleep(2)
        print('Так, ну что там, а... ну так вот...')
        print('')
        time.sleep(2)
        return step3()
    return end_game(True)


def step3():
    print('Звонко шлепая лапами по асфальту, утка направилась в бар "Арарат"')
    print('')
    print('У входа в бар утку ждал Face-контроль')
    print('Face-контроль: слышала мой трек про бургер?')
    option = ''
    options = {'кря': True, 'бррря': False}
    while option not in options:
        print('Выберите: {} / {}'.format(*options))
        option = input('Утка: ')
    if options[option]:
        print('Face-контроль: че?')
    else:
        print('Face-контроль: извини, ты не проходишь!')
        return end_game()

    option = ''
    options = {'кря-кря': True, 'бррря': False}
    while option not in options:
        print('Выберите: {} / {}'.format(*options))
        option = input('Утка: ')
    if options[option]:
        print('Face-контроль: ладно, проходи, надеюсь ты не слушала этот трек...')
        print('Утка: кря-кря-кря')
        time.sleep(2)
        print('Утка вошла в бар... ')
        time.sleep(2)
        print('А там армяне в нарды играют)))')
        time.sleep(2)
        return step4()
    else:
        print('Face-контроль: значит, не послышалось. Извини, ты не проходишь!')
        return end_game()


def step4():
    print('Поздравляем, вы доставили утку в бар "Арарат". Начать заново?')
    option = ''
    options = {'да': 0, 'нет': 1, 'хочу анекдот': 2}
    while option not in options:
        print('Выберите: {} / {} / {}'.format(*options))
        option = input('Ты: ')
    if options[option] == 0:
        return step1(True)
    elif options[option] == 2:
        print("""
        Закончился всемирный потоп. Ковчег причаливает к Арарату, 
        и Ной начинает оттуда выгружать клетки с медведями, собаками, 
        тиграми, львами и другими животными.
        А на горе армяне сидят и в нарды играют. 
        Один другого в бок толкает и говорит:
        - Ара, смотри, цирк приехал!
        """)
        return step4()
    else:
        return end_game(True)


def end_game(win=False):
    if win:
        print('Ну и правильно (Game Over)!')
        return
    print('Проиграл (Game Over)!')


if __name__ == '__main__':
    step1()
