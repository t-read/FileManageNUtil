import os
import csv

"""
이 코드는, 특정한 csv 파일에서 값을 읽어와 해당 값을 폴더 이름으로 가지는 폴더들을 생성하는 코드입니다. 
base_path 변수에 폴더를 생성할 경로를 지정하고, csv_path 변수에 생성할 폴더 이름들을 저장한 csv 파일의 경로를 지정합니다. 
그리고 csv 파일을 열어서 파일을 한 줄씩 읽어들이면서, 해당 값을 폴더 이름으로 하위 폴더들까지 생성하는 작업을 합니다.
"""

# 생성될 폴더 경로
base_path = ""
# csv 파일 경로
csv_path = ""

# csv 파일을 열어서 처리
with open(csv_path, mode="r") as csv_file:
    # csv 파일을 읽어오는 csv.reader 객체 생성
    csv_reader = csv.reader(csv_file)
    # csv 파일의 첫 번째 row를 건너뛰기
    next(csv_reader)
    # csv 파일의 각 row를 처리하기 위한 loop
    for row in csv_reader:
        # csv 파일에서 값을 읽어들임
        a_value = row[0]
        # os.makedirs() 함수를 사용하여 폴더를 생성
        # os.path.join() 함수를 사용하여 base_path의 경로와 a_value의 값을 합침
        os.makedirs(os.path.join(base_path, a_value), exist_ok=True)
        # os.makedirs() 함수를 사용하여 하위 폴더인 "1", "2" 폴더를 생성
        os.makedirs(os.path.join(base_path, a_value, "1"), exist_ok=True)
        os.makedirs(os.path.join(base_path, a_value, "2"), exist_ok=True)