from PIL import Image
import os

folder_path = "C:\\Users\\DIS\\Desktop\\141\\53_A023_B0128_C001\\" # 이미지 파일이 저장된 폴더 경로

for filename in os.listdir(folder_path):
    # .jpeg 파일만 선택
    if filename.endswith('.JPEG'):
        img_path = os.path.join(folder_path, filename)
        # 이미지 파일 로드
        with Image.open(img_path) as im:
             # .jpg 형식으로 저장
             rgb_im = im.convert('RGB')
             # 이미지 파일 확장자 변경하여 저장
             new_filename = os.path.splitext(filename)[0] + ".jpg"
             new_file_path = os.path.join(folder_path, new_filename)