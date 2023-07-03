import pandas as pd

# 첫 번째 CSV 파일 경로
csv1 = '.csv'
# 두 번째 CSV 파일 경로
csv2 = '.csv'

# CSV 파일들을 Pandas DataFrame으로 읽어옵니다
df1 = pd.read_csv(csv1) # 첫 번째 CSV 파일 읽기
df2 = pd.read_csv(csv2) # 두 번째 CSV 파일 읽기

# ~ (tilde) 기호는 해당 논리식이 False인 모든 행을 리턴합니다
# 여기서는 df1에서 A열과 같은 값을 가진 행들을 제외한 나머지 행을 추출합니다
# 즉, 중복되지 않은 데이터를 추출합니다
output_data = df2[~df2['A'].isin(df1['A'])]

# 추출된 데이터를 새로운 CSV 파일로 저장합니다
# index=False로 설정하여, index 값은 CSV 파일에서 제외합니다
output_data.to_csv('output.csv', index=False)
