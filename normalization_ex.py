#수치형 자료 변환하기 - 정규화
#수치형 자료의 경우 다른 수치형 자료와 범위를 맞추기 위해 정규화 또는 표준화를 수행합니다.

#이번 실습에서는 titanic 데이터에서 수치형 자료인 Fare 데이터를 정규화해보겠습니다.

#정규화 공식
#X−XminXmax−Xmin\frac{X-X_{min}}{X_{max}-X_{min}}

#지시사항
#normal 함수를 완성하고 Fare 데이터를 정규화하여 Fare에 저장합니다.


import pandas as pd
from elice_utils import EliceUtils

elice_utils = EliceUtils()

"""
1. 정규화를 수행하는 함수를 구현합니다.
"""
def normal(data):
    
    #data = (data - min(data)) / (max(data) - min(data))
    data = (data - data.min()) / (data.max() - data.min())
    
    return data

# 데이터를 읽어옵니다.
titanic = pd.read_csv('./data/titanic.csv')
print('변환 전: \n',titanic['Fare'].head())

# normal 함수를 사용하여 정규화합니다.
Fare = normal(titanic['Fare'])

# 변환한 Fare 데이터를 출력합니다.
print('\n변환 후: \n',Fare.head())

