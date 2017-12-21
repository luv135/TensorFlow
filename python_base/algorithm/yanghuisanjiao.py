# 杨辉三角

def yanghui(line):
    value = [1]
    for n in range(line):
        print(value)
        value = [1] + [value[i] + value[i + 1] for i in range(0, len(value) - 1)] + [1]


yanghui(10)
