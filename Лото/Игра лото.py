from projects.Project.Лото.Loto_class import Loto


# Сама игра
while True:
    mark_list = []                                                                                                      # Список с индексами игроков на исключение
    players_list = []                                                                                                   # Список игроков в игре
    winners_list = []                                                                                                   # Список победителей
    loto_number = Loto()                                                                                                # Игровые числа будут генерироваться из этой переменной дял всех игроков
    a = 0                                                                                                               # Количество игроков
    t_f = ''                                                                                                            # Бот или не бот
    y_n = ''                                                                                                            # Зачеркнуть число или нет
    repeat = ''                                                                                                         # Играть ещё раз в игру или нет

    # Инициализация игроков
    while a <= 0:
        try:
            a = int(input('Введите количество игроков: '))
        except:
            print(f'Ошибка. Введите количество игроков ещё раз')

    for i in range(a):
        players_list.append(exec("player_{} = {}".format(i, i)))

    # Для каждого игрока создаётся имя, числа в карте и сама карта
    for i in range(len(players_list)):
        players_list[i] = Loto()
        players_list[i].player_name = input(f"Введите имя игрока_{i}: ")
        while t_f != 't' and t_f != 'f':
            t_f = input("Введите, является ли игрок ботом (t, f): ")
        if t_f == 't':
            players_list[i].bot = True
        elif t_f == 'f':
            players_list[i].bot = False

        t_f = ''                                                                                                        # Сброс ответа, чтобы спрашивать каждого игрока

        players_list[i].new_card_number()
        players_list[i].compute_card()

    # Приступаем к игровой сессии
    while True:
        mark_list = []                                                                                                  # Обнуляем список каждый раз
        loto_number.get_random_number()                                                                                 # Получаем одно число на всех каждый раз
        print(f"Новый бочонок: {loto_number.current_number} (осталось {len(loto_number.numbers_in_game)})")
        for i in players_list:                                                                                          # Показываем карты всех игроков
            i.show_card(i.player_name)
            i.current_number = loto_number.current_number                                                               # Передаём одно число всем

        for i in players_list:
            if i.bot:
                if loto_number.current_number[0] in i.card_number:
                    i.pass_in_card()
                    i.card_number.remove(loto_number.current_number[0])
            else:
                y_n = ''                                                                                                # Сброс ответа, чтобы спрашивать каждого игрока
                while y_n != 'y' and y_n != 'n':
                    y_n = input(f"Игрок {i.player_name}: Зачеркнуть цифру? (y/n): ")

                if y_n == 'y' and loto_number.current_number[0] in i.card_number:
                    i.pass_in_card()
                    i.card_number.remove(loto_number.current_number[0])
                elif y_n == 'n' and loto_number.current_number[0] not in i.card_number:
                    continue
                else:
                    print(f"Игрок {i.player_name} проиграл")
                    mark_list.append(i)

            if not i.card_number:
                print(f'Игрок {i.player_name} закончил')
                winners_list.append(i)
                mark_list.append(i)

        for i in range(len(mark_list)):
            players_list.remove(mark_list[i])

        if not players_list:
            print('*' * 50)
            if not winners_list:
                print('Все проиграли. Удачи в следующий раз!')
                break
            else:
                for i in range(len(winners_list)):
                    print(f'Игрок {winners_list[i].player_name} занял {i + 1} место')
                break

        print('*' * 50)                                                                                                 # Разделение раундов

    print('*' * 50)
    while repeat != 'y' and repeat != 'n':
        repeat = input(f'Хотите сыграть ещё раз? (y,n) ')

    print('*' * 50)

    if repeat == 'n':
        break
