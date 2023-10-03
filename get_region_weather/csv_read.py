import pandas as pd
import chardet

# 파일 인코딩 자동 감지
# with 문법은 주로 파일, 네트워크 연결, 데이터베이스 연결과
# 같이 자원을 사용하는 동안 리소스를 
# 효율적으로 관리하기 위해 사용. 
# with 문법을 사용하면 코드 블록을 벗어나면 자원이 
# 자동으로 정리 및 해제되므로 메모리 누수와 같은 
# 문제를 방지할 수 있다. 

with open('C:\\DATA\\satilite_google_earth\\산림청 국립산림과학원_대형산불위험예보목록정보_20230607 (1).csv', 'rb') as f:
    result = chardet.detect(f.read())

encoding = 'euc-kr'  # 또는 'cp949' 또는 'euc-kr' 등 올바른 인코딩으로 지정

# 파일 열기

df = pd.read_csv('C:\\DATA\\satilite_google_earth\\산림청 국립산림과학원_대형산불위험예보목록정보_20230607 (1).csv', encoding=encoding)

# 열 이름 출력
print(df.columns)

# 시도명에 '대전'이라는 문자열이 포함된 정보 필터링
filtered_info = df[df['시도명'].str.contains('대전') ]
print(filtered_info)

# # 처음 몇 행의 데이터 출력
# print(df.head())

