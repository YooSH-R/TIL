import pandas as pd

"""
Python으로 엑셀 형태 데이터 다루기
"""

data = {
    'Name': ['Alex', 'Brad', 'Chad'],
    'Age': [25, 30, 35],
    'Score': [55.5, 90.3, 78.9]
}
df = pd.DataFrame(data)
print(df)

# Series: DataFrame의 열(Column)
name_series = df['Name']
print(name_series)
age_series = df['Age']
print(age_series)
print()
# 행(Row)
print(df.loc[0])
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