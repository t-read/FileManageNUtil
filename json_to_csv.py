import pandas as pd
import glob
import shutil
from tqdm import tqdm
import json

# json 파일을 Pandas DataFrame으로 불러옵니다.
data = pd.read_json("./sd.json")

# Pandas DataFrame의 컬럼 이름을 변경합니다.
data.rename(columns={0:'path'}, inplace=True)

# 이미지 파일 이름만 추출하여 컬럼을 추가합니다.
data["name"] = data["path"].apply(lambda x: x.split("/")[-1])
data["name"] = data["name"].apply(lambda x: x.split(".")[0])
data.to_csv("./asd.csv")
    

"""
csv_data = pd.read_csv("53_add.csv")
#csv_data["path"] = csv_data["name"].apply(lambda x:str(x) + ".jpg")
print(csv_data)

for i, row in csv_data.iterrows():
    shutil.move(row["path"], "/media/smartcoop/5-1/5-3_s3/53_11400_image")
"""
