# 2 ~ 5단 세로출력
count = 1

while count < 3:
  if count < 2:
    for i in range(1,10):
      print()
      for j in range(2,6):
        print(f"{j} * {i} = {j * i}", end="\t")
    count += 1
  else:
    print()
    for i in range(1,10):
      print()
      for j in range(6, 10):
        print(f"{j} * {i} = {i * j}", end="\t")
    count += 1
    