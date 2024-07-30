"""
3. Observer (Наблюдатель)
Паттерн Наблюдатель определяет зависимость "один ко многим" между объектами таким образом,
что при изменении состояния одного объекта все зависимые объекты уведомляются
и обновляются автоматически.
"""

class Subject:
    def __init__(self):
        self._observers = []  # Список наблюдателей

    def attach(self, observer):
        self._observers.append(observer)  # Добавление наблюдателя

    def detach(self, observer):
        self._observers.remove(observer)  # Удаление наблюдателя

    def notify(self):
        for observer in self._observers:
            observer.update(self)  # Уведомление всех наблюдателей

class Observer:
    def update(self, subject):
        raise NotImplementedError  # Базовый метод, который должен быть переопределён

class ConcreteObserver(Observer):
    def update(self, subject):
        print(f"Observer notified by {subject}")  # Реализация метода обновления

subject = Subject()
observer = ConcreteObserver()
subject.attach(observer)
subject.notify()  # Уведомление всех наблюдателей
