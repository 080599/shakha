rooms = {}  # Словарь для хранения занятых номеров

def add_client():
    """Добавляет клиента и номер комнаты."""
    if rooms:
        print("Занятые номера:")
        for name, room in rooms.items():
            print(f"{name}: Комната {room}")
    else:
        print("Все номера свободны.")

    client_name = input("Введите имя клиента: ")
    room_number = input("Введите номер комнаты: ")

    if room_number not in rooms.values():
        rooms[client_name] = room_number
        print(f"Клиент {client_name} заселен в комнату {room_number}")
    else:
        print("Номер комнаты уже занят.")

def remove_client():
    """Удаляет клиента из базы."""
    client_name = input("Введите имя клиента для удаления: ")
    if client_name in rooms:
        del rooms[client_name]
        print(f"Клиент {client_name} удален из базы.")
    else:
        print("Клиента с таким именем нет в базе.")

def view_occupied_rooms():
    """Отображает список занятых номеров."""
    if rooms:
        print("Занятые номера:")
        for name, room in rooms.items():
            print(f"Комната {room}: {name}")
    else:
        print("Все номера свободны.")

while True:
    print("\nМеню:")
    print("1. Добавить клиента")
    print("2. Удалить клиента")
    print("3. Увидеть занятые номера")
    print("4. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_client()
    elif choice == "2":
        remove_client()
    elif choice == "3":
        view_occupied_rooms()
    elif choice == "4":
        break
    else:
        print("Неверный выбор.")