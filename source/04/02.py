def get_number(is_not_negative:bool, question:str, error:str):
    while 1:
        answer = input(question)
        count = answer[1:] if answer[0] == "-" and not is_not_negative else answer
        if not count.isdigit():
            print(error)
            continue
        count = int(answer)
        break
    return count

number_count = get_number(True,"Введите количество чисел: ", "Ошибка! Должно быть введено неотрицательное число!")

positive_count = negative_count = zero_count = 0

for _ in range(number_count):
    number = get_number(False, "Введите число: ", "Ошибка! Введенная строка не является числом!")
    if number > 0:
        positive_count += 1
    elif number == 0:
        zero_count += 1
    else:
        negative_count += 1

print("Количество отрицательных чисел: {0}.\n"
      "Количество нулей: {1}.\n"
      "Количество положительных чисел: {2}.".format(negative_count, zero_count, positive_count))