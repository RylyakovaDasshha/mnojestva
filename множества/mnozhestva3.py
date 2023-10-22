list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

common_numbers = sorted(set(list1).intersection(list2))

print("Даны два списка чисел:", list1, list2)
print("Общие числа входящие в оба списка в порядке возрастания:")
for number in common_numbers:
    print(number)
