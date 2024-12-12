# 5 stars
def calculate_price(ornaments: str) -> int:
    values = {'*' : 1, 'o' : 5, '^' : 10, '#' : 50, '@' : 100}
    result = 0

    for i in range (1, len(ornaments)):
        if not ornaments[i] in values.keys():
            return undefined # Library Undefined imported by the webpage of adventjs2024
        last = values[ornaments[i]]

        result = (result + values[ornaments[i - 1]] if values[ornaments[i]] <= values[ornaments[i - 1]] 
                 else result - values[ornaments[i - 1]])

    return result + values[ornaments[-1]]