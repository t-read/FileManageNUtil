from pathlib import Path
import shutil
import os

"""
기존의 이미지 파일들을 500장 단위로 나누어서 새로운 폴더에 이동시키는 코드입니다. 
먼저, createFolder(directory) 함수를 정의해놓습니다. 
이 함수는 입력받은 경로에 해당하는 폴더가 존재하지 않는 경우 폴더를 생성합니다. 
Path 를 이용하여 입력 폴더 경로를 지정하고, 입력 폴더 경로에서 이미지 파일만 추출하여 리스트 image_path 에 저장합니다. 
shutil.move 함수를 사용하여, 500장마다 새로운 경로에 폴더를 생성하고, 폴더에 해당하는 이미지 파일들을 이동시킵니다.
"""
 
# 새로운 폴더를 생성하는 함수
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

# 입출력 폴더 경로 지정
path = Path("")
image_path = list(path.glob("**/*.jpg"))
output_path = "C:\\Users\\DIS\\Desktop\\pj5\\5-020\\devide_file"

# 기존의 이미지 파일들을 n장 단위로 나눠서 새로운 폴더에 이동시킴
for i, row in enumerate(image_path):
    # n장마다 새로운 폴더 생성
    if i % 500 == 0:
        output_path = f"C:\\Users\\DIS\\Desktop\\pj5\\5-020\\devide_file\\{i}"
        createFolder(output_path)
    # shutil.move() 함수로 이미지 파일 이동시킴
    # str(row)를 사용하여 row 변수에 포함된 파일 경로를 문자열로 변환
    shutil.move(str(row), output_path)