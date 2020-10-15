try:
  a = (int(input('점수를 입력해주세요: ')))

  if a > 100 or a < 0 :
    print('점수를 확인해주세요')

  elif 90 < a <= 100:
    print('A')
  elif 80 < a <= 90:
    print('B')
  elif 70 < a <= 80:
    print('C')
  elif 60 < a <= 70:
    print('D')
  else:
    print('F')
  
except ValueError:
  print('입력이 잘못되었습니다. 숫자(정수)만 입력해줴요')