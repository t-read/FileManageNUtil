from PIL import Image
import os

# 이미지 파일이 저장된 폴더 경로
folder_path = ""

# 폴더 내 모든 파일에 대해 반복합니다
for filename in os.listdir(folder_path):
    # .jpeg 확장자를 가진 파일에 대해서만 처리합니다.
    if filename.endswith('.JPEG'):
        # 이미지 파일 경로 생성
        img_path = os.path.join(folder_path, filename)
        
        # 이미지 파일 로드
        with Image.open(img_path) as im:
             # RGB 형식으로 변환
             rgb_im = im.convert('RGB')
             
             # .jpg 확장자를 가진 파일로 변환하여 저장
             new_filename = os.path.splitext(filename)[0] + ".jpg"
             new_file_path = os.path.join(folder_path, new_filename)
             
             # 변환된 파일 저장
             rgb_im.save(new_file_path)