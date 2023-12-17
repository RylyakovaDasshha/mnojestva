#вводим последовательность чисел через пробел 
sequence = input("Введите числа через пробел: ")
#разбиваем пос-во чисел на отдельные числа
numbers = sequence.split()
#создаем множества
previous_numbers = set()
#проходимся по списку numbers
for number in numbers:
    #если число раньше встречалось выводится да
    if number in previous_numbers:
        print("YES")
        #если число не встречалось раньше выводится нет
    else:
        print("NO")
        previous_numbers.add(number)
