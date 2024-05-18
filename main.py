import random


#Вставки
def sortirovka_vs(stroka):
    sravnenya = 0
    zameny = 0

    for i in range(1, len(stroka)):
        key = stroka[i]
        j = i - 1
        sravnenya += 1

        while j >= 0 and stroka[j] > key:
            stroka[j + 1] = stroka[j]
            zameny += 1
            j -= 1
            sravnenya += 1

        stroka[j + 1] = key

    return stroka, sravnenya, zameny

#Отбор
def sortirovka_otb(stroka):
    sravnenya = 0
    zameny = 0

    for i in range(len(stroka)):
        min_index = i

        for j in range(i + 1, len(stroka)):
            sravnenya += 1
            if stroka[j] < stroka[min_index]:
                min_index = j

        stroka[i], stroka[min_index] = stroka[min_index], stroka[i]
        zameny += 1

    return stroka, sravnenya, zameny


# Главная функция
def main():
    array_size = int(input("Введите размер массива: "))
    array = [random.randint(1, 100) for _ in range(array_size)]  # Генерация случайных чисел от 1 до 100

    otsortir_massiv1, vivod_sravneniy2, vivod_zamen3 = sortirovka_vs(array.copy())
    otsortir_massiv3, vivod_sravneniy4, vivod_zamen5 = sortirovka_otb(array.copy())
    print("Метод сортировки вставками")
    print("Исходный массив:",array)
    print("--------------------------------------------")
    print("Отсортированный массив:", otsortir_massiv1)
    print("--------------------------------------------")
    print("Количество сравнений: ",vivod_sravneniy2)
    print("Количество замен: ", vivod_zamen3)
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("Метод сортировки отбором")
    print("Исходный массив:", array)
    print("--------------------------------------------")
    print("Отсортированный массив:", otsortir_massiv3)
    print("--------------------------------------------")
    print("Количество сравнений: ", vivod_sravneniy4)
    print("Количество замен: ", vivod_zamen5)
    print("--------------------------------------------")




# Вызов главной функции
if __name__ == "__main__":
    main()