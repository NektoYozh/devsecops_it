items = [
    {
        "id":1,
        "title":"rock",
        "price": 10
    },
    {
        "id": 2,
        "title": "scissors",
        "price": 20
    },
    {
        "id": 3,
        "title": "paper",
        "price": 30
    }
        ]

cart = []

def print_list_of_dict(items):
    for item in items:
        for k, v in item.items():
            print("{0}: {1}".format(k, v), end = "\t\t")
        print()

def add_item(item_id):
    for i in (item for item in cart if item["id"] == item_id):
        i["count"] += 1
        break
    else:
        cart.append({"id":item_id,"count":1})

while 1:
    answer = input("Выберите пункт меню:\n"
                   "1 Вывести все товары каталога\n"
                   "2 Добавить товар в корзину по id\n"
                   "3 Вывести корзину\n"
                   "4 Выход\n")
    match answer:
        case "1":
            print_list_of_dict(items)
        case "2":
            answer = input("Введите id ")
            add_item(answer)
        case "3":
            print_list_of_dict(cart)
        case "4":
            break




