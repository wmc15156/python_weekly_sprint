import json

# 먼저 객체에 2 ~ 9단을 만들어서 json.dumps를 이용

dic = dict()

for i in range(2,10):
  arr = list()
  for j in range(1,10):
    #리스트에 곱한값을 다 넣기
    arr.append(i*j)
  # 2중 for문 끝나는 시점에 빈 디셔너리에 값 넣어주기
  dic[str(i)] = arr

# json.dumps를 이용
print(json.dumps(dic, indent=4))

