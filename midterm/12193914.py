import os
import pickle
import gzip
import random
import json

from typing import List, Dict

global all_data  # 전역변수설정

print('시작')
def make_data():
#   1. 학생 데이터를 만드는 코드. 
# 2. “저장경로를 입력하세요”라는 커맨드 입력받고, 경로를 입력
# 하지 않을 시 현재 경로를 입력해 줌. w 만일 해당 경로에 json 파일이 있다면, “경로에 해당 파
# 일이 있습니다.”라는 말과 함께 3번 잘못 입력 시 초기
# 화면을 보여줌
  count = 0
  json_file = False
  
  while True:
    if count == 3:
      return
    route = input("저장경로를 입력하세요: ")
    
    if route == "":
      os.chdir(os.getcwd())
    else:
      os.chdir(route)
    
    work_dir = os.listdir(os.getcwd())
    
    for i in work_dir:
      filename, fileExtension = os.path.splitext(i)
      if fileExtension == '.json':
        json_file = True
  
      if(json_file):
        count += 1
        print("경로에 해당 파일이 있습니다.!!!!")
        break
      
    if json_file == False:
      with open("test2.json", 'w') as file:
        file.write("{}")
        return
    

def load_std_info():
  
  check = False
  router = input("파일을 포함하여 불러올 경로를 입력해주세요: ")
  # 입력받은 dir로 이동

  # 입력값에서 .json 파일 추출
  input_file = router.split('/')[len(router.split('/'))-1]

  split_file = router.split('/')
  
  split_file.pop()
  # 입력받은 디렉토리
  input_dir = "/".join(split_file)
  # 입력받은 router로 현재 디렉토리 이동
  change_current_dir = os.chdir(input_dir)

  work_dir = os.listdir(change_current_dir)
  try:
    ## 현재 디렉토리에 해당 json 파일이 있는지 확인!
    for i in work_dir:
      if i == input_file:
        with open(input_file, 'rb') as file:
          check = True
          read_data = pickle.load(file)
          print(read_data)
          
          return read_data
    if not check:
      # 해당경로에 입력받은 파일이 없을경우
      print("파일이 없습니다.")
      with open(input_file, 'wb') as file:
        a = pickle.dumps({})
        file.write(a)
        return dict()
  except EOFError:
    return dict()
    
          
def add_id():
  count:int = 0
  global all_data
  all_data = load_std_info()
  print(all_data)
  while True:
    try:
      if count >= 3:
        return
      input_data:str = input("학생 학번을 입력해주세요: ")
      # 숫자변환 시 error확인
      input_data_to_number:int = int(input_data)
      
      if len(input_data) > 8:
        print('학번의 형태가 맞지 않습니다(숫자8자리). 다시 입력하세요')
        count += 1
        continue
      
      print(f"학번 '{input_data_to_number}'가 입력되었습니다")
      # ---- data 처리 ---- #
      all_data[input_data_to_number] = []
      
      print(all_data)
      return 
    except ValueError:
      print('학번의 형태가 맞지 않습니다(숫자8자리). 다시 입력하세요')
      count += 1

