from classes import storage_1, shop_1, Request

print("Привет!")

while True:
    print("Текущие площади: ")
    print(f"storage_1: {storage_1}")
    print(f"shop_1: {shop_1}")
    user_input = input("Введите команду: ")
    if user_input == "стоп":
        break
    else:
        request = Request(user_input)
        request.move()


