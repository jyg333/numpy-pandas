import pandas as pd
"""2차원 배열로 출력, Index깂을 넣어주면 특정 값 출력가능"""
array_1 = pd.Series(['apple','banana','meat'],index=['a','b','c'] )
print(array_1)
print(array_1['c'])
#Dictionary 를 Series로 변환이 가능하다.

fruit = {
    'a': 'apple',
    'b': 'banana',
    'c': 'carrot'
}
print(fruit )
array_2 = pd.Series(fruit)
print(array_2)

"""DataFrame 은 다수의 Series를 모아서 처리하는 목적으로 사용한다.
표형태로 출력한다. 데이터를 index기준으로 묶도록 한다."""
word_dic = {
    'apple':'사과',
    'banana':'바나나' ,
    'carrot':'당근'
}
importance_dic = {
    'apple': 3,
    'banana': 2,
    'carrot': 1
}
number_dic = {
    'apple': 5,
    'banana':6,
    'carrot': 8
}

word = pd.Series(word_dic)
number = pd.Series(number_dic)
importance = pd.Series(importance_dic)
sum = pd.DataFrame({
    'word':word,
    'number': number,
    'importance': importance
})
print(sum)

#새롭게 Series를 만들기
score = sum['number'] * sum['importance']
sum['score'] = score
print(sum)

sum.loc['Blueberry'] = ['블루베리',5,3, 15]
print(sum)

# 결과물 내보내기
sum.to_csv("sum.csv",encoding="utf-8-sig")
reload = pd.read_csv("sum.csv",index_col=0)
print(reload)

"""Pandas의 연산과 함수
완벽하지 않은 데이터 처리 : null, np.  nan"""
import numpy as np

word_dic = {
    'Apple':'사과',
    'Banana':'바나나' ,
    'Carrot':'당근',
    'Durian':'두리안'
}
importance_dic = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1,
    'Durian':1

}
number_dic = {
    'Apple':   5,
    'Banana':6,
    'Carrot': 8,
    'Durian': np.nan
}
word = pd.Series(word_dic)
importance = pd.Series(importance_dic)
number = pd.Series(number_dic)

sum = pd.DataFrame({
    'word': word,
    'number':number,
    'importance':importance
})
print(sum.isnull())

sum['number'] = sum['number'].fillna('Empty')
print(sum)

#자료형 연산, fill_value=0 옵션을 넣지 않으면 겹치지 않는 값에 대해서 Nan값을 반환한다.
array1 = pd.Series([1,2,3,],index=['A','B','C'])
array2 = pd.Series([3,4,5],index=['B','C','D'])
array_sum = array1.add(array2,fill_value=0)
print(array_sum)

#Sorting

sum = sum.sort_values('importance ',ascending=False)
print(sum)

