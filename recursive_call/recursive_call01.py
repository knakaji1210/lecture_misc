"""
Pythonで理解する再帰関数
https://qiita.com/dhirabayashi/items/2f079e62fa2e286f1766
"""

# 例１：nまでの和
def total(n):
# 再帰関数には再帰呼び出しを止めるための終了条件が必要不可欠
    if n < 1:
        return 0
# あたかも関数が実装済みであるかのように考える
    return n + total(n - 1)

print(total(10))

# 例２：リストの各要素の２倍

# 普通のやり方
list = [1, 2, 3]
double_list_for = [ x*2 for x in list]
print(double_list_for)

def double_list(list):
    if list == []:
        return []

    first = list[0]
    rest = list[1:]
    return [first * 2] + double_list(rest)

print(double_list(list))