import os
from PIL import Image
from tqdm import tqdm
'''
주어진 경로에서 이미지 파일을 찾아 크기를 조정한 후, 지정된 경로에 저장하는 코드입니다. 주요 역할은 다음과 같습니다.
os.path.join() : 경로를 연결합니다.
os.listdir(): 해당 경로의 파일 목록을 구합니다.
os.path.startswith(): 파일 이름의 문자열이 ()에서 지정한 문자열로 시작하는지를 검사합니다.
PIL.Image.open(): 이미지 파일을 Image 객체로 엽니다.
Image.resize(): 이미지의 크기를 조정합니다.
Image.save(): 이미지를 저장합니다.
'''
# 입력 이미지 폴더 경로
input_folder = ""
# 조정된 이미지 저장 폴더 경로
output_folder = ""
# 조정할 이미지 크기
output_size = (1920, 1080)

# 입력 폴더의 파일 이름들을 반복하며 이미지 resize를 수행
# tqdm을 사용하여 진행 상황을 출력
for filename in tqdm(os.listdir(input_folder)):
    # 숨김 파일은 건너뜁니다
    if not filename.startswith("."):
        # input 폴더와 output 폴더의 파일 경로를 만듭니다
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 실행할 때마다 이미지를 열고 이미지 객체를 생성합니다
        with Image.open(input_path) as image:
            # 조정된 크기의 이미지를 생성합니다
            resized_image = image.resize(output_size)
            # 조정된 이미지를 지정된 경로에 저장합니다
            resized_image.save(output_path)