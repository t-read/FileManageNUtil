import os
import csv
from pathlib import Path
from tqdm import tqdm
import pandas as pd
'''
csv 파일을 이용하여 DataFrame을 생성하고, 특정 폴더에 있는 jpg 파일들의 이름을 DataFrame에 맞게 수정한 뒤 데이터프레임을 사용하여 파일을 필터링 후 출력.

주요 역할
pd.read_csv(): csv 파일을 읽어와 DataFrame으로 변환하는 함수입니다.
Path, glob() : 폴더 경로를 다루기 위해 사용하는 클래스 및 함수입니다.
to_csv(): DataFrame을 csv 파일로 저장하는 함수입니다.
apply(): 데이터프레임 데이터를 하나씩 반복하며 함수를 적용하여 새로운 데이터프레임을 생성하는 함수입니다.
isin(): DataFrame에서 특정 컬럼에서 매칭되는 데이터를 찾아내는 함수입니다.
주석 부분을 참고하시면 코드가 어떤 역할을 수행하는지 자세히 이해하실 수 있습니다.
'''
# csv1 경로에 있는 csv 파일을 pandas dataframe으로 저장
csv1 = "C:\\Users\\DIS\\Desktop\\temporary\\fit\\output_WEB.csv"
df = pd.read_csv(csv1)

# folder_path 경로의 모든 하위 폴더에서 jpg 파일들을 찾아서 리스트 형태로 jpg_path에 저장
folder_path = Path("C:\\Users\\DIS\\Desktop\\temporary\\preOp")
jpg_path = pd.DataFrame(list(folder_path.glob("**/*.jpg")))

# jpg_path의 파일 경로들을 csv 형식으로 저장
jpg_path.to_csv('C:\\Users\\DIS\\Desktop\\temporary\\preOp\\asd.csv','w',encoding='utf-8')

# csv2 경로에 있는 csv 파일을 pandas dataframe으로 저장
csv2 = "C:\\Users\\DIS\\Desktop\\temporary\\preOp\\asd.csv"
df2 = pd.read_csv(csv2)
# df2 데이터프레임의 첫번째 열에서 파일 이름만 추출하여 "name" 열에 저장
df2["name"] = df2[0].apply(lambda x: x.split("/")[-1])

# df2에서 "name" 열의 값이 df 데이터프레임의 "A" 열의 값과 일치하는 행만 추출하여 "df_isin"에 저장
df_isin = df2[df2["name"].isin(df["A"])]

# df_isin 출력
print(df_isin)