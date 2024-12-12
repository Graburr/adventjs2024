import re
# Trying all test by hand works fine but when upload it, doesn't work
def compile(instructions):
  variables = {}
  i = 0
  instruction : list[str] = None

  operators = {
    "MOV": lambda variable: variables.update({instruction[2]: 
                                              int(variable) if re.search("-?[0-9]+", variable)
                                              else variables[variable]}),
    "JMP": lambda variable: int(instruction[2]) if variables[variable] == 0 else i + 1, 
    "INC": lambda variable: variables.update({variable: variables.get(variable, 0) + 1}),
    "DEC": lambda variable: variables.update({variable: variables.get(variable, 0) - 1}),
  }
  

  while i < len(instructions):
    instruction = instructions[i].split()
    
    if instruction[0] != "JMP":
      operators[instruction[0]](instruction[1])
      i += 1
    else:
      i = operators[instruction[0]](instruction[1])

  return variables.get("A", None)
