# Игра  крестики - нолики, Автор: Панков Ю. А.
# _*_ coding: utf-8 _*_
import random


def draw_field(field):
    """
    Функция отрисовки поля
    """
    print("-------------")
    for i in range(3): # после первой отрисвки для красоты можно не отрисовывать цифры
        print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print("-------------")


def gamer_move_input(gamer_object):
    """
    Функция ввода пользователем хода, внутри функции есть проверка на корректность введённого хода
    """
    check_move = True
    while check_move != False:
        gamer_move = input("Введите число от 1 до 9, на место которого будет поставлен " + gamer_object + " ")
        try:
            gamer_move = int(gamer_move)
        except:
            print("Ошибка! Вы точно ввели число?")
            continue
        if gamer_move >= 1 and gamer_move <= 9:
            if gamer_move < 4:  # К1, сделано для облегчения игры на боковой клавиатуре
                gamer_move = gamer_move + 6
            else:
                if gamer_move > 6:
                    gamer_move = gamer_move - 6
            if gamer_move != field[gamer_move - 1]:
                print("Ошибка! В этой клетке уже что-то стоит")
            else:
                field[gamer_move-1] = gamer_object
                check_move = False
        else:
            print("Ошибка! Введите число от 1 до 9, чтобы продолжить")


def ai_move_input(gamer_object, count):
    """
    Функция хода ИИ
    """
    if gamer_object == "X":  # Определение фигуры ИИ
        ai_object = "O"
    else:
        ai_object = "X"
    if win_comb_check(ai_object) != False:  # Проверка на наличие победной комбинации для ИИ
        field[win_comb_check(ai_object)-1] = ai_object
        return
    if win_comb_check(gamer_object) != False:  # Проверка на наличие победной комбинации для игрока
        field[win_comb_check(gamer_object)-1] = ai_object
        return
    if field[4] == 5:  # Первым ходом всегда выгодно занять центральную клетку
        field[4] = ai_object
        return
    if count == 1 and ai_object == "X" or count == 0 and ai_object == "O":  # Х2/О1 ставим фигуру на одну из клеток свободной диагонали
        if field[0] == 1 and field[8] == 9 and ai_object == "O" and field[1] == 1 and field[3] == 3:
            field[random.choice([0, 8, 0, 8, 3, 0, 8, 0, 1, 0, 8, 3])] = ai_object  # Даёт примерно 20% шанс ИИ на ошибку = игроку на победу
        if field[0] == 1 and field[8] == 9:
            field[random.choice([0, 8])] = ai_object
            return
        if field[2] == 3 and field[6] == 7:
            field[random.choice([2, 6])] = ai_object
            return
    if count == 2 and ai_object == "X":  # Х3
        if field[0] == 1 and field[1] == 2 and field[3] == 4:
            field[0] = ai_object
            return
        if field[1] == 2 and field[5] == 6 and field[2] == 3:
            field[2] = ai_object
            return
        if field[6] == 7 and field[3] == 4 and field[7] == 8:
            field[6] = ai_object
            return
        if field[8] == 9 and field[7] == 8 and field[5] == 6:
            field[8] = ai_object
            return
    if count > 2 and ai_object == "X":  # дальнейшии ходы Х
        i = 1
        while i < 8:
            if field[i] == i+1:
                field[i] = ai_object
                return
            i += 2
    if count == 1 and ai_object == "O":  # О2
        if field[1] == 2 and field[7] == 8:
            field[random.choice([1, 7])] = ai_object
            return
        if field[3] == 4 and field[5] == 6:
            field[random.choice([3, 5])] = ai_object
            return
    i = 0
    while i < 9:  # Если для какой-то фигуры не удалось выбрать место, ставим её в любую свободную крлетку
        if field[i] == i + 1:
            field[i] = ai_object
            return
        i += 1



def win_comb_check(object):
    """
    Функция проверки игрового поля на наличие выигрышной комбинации у определённой фигуры (Х/О) при следующем ходе
    """
    win_comb = ((0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6), (0,3,6), (1,4,7), (2,5,8))
    for each in win_comb:
        if field[each[0]] == field[each[1]] == object and field[each[2]] == each[2] + 1:
            return field[each[2]]
        if field[each[0]] == field[each[2]] == object and field[each[1]] == each[1] + 1:
            return field[each[1]]
        if field[each[2]] == field[each[1]] == object and field[each[0]] == each[0] + 1:
            return field[each[0]]
    return False


def win_check(field):
    """
    Функция проверки игрового поля на наличие выигрышной комбинации
    """
    win_comb = ((0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6), (0,3,6), (1,4,7), (2,5,8))
    for each in win_comb:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False


def choose_gamer_object():
    """
    Функция выбора игроком фигуры (Х/О)
    """
    check_move = True
    while check_move != False:
        gamer_object = input("Введите X или O для выбора, X ходят первые ")
        posible_gamer_objects_o = ("O", "o", "О", "о", "0")
        posible_gamer_objects_x = ("X", "x", "Х", "х")
        flag_error_choice = 0
        for each in posible_gamer_objects_o:
            if gamer_object == each:
                flag_error_choice += 1
                gamer_object = "O"  # англ. больш. о
        for each in posible_gamer_objects_x:
            if gamer_object == each:
                flag_error_choice += 1
                gamer_object = "X"  # англ. больш. х
        if flag_error_choice == 0:
            print("Ошибка! Выберете X или O чтобы продолжить")
            continue
        else:
            return gamer_object


def main(field):
    """
    Основная функция, в ней происходит игра
    """
    gamer_object = choose_gamer_object()
    counter = 0
    count_ai = 0
    win = False
    while win != True:
        draw_field(field_g)
        if counter % 2 == 0:
            if gamer_object == "X":
                gamer_move_input(gamer_object)
            else:
                ai_move_input(gamer_object, count_ai)
                count_ai += 1
        else:
            if gamer_object == "X":
                ai_move_input(gamer_object, count_ai)
                count_ai += 1
            else:
                gamer_move_input(gamer_object)
        counter += 1
        i = 0
        while i < 9:
            if field[i] == "X" or field[i] == "O":
                field_g[i] = field[i]
            else:
                field_g[i] = " "
            i += 1
        if counter > 4:
            win_object = win_check(field)
            if win_object:
                if win_object == gamer_object:
                    draw_field(field_g)
                    print("Вы выиграли!")
                    return
                else:
                    draw_field(field_g)
                    print("Вы проиграли :(")
                    return
        if counter == 9:
            draw_field(field_g)
            print("Ничья!")
            return


field = [i for i in range(1, 10)]
field_g = [7, 8, 9, 4, 5, 6, 1, 2, 3]  # К1, сделано для облегчения игры на боковой клавиатуре
main(field)
while 1:
    """
    Цикл перезапускаа игры
    """
    repeat_g = input("Хотите сыграть ещё раз? (Y/N) ")
    if repeat_g == "Y" or repeat_g == "y":
        field = [i for i in range(1, 10)]
        field_g = [7, 8, 9, 4, 5, 6, 1, 2, 3]
        main(field)
    if repeat_g == "N" or repeat_g == "n":
        print("До свидания :)")
        break
    else:
        continue