class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Геттер для названия книги (только для чтения)."""
        return self._name

    @property
    def author(self) -> str:
        """Геттер для автора книги (только для чтения)."""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    @property
    def pages(self) -> int:
        """Геттер для количества страниц."""
        return self.pages

    @pages.setter
    def pages(self, value: int):
        """Сеттер для количества страниц с проверкой."""
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
        
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Аудиокнига. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Используем сеттер для проверки

    @property
    def duration(self) -> float:
        """Геттер для продолжительности."""
        return self._duration

    @duration.setter
    def duration(self, value: float):
        """Сеттер для продолжительности с проверкой."""
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = float(value)

    def __str__(self):
        # Переопределяем __str__ чтобы включить информацию о длительности
        return f"Аудиокнига {self.name}. Автор {self.author}. Длительность: {self.duration} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
