import math
import time


def list_generator():
    lista = []
    for i in range(9):
        lista.append(i)
    print("wygenerowano listę")
    return lista


def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        end_list = lista[-1]
        middle_list = [end_list]
        lesser_list = []
        greater_list = []
        for i in range(len(lista) - 1):
            if lista[i] <= end_list:
                lesser_list.append(lista[i])
            else:
                greater_list.append(lista[i])
        returned_list = quick_sort(lesser_list) + middle_list + quick_sort(greater_list)
        return returned_list


def linear_search(value, lista):
    for i in lista:
        if i == value:
            return True


def binary_search(value, lista):
    binary_search_list = quick_sort(lista)

    low_index = 0
    last_index = len(binary_search_list) - 1
    middle_index = last_index // 2

    while low_index <= last_index:
        if value == binary_search_list[middle_index]:
            return True
        elif value > binary_search_list[middle_index]:
            low_index = middle_index + 1
            middle_index = (last_index + low_index) // 2
        elif value < binary_search_list[middle_index]:
            last_index = middle_index - 1
            middle_index = (last_index + low_index) // 2


def jump_search(value, lista):
    jump_value = int(math.sqrt(len(lista)))
    jump_search_list = quick_sort(lista)
    marker = 0
    i = 0

    if jump_search_list == []:
        return None

    while True:
        if i <= len(jump_search_list)-1:
            if jump_search_list[i] == value:
                return True
            elif jump_search_list[i] < value:
                marker = i
                i += jump_value
            elif jump_search_list[i] > value:
                i -= 1
                if marker >= i:
                    return None
        elif i < 0:
            return None
        else:
            i -= jump_value
            while i <= len(jump_search_list) - 1:
                if jump_search_list[i] == value:
                    return True
                else:
                    i += 1
                    if i == len(jump_search_list):
                        return None

def main():
    generated_list = [8, -1, 9, 100, 2039, -4938, 0, 4] #list_generator()
    search_value = int(input("Wpisz szukana liczbe: "))
    start = time.time()
    if linear_search(search_value, generated_list) is True:
        print("ZNALEZIONO LICZBĘ")
    else:
        print('NIEZNALEZIONO')
    stop = time.time()
    print("Czas wyszukiwania liniowego: ", stop - start, " sek.")

    start = time.time()
    if binary_search(search_value, generated_list) is True:
        print("ZNALEZIONO LICZBĘ")
    else:
        print('NIEZNALEZIONO')
    stop = time.time()
    print("Czas wyszukiwania binarnego: ", stop - start, " sek.")

    start = time.time()
    if jump_search(search_value, generated_list) is True:
        print("ZNALEZIONO LICZBĘ")
    else:
        print('NIEZNALEZIONO')
    stop = time.time()
    print("Czas wyszukiwania jump-search: ", stop - start, " sek.")


if __name__ == '__main__':
    main()
