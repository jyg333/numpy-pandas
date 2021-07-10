"""Masking 연산"""
import pandas as pd
import numpy as np

# 각 원소단위로 처리하기
df = pd.DataFrame(np.random.randint(1, 10,(2,2)),index=[0,1],columns=["A","B"])
print(df)
print(df["A"]>= 5)
# Query 형태로 추출, 조건을 만족할때 출
print(df.query("A > 2 and B <= 8"))

# 세부적인 연산
df02 = pd.DataFrame([[1,2,3,4,],[1,2,3,4,]],index=[0,1],columns=["A","B","C","D"])
print(df02)
df03 = df02

df02 = df02.apply(lambda x : x*x)
print(df02)

def square(x):
    return x*x
print(square(df03))
#같은 결과 출력되는 것을 확인 할 수 있다.

#특정 데이터 프레임의 데이터 변경하기
df04 = pd.DataFrame([["Apple","Banana","Carrot","Durian"],
                     ["Banana","Carrot","Apple","Banana"]],
                    index=[0,1],
                    columns=["A","B","C","D"]
                    )
print(df04)
df04 = df04.replace({"Apple": "FineAplle"})
print(df04)

#DataFrame Group By
df05 = pd.DataFrame([
    ["Apple",7,"fruit"],
    ["Banana",3,"fruit"],
    ["Rice",7,"Meal"],
    ["Meat",9,"Meal"]],
     columns=["Names","Frequency","Type"]
)
print(df05)
df05 = df05.groupby(["Type"]).sum()
print(df05)

df06 = pd.DataFrame([
    ["Apple",4,3,"fruit"],
    ["Banana",3,6,"fruit"],
    ["Rice",7,3,"Meal"],
    ["Meat",9,10,"Meal"]],
     columns=["Names","Frequency","Importance","Type"]
)
print(df06.groupby(["Type"]).aggregate([min,max, np.average])) #정수형 컬럼에 대해서 각각의 연산 수행

def mean_filter(data):
    return data["Frequency"].mean() >= 5

# Frequency의 평균이 5보다 큰 값을 가진 "Type"만 출력
print(df06.groupby("Type").filter(mean_filter))

df06["Gap"] = df06.groupby("Type")["Frequency"].apply(lambda x : x - x.mean())
print(df06)

#DataFrame의 다중화
df07 = pd.DataFrame(np.random.randint(1,20,(4,4)),
                    index=[["1차","1차","2차","2차"],["공격","공격","수비","수비"]],
                    columns=["1회","2회","3회","4회"]
                    )
print(df07)
print(df07[["1회","2회"]].loc["2차"])

