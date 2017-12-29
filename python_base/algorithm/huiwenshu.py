# 回文数
def huiwen(number):
    for i in range(number + 1):
        a = str(i)
        if a[::-1] == a:
            print(a)


# huiwen(10000)

def huiwen2(number):
    return str(number) == str(number)[::-1]


print(list(filter(huiwen2, list(range(10000)))))
