import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 讀入training data
arr = np.loadtxt("training.txt", delimiter=",")
df = pd.DataFrame(arr, columns=['x1', 'x2', 'class'])

# 讀入預測data
arrtest = np.loadtxt("test.txt", delimiter=",")
dftest = pd.DataFrame(arrtest, columns=['x1', 'x2'])

# 建立圖表
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.xlabel('x1')
plt.ylabel('x2')
plt.grid(True)

# 區分class欄位中1與-1之data
filter1 = (df['class'] == 1)
filter0 = (df['class'] == -1)
df1 = df[filter1]
df0 = df[filter0]

# 畫點 1是黑點 -1是紅x
ax.scatter(df1['x1'], df1['x2'], label='+1(Training)', color='black', marker='o')
ax.scatter(df0['x1'], df0['x2'], label='-1(Training)', color='red', marker='x')

# 找到最小及最大的x1值 用來畫線
minx = df.min().at['x1']
maxx = df.max().at['x1']

# w vector 與 b 建立
w = [random.random(), random.random()]
b = random.random()

# crt確認所有data是否training成功 及epoch是否超過上限
crt = False
epoch = 0
while not crt:
    epoch += 1
    if epoch == 30:
        break
    # tp用來確認單一data是否通過
    tp = True
    for t in range(len(df)):
        # 若不符合則
        if np.sign(np.dot(w, df.loc[t, ['x1', 'x2']]) + b) != df.at[t, 'class']:
            w = w + (df.at[t, 'class'] * df.loc[t, ['x1', 'x2']])
            b = b + df.at[t, 'class']
            tp = False
    # 若tp失敗則false
    crt = crt or tp

# test資料預測
tdata = 1
x1 = []
x0 = []
y1 = []
y0 = []
for t in range(len(dftest)):
    x = dftest.at[t, 'x1']
    # y為線上預估值
    y = (-b - w[0] * x) / w[1]

    print("test data", tdata, ":")
    print("x1=", x, ", x2=", dftest.at[t, 'x2'])
    if dftest.at[t, 'x2'] > y:
        x0.append(x)
        y0.append(dftest.at[t, 'x2'])
        print("預測結果: -1")
    else:
        x1.append(x)
        y1.append(dftest.at[t, 'x2'])
        print("預測結果: +1")
    tdata += 1
    print()

plt.scatter(x0, y0, label='-1(Testing)', marker='^', color='red')
plt.scatter(x1, y1, label='+1(Testing)', marker='^', color='black')

print()
print("w1: ", w[0])
print("w2: ", w[1])
print("b: ", b)

# 畫線
x = np.linspace(minx, maxx, 100)
y = (-b - w[0] * x) / w[1]
plt.plot(x, y)

plt.legend(loc='lower right')
plt.show()
