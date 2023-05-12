"""
https://utokyo-ipp.github.io/appendix/3-recursion.html

def recursive_function(...):
    if 問題粒度の判定:
        再帰呼び出しを含まない基本処理
    else:
        再帰呼び出しを含む処理（問題の分割や部分解の合成を行う）

"""

# 再帰関数の例１：接頭辞リストと接尾辞リスト
# 入力の文字列の接頭辞リストを返す関数prefixes
def prefixes(s):
    if s == '':
        return []
    else:
        return [s] + prefixes(s[:-1])

# 入力の文字列の接尾辞リストを返す関数suffixes
def suffixes(s):
    if s == '':
        return []
    else:
        return [s] + suffixes(s[1:])

s = 'aabcc'

print(prefixes(s))
print(suffixes(s))

# 再帰関数の例２：べき乗の計算
# 入力の底baseと冪指数exptからべき乗を計算する関数power
def power(base, expt):
    if expt == 0:
        # exptが0ならば1を返す
        return 1
    else:
        # exptを1つずつ減らしながらpowerに渡し、再帰的にべき乗を計算
        # (2*(2*(2*....*1)))
        return base * power(base, expt - 1)

print(power(2,10))

# 再帰関数の例３：マージソート・・・まだよくわかっていない
# マージソートを行い、比較回数 n を返す
def merge_sort_rec(data, l, r, work):
    n = 0
    if r - l <= 1:
        return n
    m = l + (r - l) // 2
    n1 = merge_sort_rec(data, l, m, work)
    n2 = merge_sort_rec(data, m, r, work)
    i1 = l
    i2 = m
    for i in range(l, r):
        from1 = False
        if i2 >= r:
            from1 = True
        elif i1 < m:
            n = n + 1
            if data[i1] <= data[i2]:
                from1 = True
        if from1:
            work[i] = data[i1]
            i1 = i1 + 1
        else:
            work[i] = data[i2]
            i2 = i2 + 1
    for i in range(l, r):
        data[i] = work[i]
    return n1 + n2 + n

def merge_sort(data):
    return merge_sort_rec(data, 0, len(data), [0]*len(data))

import random
a = [random.randint(1,10000) for i in range(100)]
print(a)
print(merge_sort(a))