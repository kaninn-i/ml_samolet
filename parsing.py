from time import sleep
import cianparser as cian
# proxies = [
#   '117.250.3.58:8080', 
#   '115.96.208.124:8080',
#   '152.67.0.109:80', 
#   '45.87.68.2:15321', 
#   '68.178.170.59:80', 
#   '20.235.104.105:3729', 
#   '195.201.34.206:80',
# ]


# moscow_parser = cian.CianParser(location='Москва')
# data = moscow_parser.get_flats(deal_type='sale', rooms='all', with_saving_csv=True, additional_settings={"start_page":1, "end_page":54}, with_extra_data=True)


# for i in cian.list_locations():
#   print(i)


list_1 = ['Егорьевск','Ступино','Руза','Электросталь']

# бронницы и балашиха есть ("Бронницы", "Балашиха", "Видное", "Волоколамск", "Воскресенск", "Высоковск", "Верея", "Голицыно", "Дзержинский", "Долгопрудный",
# "Дубна", "Дмитров", "Домодедово", "Дрезна", "Дедовск", "Егорьевск", "Егорьевск", "Жуковский", "Звенигород", "Зарайск", "Истра",
# "Ивантеевка", "Коломна", "Королёв", "Луховицы", "Люберцы", "Можайск", "Мытищи", "Наро-Фоминск", "Ногинск", "Орехово-Зуево", "Одинцово", "Озёры", "Подольск", "Протвино", ) 

# list_2 = ["Краснознаменск", "Кашира""Клин", "Красногорск", "Краснозаводск", "Кубинка", "Куровское (Московская)", "Лыткарино", "Ликино-Дулёво",
#                   "Лосино-Петровский", "Луховицы", "Люберцы", "Можайск", "Мытищи", "Наро-Фоминск", "Ногинск", , "Одинцово", "Озёры", "Подольск", "Протвино", "Пущино",]

# list_3 = ["Реутов", "Рошаль", "Раменское", "Руза", "Серпухов", "Сергиев Посад", "Солнечногорск", "Ступино", "Старая Купавна", "Талдом",
#                   "Фрязино", "Химки", "Хотьково", "Черноголовка", "Чехов", "Шатура", "Щёлково", "", "Электрогорск", "Электроугли", , "Павловский Посад", "Пересвет", "Пушкино"]

 
town_parser = cian.CianParser(location='Долгопрудный')
rooms = [1, 2, 3, 'studio']
for room in rooms:
  print('Парсинг города Долгопрудный, комнат:', room)
  data = town_parser.get_flats(
  deal_type='sale',
  rooms=room,
  with_saving_csv=True,
  additional_settings={"start_page":1, "end_page":11},
  with_extra_data=True)
  sleep(30)
sleep(60)

town_parser = cian.CianParser(location='Реутов')
rooms = [1, 2, 3, 'studio']
for room in rooms:
  print('Парсинг города Реутов, комнат:', room)
  data = town_parser.get_flats(
  deal_type='sale',
  rooms=room,
  with_saving_csv=True,
  additional_settings={"start_page":1, "end_page":20},
  with_extra_data=True)
  sleep(30)
sleep(60)

town_parser = cian.CianParser(location='Домодедово')
rooms = [1, 2, 3, 4, 5, 'studio']
for room in rooms:
  print('Парсинг города Домодедово, комнат:', room)
  data = town_parser.get_flats(
  deal_type='sale',
  rooms=room,
  with_saving_csv=True,
  additional_settings={"start_page":1, "end_page":25},
  with_extra_data=True)
  sleep(30)
sleep(60)

town_parser = cian.CianParser(location='Щёлково')
rooms = [1, 2, 3, 'studio']
for room in rooms:
  print('Парсинг города Щёлково, комнат:', room)
  data = town_parser.get_flats(
  deal_type='sale',
  rooms=room,
  with_saving_csv=True,
  additional_settings={"start_page":1, "end_page":15},
  with_extra_data=True)
  sleep(30)
sleep(60)

town_parser = cian.CianParser(location='Подольск')
rooms = [1, 2, 3, 'studio']
for room in rooms:
  print('Парсинг города Подольск, комнат:', room)
  data = town_parser.get_flats(
  deal_type='sale',
  rooms=room,
  with_saving_csv=True,
  additional_settings={"start_page":1, "end_page":18},
  with_extra_data=True)
  sleep(30)
sleep(60)

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
