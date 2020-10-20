# 제네레이터를 이용하여 별모양 찍기

# 조건 입력값을 받아서 행 갯수 정함

# Docstring, Typehinting 사용 , 제네레이터 사용 , 함수사용

def range_gen():
  """[제네레이터 함수, __next__ 호출 시 리턴값 1씩 증가 ]

  Yields:
      [int]: [호출시 마다 i값 증가]
  """
  i: int = 0
  
  while True:
    yield i
    i += 1

def star_print(): 
  """[별을 찍어주는 함수]
  입력값을 받아 별을 찍어주는 함수
  """
  lines: int = int(input('별의 갯수를 입력해주세요: '))
  gen: dict = range_gen()

  while True:
    limit: int = gen.__next__()
    if limit >= lines:
      break
    for i in reversed(range(lines)):
      if limit < i:
        print(" ", end="")
      else:
        print("*", end="")
    print()

star_print()
    

    
  


    
  