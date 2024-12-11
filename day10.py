import re

def compile(instructions):
  variables = {}
  operators = {"INC" : (lambda value: variables[variable] = value),
              "DEC" : -1}
  i = 0

  while i < len(instructions):
    instruction = instructions[i].split()

    if instruction[0] == "MOV":
      variables[instruction[-1]] = (int(instruction[1]) if re.search("-?[0-9]+", instruction[1])
                                    else variables[instruction[1]]) 
    elif instruction[0] == "JMP":
      i = int(instruction[2]) if variables[instruction[1]] == 0 else i + 1
      continue
    else:
      variables[instruction[1]] = (variables[instruction[1]] + operators[instruction[0]] 
                                   if instruction[1] in variables else 0)
    
    i += 1

  return variables.get("A", None)

if __name__ == "__main__":
  instructions = [
    'MOV 0 A', 
    "INC A"
  ]

  print(compile(instructions))