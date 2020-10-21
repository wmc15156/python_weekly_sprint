import os
import json
import ast

# a = {1: 2}
# with open("sample.json", 'a') as file:
#   file.write('[]')

with open("sample.json", 'r') as file:
  a = eval(file.read())
  print(a)
  a.append(1)
  print(a)
  with open("sample.json", 'w') as file:
    file.write(json.dumps(a))
  # print(ast.literal_eval(file.read()))