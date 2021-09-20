# Задание 5.1
print("Задание 5.1")
#Создать программно файл в текстовом формате, записать
# в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('text1_file.txt', 'w+') as file:
    while True:
        user_answ = input('Введите текст: \n ')
        file.writelines(user_answ + '\n')
        if not user_answ:
            break


# Задание 5.2
print("Задание 5.2")

#Создать текстовый файл (не программно), сохранить
# в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

def count_info():
    try:
        with open('text1_file.txt', 'r', encoding="utf-8") as file:
            my_list = file.readlines()
            for i in range(len(my_list)):
                new_l = my_list[i].split()
                print(f'Количество строк в файле {len(my_list)}. В {i + 1}-ой строке {len(new_l)} слов(о)')
    except FileNotFoundError:
        return 'Файл не найден'


count_info()


# Задание 5.3
print("Задание 5.3")
#Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#Выполнить подсчет средней величины дохода сотрудников

def workers_statistics():
    workers = [['Петров ', '25000 \n'], ['Иванов ', '30000 \n'], ['Сидоров ', '15000 \n'], ['Фисташкин ', '8000 \n'],['Финашкин ', '32000']]
    try:
        with open('text2_file.txt', 'r+', encoding="utf-8") as file:
            for i in range(len(workers)):
                file.writelines(workers[i])
            l = file.readlines()
            poor = []
            sum = 0
            for i in range(len(l)):
                salary = int((l[i].split())[1])
                if salary < 20000:
                    poor.append((l[i].split())[0])
                sum += salary
            print(f'Средняя величина дохода сотрудников равна {sum / len(workers) / 12:.2f}')
            print(f'Меньше 20 тыс. рублей получает сотрудник: {", ".join(poor)}')
    except FileNotFoundError:
        return 'Файл не найден.'

workers_statistics()

# Задание 5.4
print("Задание 5.4")
#Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

