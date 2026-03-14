from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from datetime import datetime


class SocialNetwork(ABC):
    """
    Базовый абстрактный класс для социальных сетей.

    Определяет общие атрибуты и методы для всех социальных сетей.
    Некоторые атрибуты сделаны непубличными для защиты данных пользователя.
    """

    def __init__(self, name: str, user_id: str, email: str) -> None:
        """
        Инициализация базового класса социальной сети.

        Args:
            name: Название социальной сети
            user_id: Идентификатор пользователя
            email: Email пользователя (непубличный атрибут для защиты)
        """
        self.name = name
        self._user_id = user_id  # защищённый атрибут, чтобы предотвратить прямой доступ
        self.__email = email  # приватный атрибут для конфиденциальности
        self._posts: List[str] = []  # защищённый список постов
        self.friends_count: int = 0

    @property
    def email(self) -> str:
        """Геттер для приватного email с маскировкой для безопасности."""
        return self.__email[:3] + "***" + self.__email[self.__email.find('@'):]

    def add_post(self, content: str) -> None:
        """
        Добавляет новый пост в ленту.

        Args:
            content: Текст поста
        """
        self._posts.append(content)
        print(f"Пост добавлен в {self.name}: {content[:30]}...")

    def get_posts(self) -> List[str]:
        """
        Возвращает список всех постов пользователя.

        Returns:
            List[str]: Список постов
        """
        return self._posts.copy()  # возвращаем копию для защиты исходных данных

    @abstractmethod
    def share_content(self, content: str, visibility: str = "public") -> bool:
        """
        Абстрактный метод для публикации контента.
        Каждая соцсеть реализует свою логику публикации.

        Args:
            content: Контент для публикации
            visibility: Уровень видимости (public, friends, private)

        Returns:
            bool: Успешность публикации
        """
        pass

    def __str__(self) -> str:
        """
        Магический метод для пользовательского строкового представления.

        Returns:
            str: Информация об аккаунте в соцсети
        """
        return f"{self.name} аккаунт: {self._user_id} | Друзья: {self.friends_count}"

    def __repr__(self) -> str:
        """
        Магический метод для технического представления объекта.

        Returns:
            str: Техническая информация об объекте
        """
        return f"SocialNetwork(name='{self.name}', user_id='{self._user_id}', friends={self.friends_count})"


class VK(SocialNetwork):
    """
    Дочерний класс для социальной сети ВКонтакте.
    Расширяет базовый класс специфическими для VK функциями.
    """

    def __init__(self, user_id: str, email: str, phone: Optional[str] = None) -> None:
        """
        Инициализация аккаунта VK.

        Args:
            user_id: ID пользователя VK
            email: Email пользователя
            phone: Номер телефона (специфично для VK, непубличный)
        """
        # Расширяем конструктор базового класса
        super().__init__("VK", user_id, email)
        self._phone = phone  # защищённый атрибут
        self.audio_playlists: List[str] = []  # специфично для VK
        self._wall_visibility: str = "all"  # настройки стены

    def share_content(self, content: str, visibility: str = "public") -> bool:
        """
        Перегруженный метод для публикации в VK.

        Причина перегрузки: VK имеет специфические настройки приватности
        и возможность прикреплять музыку/видео.

        Args:
            content: Контент для публикации
            visibility: Уровень видимости (public, friends, private, custom)

        Returns:
            bool: Успешность публикации
        """
        if visibility not in ["public", "friends", "private", "custom"]:
            print("Ошибка: недопустимый уровень видимости для VK")
            return False

        # В VK можно прикреплять музыку к постам
        if self.audio_playlists:
            content += f"\n[прикреплён плейлист: {', '.join(self.audio_playlists[:2])}]"

        self.add_post(content)
        print(f"[VK] Опубликовано с видимостью: {visibility}")
        return True

    def add_playlist(self, playlist_name: str) -> None:
        """
        Специфичный для VK метод добавления плейлиста.

        Args:
            playlist_name: Название плейлиста
        """
        self.audio_playlists.append(playlist_name)

    def __str__(self) -> str:
        """
        Перегруженный магический метод для VK.

        Returns:
            str: Расширенная информация об аккаунте VK
        """
        base_info = super().__str__()
        phone_info = f", Телефон: {self._phone[:4]}***" if self._phone else ""
        return f"{base_info} | Плейлистов: {len(self.audio_playlists)}{phone_info}"

    def __repr__(self) -> str:
        """
        Перегруженный магический метод для технического представления VK.

        Returns:
            str: Техническая информация об объекте VK
        """
        return f"VK(user_id='{self._user_id}', email='{self.email}', phone={self._phone is not None})"


