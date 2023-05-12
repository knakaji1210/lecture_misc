"""
Python　再帰関数についての基本
https://qlitre-weblog.com/recursive-function-python/
"""

# 例１：階乗計算（普通のやり方）
def factorial(n: int) -> int:  # ->はアノテーション
    product = 1
    while n > 0:
        product *= n
        n = n - 1
    return product

print(factorial(4))

# 例１：階乗計算（再帰関数）
def factorial2(n):
    if n == 0:
        return 1
    return n * factorial2(n - 1)

print(factorial2(4))

# メモによる再帰の高速化
def double_factorial(n):
    if n == 0:
        return 1
    return n * double_factorial(n - 1) + n * double_factorial(n - 1)

a = double_factorial(2)
print(a)

"""
# 1回目
2 * f(1) + 2 * f(1)
# 2回目
2 * 1 * ( f(0) + f(0) ) + 2 * 1 * ( f(0) + f(0) )
# 3回目
2 * 1 * (1 + 1) + 2 * 1 * ( 1 + 1 )
"""

# 高速化
def double_factorial2(n, _memo):
    # 答えが記録済みだったら、再計算はせず返す
    if n in _memo:
        print(n)
        print(_memo[n])
        return _memo[n]
    # 答えがない場合は再帰的に計算する
    if n == 0:
        ret = 1
    else:
        print("a")
        ret = n * double_factorial2(n - 1, _memo) + n * double_factorial2(n - 1, _memo)

    # 答えを記録する
    _memo[n] = ret
    print(ret)
    # 値を返す
    return ret

b = double_factorial2(2, [])
print(b)