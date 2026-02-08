# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class BankAccount:
    def __init__(self, account_number: str, owner: str, initial_balance: float = 0.0):
        """

        :param account_number: Номер счета
        :param owner: Владелец счета
        :param initial_balance: Начальный баланс (по умолчанию 0.0)

        Примеры:
        >>> account = BankAccount("123456789", "Иван Иванов", 1000.0)
        """
        if not isinstance(account_number, str):
            raise TypeError("Номер счета должен быть строкой")
        if not account_number:
            raise ValueError("Номер счета не может быть пустым")
        self.account_number = account_number

        if not isinstance(owner, str):
            raise TypeError("Владелец счета должен быть строкой")
        if not owner:
            raise ValueError("Владелец счета не может быть пустым")
        self.owner = owner

        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Баланс должен быть типа int или float")
        if initial_balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        """
        Внесение денег на счет

        :param amount: Сумма для внесения
        :raise ValueError: Если сумма отрицательная

        Примеры:
        >>> account = BankAccount("123456789", "Иван Иванов", 1000.0)
        >>> account.deposit(500.0)
        >>> account.balance
        1500.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if amount <= 0:
            raise ValueError("Сумма для внесения должна быть положительной")

        self.balance += amount

    def withdraw(self, amount: float) -> float:
        """
        Снятие денег со счета

        :param amount: Сумма для снятия
        :return: Фактически снятая сумма
        :raise ValueError: Если сумма отрицательная или превышает баланс

        Примеры:
        >>> account = BankAccount("123456789", "Иван Иванов", 1000.0)
        >>> account.withdraw(300.0)
        300.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть положительной")

        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")

        self.balance -= amount
        return amount

    def get_balance(self) -> float:
        """
        Получение текущего баланса

        :return: Текущий баланс счета

        Примеры:
        >>> account = BankAccount("123456789", "Иван Иванов", 1000.0)
        >>> account.get_balance()
        1000.0
        """
        return self.balance


class Thermos:
    def __init__(self, capacity_volume: float, temperature: float, liquid_type: str):
        """
        Создание и подготовка к работе объекта "Термос"

        :param capacity_volume: Объем термоса в мл
        :param temperature: Температура жидкости в градусах Цельсия
        :param liquid_type: Тип жидкости (чай, кофе, вода и т.д.)

        Примеры:
        >>> thermos = Thermos(750, 85.5, "чай")  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем термоса должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем термоса должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть типа int или float")
        self.temperature = temperature

        if not isinstance(liquid_type, str):
            raise TypeError("Тип жидкости должен быть строкой")
        self.liquid_type = liquid_type

    def check_temperature(self) -> str:
        """
        Проверка температуры жидкости в термосе

        :return: Описание температуры (холодная, теплая, горячая)

        Примеры:
        >>> thermos = Thermos(750, 85.5, "чай")
        >>> thermos.check_temperature()
        'горячая'
        """
        if self.temperature < 20:
            return "холодная"
        elif self.temperature < 60:
            return "теплая"
        else:
            return "горячая"

    def change_temperature(self, delta: float) -> None:
        """
        Изменение температуры жидкости в термосе

        :param delta: Изменение температуры в градусах Цельсия
        :raise ValueError: Если температура станет отрицательной

        Примеры:
        >>> thermos = Thermos(750, 85.5, "чай")
        >>> thermos.change_temperature(-10.5)
        """
        if not isinstance(delta, (int, float)):
            raise TypeError("Изменение температуры должно быть типа int или float")

        new_temperature = self.temperature + delta
        if new_temperature < 0:
            raise ValueError("Температура не может быть отрицательной")

        self.temperature = new_temperature


class Bottle:
    def __init__(self, capacity_volume: float, occupied_volume: float, material: str):
        """
        Создание и подготовка к работе объекта "Бутылка"

        :param capacity_volume: Объем бутылки в мл
        :param occupied_volume: Объем занимаемой жидкости в мл
        :param material: Материал бутылки (стекло, пластик, металл)

        Примеры:
        >>> bottle = Bottle(1000, 500, "стекло")  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем бутылки должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем бутылки должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        if occupied_volume > capacity_volume:
            raise ValueError("Количество жидкости не может превышать объем бутылки")
        self.occupied_volume = occupied_volume

        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        self.material = material

    def is_empty_bottle(self) -> bool:
        """
        Функция которая проверяет является ли бутылка пустой

        :return: True если бутылка пуста, иначе False

        Примеры:
        >>> bottle = Bottle(1000, 0, "стекло")
        >>> bottle.is_empty_bottle()
        True
        """
        return self.occupied_volume == 0

    def add_liquid(self, liquid: float) -> None:
        """
        Добавление жидкости в бутылку.

        :param liquid: Объем добавляемой жидкости в мл
        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в бутылке

        Примеры:
        >>> bottle = Bottle(1000, 500, "стекло")
        >>> bottle.add_liquid(300)
        """
        if not isinstance(liquid, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if liquid < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом")

        if self.occupied_volume + liquid > self.capacity_volume:
            raise ValueError("Недостаточно места в бутылке")

        self.occupied_volume += liquid

    def remove_liquid(self, amount: float) -> float:
        """
        Извлечение жидкости из бутылки.

        :param amount: Объем извлекаемой жидкости в мл
        :return: Объем реально извлеченной жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество жидкости в бутылке

        Примеры:
        >>> bottle = Bottle(1000, 500, "стекло")
        >>> bottle.remove_liquid(200)
        200
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Извлекаемая жидкость должна быть типа int или float")
        if amount < 0:
            raise ValueError("Извлекаемая жидкость должна быть положительным числом")

        if amount > self.occupied_volume:
            raise ValueError("Недостаточно жидкости в бутылке")

        self.occupied_volume -= amount
        return amount


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
