from abc import abstractmethod, ABC


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self, items: dict, capacity=100):
        self.__items = items
        self.__capacity = capacity

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, count):
        self.__capacity = count

    def add(self, name, count):
        if name in self.__items.keys():
            if self.get_free_space() >= int(count):
                print("Товар добавлен")
                self.__items[name] += int(count)
                return True
            else:
                if isinstance(self, Shop):
                    print("Не хватает места в магазине")
                elif isinstance(self, Store):
                    print("Не хватает места на складе")
                return False

    def add_product(self, name, count):
        if self.get_free_space() >= int(count):
            print("Товар добавлен")
            self.__items[name] = int(count)
            return True
        else:
            if isinstance(self, Shop):
                print("Не хватает места в магазине")
            elif isinstance(self, Store):
                print("Не хватает места на складе")
            return False

    def remove(self, name, count):
        if self.__items[name] >= int(count):
            print("Нужное количество есть на складе")
            self.__items[name] -= int(count)
            return True
        else:
            print("Не хватает товара на складе")
            return False

    def get_free_space(self):
        current_space = 0
        for value in self.__items.values():
            current_space += value
        return self.__capacity - current_space

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items.keys())

    def __str__(self):
        st = "\n"
        for key, value in self.__items.items():
            st += f"{key}:{value}\n"
        return st


class Shop(Store):
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, count):
        if self.get_unique_items_count() >= 5:
            print("Слишком много уникальных товаров")
            return False
        else:
            super().add(name, count)


class Request:
    def __init__(self, request_str):
        request_list = request_str.split()
        action = request_list[0]
        self.__count = request_list[1]
        self.__items = request_list[2]

        if action == "Доставить":
            self.__from = request_list[4]
            self.__to = request_list[6]
        elif action == "Забрать":
            self.__from = request_list[4]
            self.__to = None
        elif action == "Привезти":
            self.__to = request_list[4]
            self.__from = None

    def move(self):
        if self.__to and self.__from:
            if eval(self.__to).add(self.__items, self.__count):
                eval(self.__from).remove(self.__items, self.__count)
        elif self.__to:
            eval(self.__to).add(self.__items, self.__count)
        elif self.__from:
            eval(self.__from).remove(self.__items, self.__count)


storage_1 = Store(items={"Телефон": 10, "Компьютер": 10, "Фен": 10})
shop_1 = Shop(items={"Телефон": 1, "Компьютер": 1, "Фен": 1})
