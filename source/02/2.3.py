answer = str(input("Is it raining? "))
print(answer)
if answer.lower() == "yes":
    answer = input("Is it windy? ")
    if answer.lower() == 'yes':
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")