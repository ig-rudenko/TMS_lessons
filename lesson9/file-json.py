# JSON
# +-----------+----------------+
# |   JSON    |     Python     |
# +-----------+----------------+
# | String    | str            |
# | Number    | int or float   |
# | Boolean   | bool           |
# | Array     | list           |
# | Object    | dict           |
# | null      | NoneType       |
# +-----------+----------------+

import json

address1 = {
    "region": "Земля♥",
    "settlement": None,
    "city": "Садовой",
    "plan_structure": None,  # Садовое товарищество
    "street": ["ул. Вишневая"],
    "building": "22",
    "is_building": False,
    "block": None,  # Корпус
}

print("# ============ Сериализация в JSON =================")
# Представление данных в виде строки
# ТОЛЬКО ASCII
# json_address1: str = json.dumps(address1)

# Сохраняем исходную кодировку
json_address1: str = json.dumps(address1, ensure_ascii=False)
print(type(json_address1))
print(json_address1)

with open("test.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_address1)

print("# ============ Десериализация из JSON =================")
address_original = json.loads(json_address1)

print(type(address_original))
print(address_original)
