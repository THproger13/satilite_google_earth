import pandas as pd
import chardet

# 파일 인코딩 자동 감지
with open('C:\\DATA\\satilite_google_earth\\산림청 국립산림과학원_대형산불위험예보목록정보_20230607 (1).csv', 'rb') as f:
    result = chardet.detect(f.read())

# encoding = result['encoding']

encoding = 'euc-kr'  # 또는 'cp949' 또는 'euc-kr' 등 올바른 인코딩으로 지정


# 파일 열기

df = pd.read_csv('C:\\DATA\\satilite_google_earth\\산림청 국립산림과학원_대형산불위험예보목록정보_20230607 (1).csv', encoding=encoding, error_bad_lines=False)
# df.to_csv('C:\\DATA\\satilite_google_earth\\산림청 국립산림과학원_대형산불위험예보목록정보_20230607.csv', encoding='utf-8', index=False)

# # 시군구명이 '포항시 남구'인 정보 필터링
# daejeon_info = df[df['시군명'] == '포항시 남구']
# print(daejeon_info)

# 열 이름 출력
print(df.columns)

# 처음 몇 행의 데이터 출력
print(df.head())

