# 按成绩排名
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_score(args):
    return args[1]


print(sorted(L, key=by_score, reverse=True))
