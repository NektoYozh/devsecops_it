number = 2
while number <= 100:
    divisor = 2
    there_is_divisor = False
    while divisor <= number ** 0.5:
        if number % divisor == 0:
            there_is_divisor = True
            break
        divisor += 1
    if not there_is_divisor:
        print(number)
    number += 1