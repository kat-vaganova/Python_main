# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input("Введите месяц в виде целого числа от 1 до 12: "))

# 1 вариант (dict)
seasons_dict = {
    12: "зима",
    1: "зима",
    2: "зима",
    3: "весна",
    4: "весна",
    5: "весна",
    6: "лето",
    7: "лето",
    8: "лето",
    9: "осень",
    10: "осень",
    11: "осень"
}
print("Время года", seasons_dict.get(month), "(решение через dict_1)")

# 2 вариант (dict)
my_dict_season = {'Зима': (1, 2, 12),
                  'Весна': (3, 4, 5),
                  'Лето': (6, 7, 8),
                  'Осень': (9, 10, 11)
                  }
for el in my_dict_season.keys():
    if month in my_dict_season[el]:
        print(f"Время года {el} (решение чрез dict_2)")

# 3 вариант (list)

seasons_list = [['Зима', 1, 2, 12],
                ['Весна', 3, 4, 5],
                ['Лето', 6, 7, 8],
                ['Осень', 9, 10, 11]
                ]

for el in seasons_list:
    for n in el:
        if month == n:
            print(f"Время года {el[0]} (решение через list)")
