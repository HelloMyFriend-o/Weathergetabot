# Weather emoji dictionary.
weather_icons = {
    '01d': '☀',
    '02d': '🌤',
    '03d': '⛅',
    '04d': '🌥',
    '09d': '🌧',
    '10d': '🌦',
    '11d': '🌩',
    '13d': '🌨',
    '50d': '🌫',
    '01n': '🌖',
    '02n': '🌖',
    '03n': '🌖',
    '04n': '☁',
    '09n': '🌧',
    '10n': '🌦',
    '11n': '🌩',
    '13n': '🌨',
    '50n': '🌫',
}
# Celsius degree sign.
degree = '\u2103'

# needed for correct temperature display.
sign = lambda x: "+" if x >= 1 else ""

# Hectopascal to mmHg conversion.
hpa_to_mmhg = 0.75

unspecified_city = 'Вначале введите город\n\n' \
                   'Например:\n' \
                   'город Казань\n' \
                   'город Санкт-Петербург\n' \
                   'город Нижний Новгород'
