multiplier_2 = 2
while multiplier_2 <= 9:
    multiplier_1 = 2
    while multiplier_1 <= 5:
        print("{0} x {1} = {2}".format(multiplier_1, multiplier_2, multiplier_1 * multiplier_2), end="\t\t")
        multiplier_1 += 1
    print("\n")
    multiplier_2 += 1
