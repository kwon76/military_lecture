#수치형 자료 변환하기 - 표준화
#수치형 자료의 경우 다른 수치형 자료와 범위를 맞추기 위해 정규화 또는 표준화를 수행합니다.

#이번 실습에서는 titanic 데이터에서 수치형 자료인 Fare 데이터를 표준화해보겠습니다.

#표준화 공식
#X−μσ\frac{X-\mu}{\sigma}	
 
#지시사항
#standard 함수를 완성하고 Fare 데이터를 표준화하여 Fare에 저장합니다.


import pandas as pd
from elice_utils import EliceUtils
from numpy import *

elice_utils = EliceUtils()

"""
1. 표준화를 수행하는 함수를 구현합니다.
"""
def standard(data):
    
    data = (data - data.mean()) / data.std()
    
    return data
    
# 데이터를 읽어옵니다.
titanic = pd.read_csv('./data/titanic.csv')
print('변환 전: \n',titanic['Fare'].head())

# standard 함수를 사용하여 표준화합니다.
Fare = standard(titanic['Fare'])

# 변환한 Fare 데이터를 출력합니다.
print('\n변환 후: \n',Fare.head())
    
