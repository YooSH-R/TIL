import pandas as pd

"""
Python으로 엑셀 형태 데이터 다루기
"""

data = {
    'Name': ['Alex', 'Brad', 'Chad'],
    'Age': [25, 30, 35],
    'Score': [55.5, 90.3, 78.9],
}
df = pd.DataFrame(data)
print(df)


# Series: DataFrame의 열(Column)
name_series = df['Name']
print(name_series)
age_series = df['Age']
print(age_series)
print()
# 행(Row) 접근
print(df.loc[0])
print()
print(df.iloc[0])
print(df.iloc[0, 0], df.iloc[0, 2])

print(df[['Name', 'Score']])

"""
집계 기능
"""
ages = [25, 30, 35]
n = len(ages)
total = sum(ages)
print(total / n)

print(df['Age'].mean())
print(df['Score'].max())
print(df['Score'].sum())

print(df.sort_values(by='Score'))


"""
다양한 데이터를 활용하여 DataFrame 생성
"""
# 목표
data = {
    'Name': ['Alex', 'Brad', 'Chad'],
    'Age': [25, 30, 35],
    'Score': [85.5, 90.3, 78.9],
}
df = pd.DataFrame(data)


# Dictionary로 만들기
alex = {'Name': 'Alex', 'Age': 25, 'Score': 85.5}
brad = {'Name': 'Brad', 'Age': 30, 'Score': 90.3}
chad = {'Name': 'Chad', 'Age': 35, 'Score': 78.9}
df_from_dict = pd.DataFrame([alex, brad, chad])
print(df_from_dict)

# 각 행의 데이터를 담은 List로 만들기
alex = ['Alex', 25, 85.5]
brad = ['Brad', 30, 90.3]
chad = ['Chad', 35, 78.9]
data = [alex, brad, chad]
df_from_list = pd.DataFrame([alex, brad, chad], columns=['Name', 'Age', 'Score'])
print(df_from_list)

# np.ndarray로 만들기
import numpy as np
nums = np.array([
    [25, 85.5],
    [30, 90.3],
    [35, 78.9],
])
names = ['Alex', 'Brad', 'Chad']
df_from_ndarr = pd.DataFrame(nums, columns=['Age', 'Score'])
df_from_ndarr.insert(0, 'Name', names)
df_from_ndarr['Age'] = df_from_ndarr['Age'].astype(int)
print(df_from_ndarr)

