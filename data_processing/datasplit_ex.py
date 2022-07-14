#데이터 분리하기
#머신러닝의 입력으로 사용하기 위해서는 데이터를 분리해야합니다. titanic 데이터에서 생존 여부인 Survived 을 예측하는 머신러닝을 수행한다고 했을 때 데이터를 분리해봅시다.

#이번 실습에서는 [실습6]에서 이상치 처리한 데이터를 바탕으로 feature 데이터와 label 데이터를 분리합니다. 이 후 학습용, 평가용 데이터로 분리합니다.

#학습용, 평가용 데이터 분리는 sklearn 라이브러리의 train_test_split을 사용하여 분리할 수 있습니다.
"""
X_train, X_test, y_train, y_test = train_test_split(feature 데이터, 
label 데이터, 
test_size= 0~1 값, 
random_state=랜덤시드값)
Copy
titanic 데이터 구성
image


지시사항
titanic_3 에서 Survived 변수를 제거하여 X에 저장하고 Survived 변수의 데이터는 pandas의 Series 형태로 y에 저장합니다.

train_test_split 를 사용하여 데이터를 분리합니다. test_size는 0.3, random_state는 42로 설정합니다.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from elice_utils import EliceUtils

elice_utils = EliceUtils()

# 데이터를 읽어옵니다.
titanic = pd.read_csv('./data/titanic.csv')

# Cabin 변수를 제거합니다.
titanic_1 = titanic.drop(columns=['Cabin'])

# 결측값이 존재하는 샘플 제거합니다.
titanic_2 = titanic_1.dropna()

# 이상치를 처리합니다.
titanic_3 = titanic_2[titanic_2['Age']-np.floor(titanic_2['Age']) == 0 ]
print('전체 샘플 데이터 개수: %d' %(len(titanic_3)))

"""
1. feature 데이터와 label 데이터를 분리합니다.
"""
X = titanic_3.drop(columns=['Survived'])
y = titanic_3['Survived']
print('X 데이터 개수: %d' %(len(X)))
print('y 데이터 개수: %d' %(len(y)))

"""
2. 학습용, 평가용 데이터로 분리합니다.
"""
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 분리한 데이터의 개수를 출력합니다.
print('학습용 데이터 개수: %d' %(len(X_train)))
print('평가용 데이터 개수: %d' %(len(X_test)))
