import os
import json

# JSON 파일이 있는 폴더 경로
folder_path = 'C:\\Users\\DIS\\Desktop\\temporary\\mistake\\2023060210010718754118'

# 폴더 내 모든 파일에 대해 반복합니다.
for filename in os.listdir(folder_path):
    # 파일 이름이 '.json'으로 끝나는 경우에만 처리합니다.
    if filename.endswith('.json'):
        # 파일 전체 경로를 생성합니다.
        file_path = os.path.join(folder_path, filename)
        
        # 파일을 읽어서 파이썬 객체로 변환합니다.
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # annotations 리스트에서 bbox 값이 마이너스인 객체가 있는지 확인합니다.
        bbox_list = [annotation['bbox'] for annotation in data['annotations']]
        negative_bbox = False
        for bbox in bbox_list:
            if min(bbox) < 0:
                negative_bbox = True
                break
                
        # 마이너스 bbox 값을 가진 객체가 있으면, 해당 파일명을 출력합니다.
        if negative_bbox:
            print(filename)