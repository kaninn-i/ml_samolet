from time import sleep
import cianparser as cian

moscow_parser = cian.CianParser(location='Москва')
rooms = [1, 2, 3, 4, 5, 'studio']
n = 25
for room in rooms:
  while n < 54:
    print('Парсинг города Москва, комнат:', room, "страницы:", n + 1, "-", n + 5)
    data = moscow_parser.get_flats(
    deal_type='sale',
    rooms=room,
    with_saving_csv=True,
    additional_settings={"start_page": n + 1, "end_page": n + 5, "sort_by": "creation_data_from_older_to_newer"},
    with_extra_data=True)
    n += 5
    sleep(30)
  sleep(30)
sleep(120)

# for i in cian.list_locations():
#   print(i)


# list_1 = ['Егорьевск','Ступино','Руза','Электросталь']

# бронницы и балашиха есть ("Бронницы", "Балашиха", "Видное", "Волоколамск", "Воскресенск", "Высоковск", "Верея", "Голицыно", "Дзержинский", "Долгопрудный",
# "Дубна", "Дмитров", "Домодедово", "Дрезна", "Дедовск", "Егорьевск", "Егорьевск", "Жуковский", "Звенигород", "Зарайск", "Истра",
# "Ивантеевка", "Коломна", "Королёв", "Луховицы", "Люберцы", "Можайск", "Мытищи", "Наро-Фоминск", "Ногинск", "Орехово-Зуево", "Одинцово", "Озёры", "Подольск", "Протвино", ) 

# list_2 = ["Краснознаменск", "Кашира""Клин", "Красногорск", "Краснозаводск", "Кубинка", "Куровское (Московская)", "Лыткарино", "Ликино-Дулёво",
#                   "Лосино-Петровский", "Луховицы", "Люберцы", "Можайск", "Мытищи", "Наро-Фоминск", "Ногинск", , "Одинцово", "Озёры", "Подольск", "Протвино", "Пущино",]

# list_3 = ["Реутов", "Рошаль", "Раменское", "Руза", "Серпухов", "Сергиев Посад", "Солнечногорск", "Ступино", "Старая Купавна", "Талдом",
#                   "Фрязино", "Химки", "Хотьково", "Черноголовка", "Чехов", "Шатура", "Щёлково", "", "Электрогорск", "Электроугли", , "Павловский Посад", "Пересвет", "Пушкино"]

 
# town_parser = cian.CianParser(location='Долгопрудный')
# rooms = [1, 2, 3, 'studio']
# for room in rooms:
#   print('Парсинг города Долгопрудный, комнат:', room)
#   data = town_parser.get_flats(
#   deal_type='sale',
#   rooms=room,
#   with_saving_csv=True,
#   additional_settings={"start_page":1, "end_page":11},
#   with_extra_data=True)
#   sleep(30)
# sleep(60)

# for town in list_1:
#   town_parser = cian.CianParser(location=town)
#   rooms = [1, 2, 3, 4, 5, 'studio']
#   for room in rooms:
#     data = town_parser.get_flats(
#       deal_type='sale',
#       rooms=room,
#       with_saving_csv=True,
#       additional_settings={"start_page":1, "end_page":3},
#       with_extra_data=True)
#     sleep(30)
# sleep(60)


# town_parser = cian.CianParser(location='Егорьевск')
# data = town_parser.get_flats(
#   deal_type='sale',
#   rooms=2,
#   with_saving_csv=True,   
#   additional_settings={"start_page":1, "end_page":10},
#   with_extra_data=True)
# sleep(30)
