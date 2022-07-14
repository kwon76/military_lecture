#결측값 처리하기
#결측값이 있는 데이터는 일반적으로 머신러닝의 입력으로 사용할 수 없습니다. 그렇기에 데이터 전 처리 과정에서는 삭제 또는 대체 방식으로 결측값을 처리합니다.

#이번 실습에서는 titanic 데이터에서 과반수 이상의 데이터가 결측값으로 존재하는Cabin 변수를 삭제합니다. 이 후, 나머지 변수에 존재하는 결측값을 처리하기 위하여 결측값이 존재하는 샘플들을 제거합니다.

#pandas의 DataFrame에서 특정 변수(columns)를 삭제하기 위해서는 drop사용합니다.
#DataFrame.drop(columns=[변수명])
#DataFrame에서 결측값이 있는 샘플을 제거하기 위해서는 dropna를 사용합니다.
#DataFrame.dropna()

#지시사항
#drop 을 사용하여 Cabin 변수를 삭제하고 titanic_1에 저장합니다.

#titanic_1에서 dropna 를 사용하여 결측값이 존재하는 샘플을 삭제하고 titanic_2에 저장합니다.

import pandas as pd
from elice_utils import EliceUtils

elice_utils = EliceUtils()

    
# 데이터를 읽어옵니다.
titanic = pd.read_csv('./data/titanic.csv')
# 변수 별 데이터 수를 확인하여 결측 값이 어디에 많은지 확인합니다.
print(titanic.info(),'\n')

"""
1. Cabin 변수를 제거합니다.
"""
titanic_1 = titanic.drop(columns=['Cabin'])
# Cabin 변수를 제거 후 결측값이 어디에 남아 있는지 확인합니다.
print('Cabin 변수 제거')
print(titanic_1.info(),'\n')

"""
2. 결측값이 존재하는 샘플 제거합니다.
"""
titanic_2 = titanic_1.dropna()
# 결측값이 존재하는지 확인합니다.
print('결측값이 존재하는 샘플 제거')
print(titanic_2.info())