def add_score():
    id_count: int = 0
    score_count: int = 0
    # 만약 학생학번이 딕셔너리에 없을경우도 에러처리를 해야되는지?
    # 조건에는 없으니 딕셔너리에는 무조건 학번이 있다고 가정
    global all_data
    print(all_data)
    
    while True:
      try:
        if id_count >= 3:
          # 학번 3번이상 입력시 초기화면
          return
        
        input_data:str = input("학생 학번을 입력해주세요: ")
        
        # 학생점수 리스트로 출력
        print(f'{input_data} 학생의 점수 리스트입니다. {all_data[int(input_data)]}')
        # 숫자변환 시 error확인
        input_data_to_number:int = int(input_data)
        if len(input_data) != 8:
          print('학번의 형태가 맞지 않습니다(숫자8자리). 다시 입력하세요')
          id_count += 1
          continue
        while True:
          try:
            if score_count >= 3:
              return
            score_data = int(input("점수를 입력해주세요"))
            print(all_data)
            for i in all_data:
              if int(i) == input_data_to_number:
                if score_data > 100:
                  score_count += 1
                  # 만일 100 초과의 입력이나 숫자가 아닌경우는 “점수가잘못되었습니다.”라는 말과 함께 0점 입력.
                  print('점수가 잘못되었습니다.')
                  all_data[i].append(0)
                  continue
                print('입력되었습니다.')
                all_data[i].append(score_data)
              return
          except ValueError:
            for i in all_data:
              if int(i) == input_data_to_number:
                score_count += 1
                  # 만일 100 초과의 입력이나 숫자가 아닌경우는 “점수가잘못되었습니다.”라는 말과 함께 0점 입력.
                print('점수가 잘못되었습니다.')
                all_data[i].append(0)
        
      except ValueError:
        print('학번의 형태가 맞지 않습니다(숫자8자리). 다시 입력하세요')
        id_count += 1
    
def remove_id():
    count:int = 0
    global all_data
    print(all_data)
    while True:
      if count == 3:
        return
      try:
        select_id: str = input("제거할 학번을 입력해주세요")
        select_id_num: int = int(select_id)
        
        if len(select_id) != 8:
          count += 1
          print("학번의 형태가 맞지 않습니다(숫자 8자리). 다시 입력 하세요")
          continue
        
        for i in all_data:
          if i == select_id_num:
            del all_data[i]
            return
          
      except ValueError:
        count += 1
        print('학번의 형태가 맞지 않습니다.(숫자 8자리) 다시 입력 하세요')

def remove_score():
  count: int = 0
  score_count: int = 0
  while True:
    if count == 3:
      return
    try:
      input_id: str = input("학번을 입력해주세요: ")
      input_id_num: int = int(input_id)
      
      if len(input_id) != 8:
        count += 1
        print("학번의 형태가 맞지 않습니다(숫자 8자리). 다시 입력 하세요")
        continue
      
      while True:
        if score_count == 3:
          return
        print(f"학번 {input_id_num}의 성적리스트는 {all_data[input_id_num]} 다음과 같습니다.")
        # 제거할 입력 순서 받기
        # 여기서는 무조건 숫자로 입력받기 따로 조건이 따로없음 인덱스범위만 초과하는지에 대한 에러처리만 있으면 됨
        remove_index = int(input("제거할 점수의 순서를 입력하세요"))
        score_data_length_check = len(all_data[input_id_num]) # 배열의 길이 확인
        
        if score_data_length_check < remove_index:
          print("올바른 범위를 선택해주세요")
          score_count += 1
          continue
        
        # 순서는 1부터 시작으로 설정
        del all_data[input_id_num][remove_index-1] # 배열에서 해당값지우기
      
        print(all_data)
        return
    except ValueError:
      print('hree')
      count += 1
      print('학번의 형태가 맞지 않습니다.(숫자 8자리) 다시 입력 하세요')
    
    
