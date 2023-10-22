list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_numbers = len(set(list1).intersection(list2))
print("Количество чисел, содержащихся одновременно в обоих списках:", common_numbers)
