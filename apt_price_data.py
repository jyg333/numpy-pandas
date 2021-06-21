"""전국 신규 아프트 분양 데이터"""

import pandas as pd
import numpy as np
#pd.set_option('display.width', 400)
df = pd.read_csv('house_price2020.csv')
df4 = df.copy()
df =df.rename(columns={'분양가격(㎡)':'분양가'})

#print(df.dtypes)
#df.to_csv('house_price_2020.csv') , 변경사항 저
#분양가가 object라서 float 으로 변경
df['분양가'] = pd.to_numeric(df['분양가'],errors = 'coerce')

#df['분양가'] = df['분양가'].convert_objects(convert_numeric=True) -> 이 코드로 변환했을 떄 에러 발생
print(df.dtypes)
print(df.head())
print(df.tail())

#Convert to numpy array
arr = df.to_numpy()
print(arr)
print(len(arr))
print(df.describe()) #간략한 통계정보를 나타냄
print(df.T.head()) # 축 변
print(df.sort_values(by='연도')[:5])
print(df.sort_values(by='지역명')[:5])
print(df.iloc[2,1]) #지정 인덱
print(df[df.분양가 > 6500][:5])

#reindexing 을 이용한 새로운 row 추가
df1 = df.reindex(index=df.index[:7], columns =list(df.columns) + ['extra'])
df1.loc[:4, 'extra'] = False

df2 = df1.copy()
df2 = df2.dropna(how='any') #Nan 값이 있는 행을 제
df2 = df2.shift(2)[:5] # shift row
print(df1)
print(df2)

test = np.arange(0,50)
test = test.reshape(10,5)
df3 = pd.DataFrame(test) #데이타 프레임으로 만들기
print(test)
print(df3)

"""Grouping"""
#print(df4.shape)
df4 =df4.rename(columns={'분양가격(㎡)':'분양가'})
df4['분양가'] = pd.to_numeric(df4['분양가'],errors = 'coerce')
df5 = df4.copy()
df4 = df4.groupby(['지역명','연도','월'])['분양가'].agg('sum')
print(df4)


grouped = df5.groupby(['지역명','연도','월']).sum()
print(grouped.unstack(0)) # 열을 도시별로
print(grouped.unstack(1)) #열을 연도 별로 출


"""Pivot Table, 자신이 원하는 데이터만 가지 행과 열을 재배치"""
df6 = pd.pivot_table(df5, values='분양가', index=['연도','지역명'], columns=['월'])
print(df6)

"""np.select(), 존건에 맞는 값 대입하기"""

conditions = [
    (df5['분양가'] < 2387),
    (df5['분양가'] >= 2387) & (df['분양가'] < 3130),
    (df5['분양가'] >= 3130) & (df['분양가'] < 3383),
    (df5['분양가'] >= 3383),
    (df5['분양가'] == np.nan)
]
choices = ['저렴', '보통', '비쌈', '매우 비쌈', '-']
df5['평가'] = np.select(conditions, choices, default=0)
print(df5.head(100))
df5 = df5.groupby(by='평가').count()
print(df5)