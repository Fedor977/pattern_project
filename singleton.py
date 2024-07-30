"""
1. Singleton (Одиночка)
Этот паттерн гарантирует, что класс будет иметь только один экземпляр
и предоставляет глобальную точку доступа к этому экземпляру.
"""

class Singleton:
    _instance = None  # Приватная переменная для хранения единственного экземпляра

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # Проверка, существует ли уже экземпляр
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance  # Возврат единственного экземпляра

singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # True, т.к. оба указывают на один и тот же экземпляр
