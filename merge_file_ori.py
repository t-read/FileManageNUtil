# 필요한 라이브러리를 불러옵니다.
import os
import shutil
import time

# 디렉토리 내 모든 파일 리스트를 반환하는 함수를 정의합니다.
def read_all_file(path):
    output = os.listdir(path) # 해당 디렉토리 내 모든 파일 리스트를 불러옵니다.
    file_list = []

    for i in output:
        if os.path.isdir(path+"/"+i): # 파일이 디렉토리인 경우, 재귀적으로 처리합니다.
            file_list.extend(read_all_file(path+"/"+i))
        elif os.path.isfile(path+"/"+i): # 파일이 일반 파일인 경우, 리스트에 추가합니다.
            file_list.append(path+"/"+i)

    return file_list

# 파일 리스트를 이동시키는 함수를 정의합니다.
def move_all_file(file_list, new_path):
    for src_path in file_list: # 파일 리스트 내 모든 항목에 대해 반복합니다.
        file = src_path.split("/")[-1] # 파일 이름만 추출합니다.
        shutil.move(src_path, new_path+"/"+file) # shutil.move() 함수를 사용하여 파일을 이동합니다.
        
# 작업 시간을 계산하기 위해 현재 시간을 저장합니다.
start_time = time.time()

src_path = "" # 기존 폴더 경로
new_path = "" # 옮길 폴더 경로

file_list = read_all_file(src_path) # 디렉토리 내 모든 파일 리스트를 불러옵니다.
move_all_file(file_list, new_path) # 파일 리스트를 이동시킵니다.

# 작업이 완료된 후 경과 시간을 계산하여 출력합니다.
print("=" * 40)
print("러닝 타임 : {}".format(time.time() - start_time))
