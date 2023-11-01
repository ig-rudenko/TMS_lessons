d = {
    "type": "FeatureCollection",  # Обязательный параметр
    "features": [  # Список данных для отображения на карте
        {
            "type": "Feature",  # Обязательный параметр
            "id": "cityID",  # Идентификатор берем из данных города
            "geometry": {
                "type": "Point",  # Обязательно Point
                "coordinates": [-65.23, 123.11],
            },
            "properties": {
                "iconCaption": "name",  # Название города
                "marker-color": "#b51eff",  # Цвет метки
            },
        },
        ...,  # Другие элементы коллекции
    ],
}

import json


geo = {
    "type": "FeatureCollection",
    "features": [],
}


with open("city.list.json", encoding="utf-8") as file:
    data = json.load(file)
    # Список городов отдельной страны
    nl_cities = list(filter(lambda x: x["country"] == "NL", data))

    for city in nl_cities[:100]:
        geo["features"].append(
            {
                "type": "Feature",
                "id": city["id"],
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        city["coord"]["lon"],
                        city["coord"]["lat"],
                    ],
                },
                "properties": {
                    "iconCaption": city["name"],
                    "marker-color": "#b51eff",
                },
            }
        )

with open("cities.geojson", "w", encoding="utf-8") as file:
    json.dump(geo, file, ensure_ascii=False)



res = {}

with open("city.list.json", encoding="utf-8") as file:
    data = json.load(file)

    for city in data:
        if city["country"] not in res:
            res[city["country"]] = 1
        else:
            res[city["country"]] += 1
