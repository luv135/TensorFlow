import numpy as np
import pandas as pd

array = np.array([[1, 2, 3],
                  [4, 5, 6]], dtype=np.float32)
print(array)
print(array.dtype)

a = np.ones((3, 4))
print(a)

arange = np.arange(12)
print(arange)

n = np.arange(12).reshape(3, 4)
print(n)

linspace = np.linspace(1, 10, 12)
print(linspace)

reshape = linspace.reshape(3, 4)
print(reshape)

a = np.array([10, 20, 30, 40])
b = np.arange(4)

print(a)
print(b)

print(a + b)
# 平方
print(b ** 2)
print(b)
print(b < 3)

a = np.array([[1, 1], [2, 2]])
b = np.arange(4).reshape(2, 2)
print(a)
print(b)

# 逐个相乘
print(a * b)
# 矩阵相乘
print(np.dot(a, b))
print(a.dot(b))

a = np.random.random((2, 4))
print(a)
# axis=0 表示列中的求和
print(a.sum(axis=0))
print(a.min())

a = np.arange(2, 14).reshape(3, 4)
a = np.random.random((3, 4))
print(a)
print(np.argmin(a))
print(np.argmax(a))
print(np.mean(a))
print(np.average(a))
print(np.median(a))
print(a)
# 累加
print(np.cumsum(a))
print(a)
# 差
print(np.diff(a))

print(np.nonzero(a))

print(np.sort(a))

a = np.arange(2, 14).reshape(3, 4)

print(a)
print(np.transpose(a))
print(a.T)
print(a.T.dot(a))

print(np.clip(a, 4, 9))

a = np.arange(3, 15).reshape(3, 4)
print(a)

print(a[2][1])
print(a[2, 1])
print(a[2])
print(a[2, :])
print(a[2, 1:3])
print('------------------')
for row in a:
    print(row)

print('----------')
for column in a.T:
    print(column)

print('---------')
# 转成1维
print(a.flatten())
print('---------')
for item in a.flat:
    print(item)

a = np.array([1, 1, 1, 1]).reshape(2, 2)
b = np.array([2, 2, 2, 2]).reshape(2, 2)
print(a)
print(b)
print('合并')
# 合并
vstack = np.vstack((a, b))  # 垂直合并
print(vstack)
print('hstack')
print(np.hstack((a, b)))  # 水平和平

print(a[np.newaxis, :])
print(a[:, np.newaxis])

print('------------')
# 矩阵分割
a = np.arange(12).reshape((3, 4))
print(a)
print(np.split(a, 2, axis=1))

print('-------------')
s = pd.Series([1, 2, 3, 4])
print(s)

dates = pd.date_range('2016-12-22', periods=6)
print(dates)

# df = pd.DataFrame(np.random.random((6, 5)), index=dates, columns=list('ABCDE'))
df = pd.DataFrame(np.arange(30).reshape((6, 5)), index=dates, columns=list('ABCDE'))
print(df.describe())
print(df.index)
print(df)
print(df.dtypes)
print('----------')
print(df)
print('----------')
print(df.head(n=2))


def ptl(s):
    print('----------')
    print(s)


def df_pt(s):
    ptl(df)
    ptl(s)


ptl(df.values)
ptl(df)
# 转置
ptl(df.T)
ptl(df)
ptl(df['A'])
df_pt(df[1:3])
df_pt(df['20161224':'20161226'])
df_pt(df.loc[dates[0]])

# 切片
df_pt(df.loc[:, ['A', 'C']])
df_pt(df.loc['20161224':'20161226', ['A', 'C']])
df_pt(df.loc['20161226', ['A', 'C']])

# 坐标对象
df_pt(df.loc[dates[0], 'B'])
df_pt(df.at[dates[0], 'B'])

# 选择行
df_pt(df.iloc[3])

df_pt(df.iloc[:, 1:3])
df_pt(df.iloc[2, 2])
df_pt(df.iat[2, 2])
df_pt(df.A > 5)
df_pt(df > 5)

df.iloc[0, 0] = np.nan
df.iloc[2, 3] = np.nan
df_pt(df)
# 丢弃 nan 行
print(df.dropna(axis=0))
