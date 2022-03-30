from fratercula import Fratercula
import uuid
from datetime import datetime
date = datetime.now()
a = Fratercula("Сокол", "Fratercula arctica arctica", 200, 15, 2019, "Арктика", uuid)

print(f"""Кличка - {a.name}, Подвид - {a.subspecies}, Вес - {a.weight}, Рост - {a.growth}, \
Возраст - {date.year - a.year_of_birth} , Среда обитания - {a.habitat}, ID - {a.id}""")