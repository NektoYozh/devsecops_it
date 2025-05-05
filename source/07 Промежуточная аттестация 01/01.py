def get_coefficient(name):
    while 1:
        try:
            float_value = float(input("{0}: ".format(name)))
            return float_value
        except ValueError:
            print("Введенное значение не является числом!")
            continue

coefficients = dict.fromkeys(["a", "b", "c"])

print("Введите коэффициенты квадратного уравнения")

for key in coefficients.keys():
    coefficients[key] = get_coefficient(key)

if coefficients["a"] == 0:
    print("Данное уравнение не является квадратным!")
else:
    D = coefficients["b"] * coefficients["b"] - 4 * coefficients["a"] * coefficients["c"]
    if D == 0:
        print("Уравнение имеет один корень: {0}".format(round(-coefficients["b"]/(2*coefficients["a"]),5)))
    elif D < 0:
        print("Уравнение не имеет корней")
    else:
        print("Уравнение имеет два корня: {0} и {1}".format(
                                                            round((-coefficients["b"] - D ** 0.5) / (2 * coefficients["a"]), 5),
                                                            round((-coefficients["b"] + D ** 0.5) / (2 * coefficients["a"]), 5)
                                                            )
        )