def save_data():
  # 학생정보를 저장하는코드
  # 아마 현재 전역변수에 있는 딕셔너리를 .json파일로 저장하는 코드
  
  # ---- 의문점 ---- # 
  # 파일이름은 ? => 1. test.json 임의로 지정() 2. 이것마저도 입력을 받을껀지(근데 요구사항에 없음)
  # 해당디렉토리에 .json파일이 여러개 있을경우(조건에 없음) ex) test.json, example.json, asdad.json => test로만 시작하는 json파일만 있다고 가정
  # ---- 의문점 ---- #
  

  # 입력값에서 .json 파일 추출
  # change_current_dir = os.chdir(input_dir)
  # work_dir = os.listdir(change_current_dir)
  try: 
    global all_data
    
    json_file_check = False
    input_router: str = input("저장 경로를 입력해주세요: ")
    select_file_name: str = input("저장할 파일 이름을 지정하세요. 파일명만 적어주세요")
    
    # 입력받은 라우터로 현재 디렉토리 이동
    os.chdir(input_router)
    
    work_dir = os.listdir(os.getcwd())
    try:
      for i in work_dir:
        filename, fileExtension = os.path.splitext(i)
        if fileExtension == '.json':
          # _있을떄와 없을때를 비교해서 적기
          split_file: str = i.split('.')
          split_file2: list = list(split_file[0])
          if '_' in split_file2:
            split_file2[-1]: str = str(int(split_file2[-1]) + 1)
            split_file3: list = "".join(split_file2)
            save_file_name: str = split_file3 + fileExtension
            
            with open(save_file_name, "wb") as file:
              json_file_check = True
              file.write(pickle.dumps(all_data))
              file.close()
              return
          else:
            split_file2 = split_file[0]+ "_1"
            save_file_name = split_file2 + fileExtension
            
            with open(save_file_name, "wb") as file:
              json_file_check = True
              file.write(pickle.dumps(all_data))
              file.close()
              return
            
      if not json_file_check:
        save_file_name = select_file_name + ".json"
        with open(save_file_name, "wb") as file:
          file.write(pickle.dumps(all_data))
          file.close()
          return
    except NameError:
      print('데이터가 비었습니다. 성적 및 학번을 먼저 입력해주세요.')
      add_id()
      return
  except FileNotFoundError:
    print('파일경로를 다시 확인해주세요')
    return
def print_std_info():
  # 파일을 불러와서 데이터를 출력하는건지?
  # 그냥 메모리에 있는 데이터를 불러와서 출력하면 되는건지? => 이 조건으로
  global all_data
  count:str = 0
  
  while True:
    if count == 3:
      for i in all_data:
        print("f 해당가능한 값 => 학번: {i} 리스트: {all_data[i]}")
      count = 0
    try:
      input_id: str = input("학번을 입력해주세요.")
      input_id_num: int = int(input_id)
      
      if len(input_id) != 8:
        count += 1
        print("학번의 형태가 맞지 않습니다(숫자 8자리). 다시 입력 하세요")
        continue
      try:
        if input_id_num == 0:
          for i in all_data:
            print(f"학번: {i}")
            # 숫자로 이루어진 요소를 문자열로 바꾸기
            value: list = all_data[i]
            value: list = list(map(str,value))
            value: str = "  ".join(value)
            print(f"점수: {value}")
        else:
          for i in all_data:
            if i == input_id_num:
              print(f"{i}학생의 점수 리스트입니다. {all_data[i]}")
              return
      except NameError:
        print('데이터가 비었습니다. 성적 및 학번을 먼저 입력해주세요.')
        add_id()
        return
      
    except ValueError:
      count += 1
      print("학번의 형태가 맞지 않습니다(숫자 8자리). 다시 입력 하세요")
    

if __name__ == "__main__":
    while(True):
        # global all_data
        # print(all_data)
        print("-------------학생성적표-----------")
        print("1. 만들기")
        print("2. 불러오기")
        print("3. 학번입력하기")
        print("4. 성적입력하기")
        print("5. 학번제거하기")
        print("6. 성적제거하기")
        print("7. 저장하기")
        print("8. 학생 점수 조회")
        print("9. 종료")
        print("데이터 입력 ")
        
        address = int(input("명령어를 입력하세요"))
        if address == 1:
            make_data()
        elif address == 2:
            load_std_info()
        elif address == 3:
            add_id()
        elif address == 4:
            add_score()
        elif address == 5:
            remove_id()
        elif address == 6:
            remove_score()
        elif address == 7:
            save_data()
        elif address == 8:
            pass
        elif address == 9:
            pass
        else:
            print("올바른 명령어를 입력해주세요")
            continue

# def write_data(data):
  
