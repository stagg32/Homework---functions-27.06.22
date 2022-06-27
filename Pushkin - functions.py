
def pushkin_year():
    yearofbirth = int(input("Введите год рождения А.С.Пушкина от Р.Х.: "))
    if yearofbirth == 1799:
        print("Верно!")
    else:
        print("Неверный год рождения")
    return yearofbirth

def pushkin_day():
    dayofbirth = input("Введи его день Рождения: ")
    if dayofbirth == "6 июня":
        print("Верно!")
    else:
        print("Неверный день рождения")


while True:
    yearofbirth = pushkin_year()
    dayofbirth = pushkin_day()