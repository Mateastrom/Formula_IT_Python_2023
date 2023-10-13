#Task_3
# TODO Разделите участников на две команды
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
#посчитаем кол-во игроков
l = len(list_players)
#найдем целое значение, начиная с которого игроки относятся во 2ю группу
middle = int(l/2)

group1 = list_players[:middle]
#в group1 игрок с номером middle не учитывается

group2 = list_players[middle:]
#в group2 игрок с номером middle учитывается
print(group1)
print(group2)
