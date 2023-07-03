import pandas as pd

csv1 = 'C:\\Users\\DIS\\Desktop\\temporary\\fit\\5-3중복webNrefine.xlsx의 자동저장.csv'
csv2 = 'C:\\Users\\DIS\\Desktop\\temporary\\fit\\WEB_file_list.csv'

# 첫 번째 CSV 파일 읽기
df1 = pd.read_csv(csv1)

# 두 번째 CSV 파일 읽기
df2 = pd.read_csv(csv2)

# 중복 제거된 데이터 추출
output_data = df2[~df2['A'].isin(df1['A'])]

# 새로운 CSV 파일로 데이터 쓰기
output_data.to_csv('output_WEB.csv', index=False)