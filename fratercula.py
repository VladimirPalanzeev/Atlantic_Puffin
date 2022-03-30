from datetime import datetime
import uuid

class Fratercula:
    """Основные характеристики тупиков"""
    def __init__(self, name, subspecies ,weight, growth,\
                 year_of_birth, habitat, id):
        self.name = name                          # Кличка
        self.subspecies = subspecies              # Подвид
        self.weight = weight                      # Вес
        self.growth = growth                      # Рост
        self.year_of_birth = year_of_birth        # Год рождения
        self.habitat = habitat                    # Среда обитания
        self.id = id.uuid4()                      # Уникальный идентификатор

    def age(self, year_of_birth):
        date = datetime.now()
        return date.year - year_of_birth

