sequence = input("Введите числа через пробел: ")
numbers = sequence.split()
previous_numbers = set()

for number in numbers:
    if number in previous_numbers:
        print("YES")
    else:
        print("NO")
        previous_numbers.add(number)
