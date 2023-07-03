import os
from tqdm import tqdm
# 현재 디렉토리 경로
path = input("C:\\Users\\DIS\\Desktop\\temporary\\he\\A118")

# 디렉토리 내 파일 리스트
file_list = os.listdir(path)

# 대문자 jpg 확장자를 소문자 jpg로 변경
for file in tqdm(file_list, desc="확장자 명 변경 중"):
    if file.endswith(".JPG"):
        os.rename(os.path.join(path, file), os.path.join(path, file.lower()))