class Facebook(SocialNetwork):
    """
    Дочерний класс для социальной сети Facebook.
    Расширяет базовый класс специфическими для Facebook функциями.
    """

    def __init__(self, user_id: str, email: str, real_name: str) -> None:
        """
        Инициализация аккаунта Facebook.

        Args:
            user_id: ID пользователя Facebook
            email: Email пользователя
            real_name: Реальное имя (специфично для Facebook)
        """
        # Расширяем конструктор базового класса
        super().__init__("Facebook", user_id, email)
        self._real_name = real_name  # защищённый атрибут
        self.events: List[Dict[str, Any]] = []  # специфично для Facebook
        self._reactions: Dict[str, int] = {"like": 0, "love": 0, "wow": 0}

    def share_content(self, content: str, visibility: str = "public") -> bool:
        """
        Перегруженный метод для публикации в Facebook.

        Причина перегрузки: Facebook требует указания реального имени
        и имеет другую систему приватности.

        Args:
            content: Контент для публикации
            visibility: Уровень видимости (public, friends, only_me, custom)

        Returns:
            bool: Успешность публикации
        """
        if visibility not in ["public", "friends", "only_me", "custom"]:
            print("Ошибка: недопустимый уровень видимости для Facebook")
            return False

        # В Facebook публикация идёт от реального имени
        content = f"{self._real_name} поделился: {content}"

        self.add_post(content)
        print(f"[Facebook] Опубликовано с видимостью: {visibility}")
        return True

    def create_event(self, event_name: str, date: datetime) -> None:
        """
        Специфичный для Facebook метод создания события.

        Args:
            event_name: Название события
            date: Дата проведения
        """
        self.events.append({
            "name": event_name,
            "date": date,
            "participants": []
        })

    def add_reaction(self, reaction_type: str) -> None:
        """
        Добавляет реакцию на пост (специфично для Facebook).

        Args:
            reaction_type: Тип реакции (like, love, wow)
        """
        if reaction_type in self._reactions:
            self._reactions[reaction_type] += 1

    def __str__(self) -> str:
        """
        Перегруженный магический метод для Facebook.

        Returns:
            str: Расширенная информация об аккаунте Facebook
        """
        base_info = super().__str__()
        return f"{base_info} | Реальное имя: {self._real_name} | Событий: {len(self.events)}"

    def __repr__(self) -> str:
        """
        Перегруженный магический метод для технического представления Facebook.

        Returns:
            str: Техническая информация об объекте Facebook
        """
        return f"Facebook(user_id='{self._user_id}', real_name='{self._real_name}')"

if __name__ == "__main__":
    # Write your solution here
    # Пример использования (раскомментируйте для тестирования):
    # Создаём экземпляры классов
    vk_user = VK("durov", "pavel@vk.com", "+79161234567")
    fb_user = Facebook("zuck", "mark@fb.com", "Mark Zuckerberg")

    # Демонстрация работы
    vk_user.friends_count = 100500
    fb_user.friends_count = 50000000

    # Тестируем методы
    vk_user.share_content("Программирую на Python!", "friends")
    vk_user.add_playlist("Rock Hits")

    fb_user.share_content("Изучаю наследование в Python", "public")
    fb_user.create_event("Python Meetup", datetime(2024, 12, 25))

    # Вывод информации
    print(vk_user)
    print(fb_user)
    print(repr(vk_user))
    print(repr(fb_user))

    # Демонстрация инкапсуляции
    print(f"Email VK (маскированный): {vk_user.email}")
    # print(vk_user.__email)  # Ошибка! Нельзя получить доступ к приватному атрибуту
    # print(vk_user._phone)    # Можно, но не рекомендуется (защищённый атрибут)
    pass
