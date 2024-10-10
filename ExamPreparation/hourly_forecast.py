def forecast(*args):
    weather = {}
    weather_order = ["Sunny", "Cloudy", "Rainy"]
    result = ""
    for city, conditions in args:
        if conditions not in weather:
            weather[conditions] = []
        weather[conditions].append(city)

    sorted_weather = dict(sorted(weather.items(), key=lambda kvp: weather_order.index(kvp[0])))

    for key in sorted_weather:
        sorted_weather[key] = sorted(sorted_weather[key])

    for condition, cities in sorted_weather.items():
        for city in cities:
            result += f"{city} - {condition}\n"

    return result
