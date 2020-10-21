import os
import pickle
import gzip
import random
import json


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
      with open("stduent.json", 'w') as file:
        file.write('[]')
        return
    
def load_std_info():
    pass

def add_id():
  count:int = 0
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
      
      obj = {}
      obj[input_data_to_number] = []
      print(f"학번 '{input_data_to_number}'가 입력되었습니다")
      # ---- data 처리 ---- #
      with open('stduent.json', 'r') as file:
        data = eval(file.read())
        data.append(obj)
        with open('stduent.json', 'w') as files:
          files.write(json.dumps(data))
          return
      
    except ValueError:
      print('학번의 형태가 맞지 않습니다(숫자8자리). 다시 입력하세요')
      count += 1

def add_score():
    id_count: int = 0
    score_count: int = 0
    
    while True:
      try:
        if id_count >= 3:
          # 학번 3번이상 입력시 초기화면
          return
        
        input_data:str = input("학생 학번을 입력해주세요: ")
        # 숫자변환 시 error확인
        input_data_to_number:int = int(input_data)
        if len(input_data) != 8:
          print('학번의 형태가 맞지 않습니다(숫자8자리). 다시 입력하세요')
          id_count += 1
          continue
        with open('stduent.json', 'r') as file:
          try:
            data = eval(file.read())
            for stu_data in data:
              for key, value in stu_data.items():
                if int(key) == input_data_to_number:
                  print(f'{input_data_to_number}의 학생의 리스트값 {value}')
                  while True:
                    if score_count >= 3:
                      # stu_data[key] = value
                      with open('stduent.json', 'w') as files:
                        files.write(json.dumps(data))
                        return
                    input_score:str = input("점수를 입력해주세요: ")
                    iuput_score_number:int = int(input_score)
                    if iuput_score_number > 100:
                      print('점수가 잘못 입력되었습니다.')
                      value.append(0)
                      score_count += 1
                      continue
                    # 해당학번 리스트에 입력받은 점수 입력
                    value.append(iuput_score_number)
                    stu_data[key] = value
                    with open('stduent.json', 'w') as files:
                      print('점수가 입력되었습니다.')
                      files.write(json.dumps(data))
                      return
          except ValueError:
            print('점수가 잘못 입력되었습니다.')
            value.append(0)
            stu_data[key] = value
      except ValueError:
        print('학번의 형태가 맞지 않습니다(숫자8자리). 다시 입력하세요')
        id_count += 1
    
def remove_id():
    pass

def remove_score():
    pass

def save_data():
    pass

def print_std_info():
    pass

if __name__ == "__main__":
    while(True):
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
            pass
        elif address == 3:
            add_id()
        elif address == 4:
            add_score()
        elif address == 5:
            pass
        elif address == 6:
            pass
        elif address == 7:
            pass
        elif address == 8:
            pass
        elif address == 9:
            pass
        else:
            print("올바른 명령어를 입력해주세요")
            continue

# def write_data(data):
  
