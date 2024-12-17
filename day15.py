# Error when send it to execute: Assigment to const variable (doesn't have sense because 
# I don't use const var)
def draw_table(data: list[dict[str, str | int]]) -> str:
    keys_avaliable = list(data[0].keys())
    max_length_value_first = max(len(value[keys_avaliable[0]]) for value in data 
                                 if isinstance(value[keys_avaliable[0]], str))
    max_length_value_second = max(len(value[keys_avaliable[1]]) for value in data 
                                  if isinstance(value[keys_avaliable[1]], str))
    
    if len(keys_avaliable[0]) > max_length_value_first:
        max_length_value_first = len(keys_avaliable[0])
    if len(keys_avaliable[1]) > max_length_value_second:
        max_length_value_second = len(keys_avaliable[1])
    
    print(max_length_value_first, " ", max_length_value_second)

    border_frame = ("+" + "-" * (max_length_value_first + 2) + "+" + 
                    "-" * (max_length_value_second + 2) + "+")
    table = border_frame + "\n" 

    table += ("| " + keys_avaliable[0].capitalize() + " " * (max_length_value_first - 
              len(keys_avaliable[0])) + " | " + keys_avaliable[1].capitalize() + " " * 
              (max_length_value_second - len(keys_avaliable[1])) + " |\n")
    
    table += border_frame + "\n"

    for value in data:
        table += ("| " + value[keys_avaliable[0]] + " " * (max_length_value_first - 
                  len(value[keys_avaliable[0]])) + " | " + value[keys_avaliable[1]] + " " *
                  (max_length_value_second - len(value[keys_avaliable[1]])) + " |\n")

    return table + border_frame


print(draw_table([
  { "name": 'Alice', "city": 'London' },
  { "name": 'Bob', "city": 'Paris' },
  { "name": 'Charlie', "city": 'New York' }]))