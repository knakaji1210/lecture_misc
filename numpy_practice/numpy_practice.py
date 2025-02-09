# example codes for numpy
# https://qiita.com/moe_713/items/671c8c912f6e8d6c7442

import numpy as np

def main():
    # 1. 配列をつくる
    # 01. np.array
    # 配列を作る
    a = np.array([1, 2, 3])
    print('a = ', a)

    af = np.array([1, 2, 3], dtype=float)
    print('af = ', af)

    # 02. np.zeros
    # 要素がゼロの配列を作る
    zero = np.zeros(3, dtype=float)
    print('zero = ', zero)

    # 03. np.zeros_like
    # aと同じ形式の、要素がゼロの行列を作る
    zerolike_a = np.zeros_like(a)
    zerolike_af = np.zeros_like(af)
    print('zerolike_a = ', zerolike_a) 
    print('zerolike_af = ', zerolike_af)

    # 04. np.ones
    # 要素が1の配列を作る
    one = np.ones(3)
    print('one = ', one)

    # 05. np.eye
    # 単位行列を作る
    eye = np.eye(2)
    print('eye = ', eye)

    # 06. np.arange
    # 規則的な配列を作る
    a_range = np.arange(0,2, 0.5) # 始点、終点(アウトプットはこの値を含まない）、間隔を記載
    print('a_range = ', a_range)

    # 07. np.linspace
    # 規則的な配列を作る
    lin_space = np.linspace(1, 10, 10) # 始点、終点(アウトプットはこの値を含む)、個数を記載
    print('lin_space = ', lin_space)

    # 2. 様々な乱数の配列をつくる

    # 08. np.random.rand
    # 0.0以上、1.0未満の一様分布の乱数を生成
    random = np.random.rand(2) # 0〜1の乱数を2つ作成
    print('random = ', random)
    random_array = np.random.rand(2, 2) # 0〜1の乱数で2x2の行列を生成
    print('random_array = ', random_array)

    # 09. np.random.randint
    # 範囲での任意の整数の乱数を生成
    rand_int = np.random.randint(1, 7)
    print('rand_int = ', rand_int)

    # 10. np.random.randn
    # 平均0、分散1の標準正規分布に従う値を生成
    randn = np.random.randn() # 値を一つ作成
    print('randn = ', randn)
    randn_array1 = np.random.randn(2, 2) # 値を2×2行列で作成
    print('randn_array1 = ', randn_array1)
    # 追加
    randn_array2 = np.random.randn(2) # 値を配列で作成
    print('randn_array2 = ', randn_array2)
    randn_array3 = np.random.randn(1,2) # 値を2×1行列で作成、上の配列との違いに注意
    print('randn_array3 = ', randn_array3)

    # 11. np.random.normal
    # 正規分布の任意の平均・標準偏差を指定できる
    random_n = np.random.normal(5, 1) # 平均5、標準偏差1の正規分布
    print('random_n = ', random_n)

    # 12. np.random.choice()
    # ランダムに要素を抽出
    random_choice = np.random.choice(lin_space)
    print(random_choice)

    # 3. 配列の参照をする

    # 13. ndarray.ndim
    # 行列の次元数を参照
    a = np.array([[1, 2 ,3],[4, 5, 6]])
    print(a)
    print('a_dim = ', a.ndim)

    # 14. ndarray.size
    # 行列の要素数を参照
    print('a_size = ', a.size)

    # 15. ndarray.shape
    # 行・列数を参照
    print('a_shape = ', a.shape)

    # 16. ndarray.dtype
    # 要素の型を参照
    print('a_type = ', a.dtype)

    # 17. [p, q]
    # 配列のp行q列目の要素の参照・・・もう少しちゃんと説明が必要
    a = np.array([1, 2, 3])
    print('a = ', a)
    print('a[1] = ', a[1])      # 先頭を0番目とした際の1番目の値を参照
    print('a[0:2] = ', a[0:2])  # スライス、0番目から、２番目の「一つ手前」までを参照
    b = np.array([[1, 2 ,3],[4, 5, 6]])
    print('b = ', b)
    print('b[0,1] = ', b[0,1])  # 0行1列目を参照
    print('b[0,:] = ', b[0,:])  # 0行目を参照
    print('b[:,1] = ', b[:,1])  # 1列目を参照
    print('b[:,[1,2]] = ', b[:,[1,2]])  # 1,2列目を参照

    # 4. 配列を操作する
    # この部分については以下も参照
    # https://it-mayura.com/python/pn003/
    
    # 18. ndarray.reshape(p, q)
    # p行q列の配列に変換
    b = np.array([[1, 2 ,3],[4, 5, 6]])
    print('b = ', b)
    c = b.reshape(3, 2)
    print('c = ', c)
    # この部分については以下も参照
    # https://it-mayura.com/python/pn003/
    # reshape関数は元になる配列情報を参照して配列を変形。
    # どちらかの配列内の要素値が変わると互いに影響しあう
    # b = np.array([[2, 4 ,6],[8, 10, 12]]) # このようにbを変化させてもcには影響しない
    b[:1] = 9                               # このようにbを変化させると   
    print('b = ', b) 
    print('c = ', c)                        # cも影響を受ける
    b = np.array([[1, 2 ,3],[4, 5, 6]])     # bを元に戻した
    print('b = ', b)
    d = np.reshape(b,(3, 2))                # reshapeの別の書き方
    print('d = ', d)
    b[1:2] = 7                              # bを変化させた
    print('b = ', b)
    print('d = ', d)

    # 19. ndarray.resize(p, q)
    # p行q列の配列に変換し、変更された配列がもとの配列より大きければ、必要なだけ0で埋める
    a = np.array([[1, 2 ,3],[4, 5, 6]])
    print('a = ', a)
    a.resize(3, 3)
    print('a = ', a)
    b = np.array([[1, 2 ,3],[4, 5, 6]])
    b_res = b.resize(3,3)
    print(b_res)            # こうするとNoneが返ってきてしまう
    b_res = np.resize(b,(3,3))
    print(b_res)            # こっちなら思っている結果が返ってくる
    # この部分については以下も参照
    # https://it-mayura.com/python/pn003/
    # resize関数は元の配列を変形して新しい配列を作成
    # reshapeは元配列と変形後の配列の要素数が同じである必要があるが,
    # resizeは変形後の要素が異なっていても配列を強制的に作成
    a = np.arange(1, 10) 
    print('a = ', a)
    b = np.resize(a,(3,3))
    print('b = ', b)
    a[0:9] = 99         # 元の配列の値を変更
    print('a = ', a)    # aは変わった
    print('b = ', b)    # bは変わらない

    # 20. ndarray.ravel
    # 多次元配列を1次元の行列にする
    a = np.array([[1, 2 ,3],[4, 5, 6]])    
    print('a = ', a)
    b = a.ravel()
    print('b = ', b)
    a[0:9] = 99         # 元の配列の値を変更
    print('a = ', a)    # aが変わると
    print('b = ', b)    # bも変わる  

    # 21. np.flip
    # 配列の要素を反対にする
    a = np.array([[1, 2 ,3],[4, 5, 6]])
    print('a = ', a)
    b = np.flip(a)
    print('b = ', b)

    # 22. ndarray.transpose
    # 配列を転置する
    a = np.array([[1, 2 ,3],[4, 5, 6]])
    print('a = ', a)
    b = a.transpose()
    print('b = ', b)

    # 23. np.append
    # 配列に要素を追加
    a = np.array([1, 2, 3])
    print('a = ', a)
    b = np.append(a, 4) # 末尾に4を追加
    print('b = ', b)
    c = np.append(0, a) # 先頭に０を追加
    print('c = ', c)
#    d = a.append(4)     # この書き方はNG
#    print('d = ', d)
    np.append(a, 5)     # これは通るけど、aには5は入ってない
    print('a = ', a)
    a = np.append(a, 6) # これならaのままでaに6が入る
    print('a = ', a)

    # 24. np.where
    # 条件を満たす要素を返す、あるいはTrue・Falseを判定する
    a = np.arange(6).reshape((2, 3))
    print('a = ', a)
    w1 = np.where(a < 3, True, False)   # a<3の場合True、そうでない場合Falseを返す
    print('w1 = ', w1)
    w2 = np.where(a < 3)                # a<3を満たす要素の範囲を抽出
    print('w2 = ', w2)
    # 以下使えそうなnp.whereの使い方
    # https://note.nkmk.me/python-numpy-where/
    b = np.arange(9).reshape(3, 3)
    print('b = ', b)
    c = np.where((b > 2) & (b < 6), -1, 100)
    print('c = ', c)
    d = np.where((b > 2) & (b < 6) | (b == 7), -1, 100) # |はor
    print('d = ', d)
    e = np.where(b < 4, b, 100)
    print('e = ', e)

    # 25. np.all
    # 配列の要素が全て条件を満たすか否かを判定する
    a = np.arange(6).reshape((2, 3))
    print(np.all(a < 3))
    print(np.all(a < 6))

    # 26. np.any
    # 配列の要素のいずれかが条件を満たすか否かを判定する
    print(np.any(a < 3))
    print(np.any(a > 6))

    # 27. ndarray.argmax
    # 多次元配列の中の最大値の要素を持つインデックスを返す
    print(a.argmax())

    # 28. np.sort
    # 配列を小さい順に並べ替える
    a = np.array([8, 2, 1, 5, 6])
    print('a = ', a)
    b = np.sort(a)
    print('b = ', b)

    # 29. np.argsort
    # 配列を小さい順に並べ替えた際の配列のインデックスを出力
    c = np.argsort(a)
    print('c = ', c)

    # 30. np.expand_dims
    # 配列に次元を追加
    a = np.arange(6).reshape(2, 3)
    print('a = ', a)
    b = np.expand_dims(a, 0)
    print('b = ', b)
    # よくわからないが、np.expand_dimsは非推奨だそうで、np.newaxisかreshapeを使うべきだということ
    # https://www.internetacademy.co.jp/itlab/column-technology/python_stydy08.html

    # 31. np.broadcast_to
    # ブロードキャストと呼ばれる、異なる形状の配列を自動統一を実施
    # 特にbroadcast_toは配列を任意の形状にブロードキャストする際に使用する
    a = np.arange(2)
    print('a = ', a)
    b = np.broadcast_to(a,(2, 2))
    print('b = ', b)

    # 32. np.broadcast_arrays
    # 複数の配列をブロードキャストして形状を揃えたい際に使用する
    a = np.arange(3)
    print('a = ', a)
    b = np.arange(3).reshape(3, 1)
    print('b = ', b)
    c = np.broadcast_arrays(a, b)   # ちょっと意味がわからない
    print('c = ', c)

    # 5. 配列の演算
    # 33. 一般的な四則演算
    a = np.array([1, 2, 3])
    print('a = ', a)
    b = np.array([4, 5, 6])
    print('b = ', b)
    c = a + b
    print('a + b = ', c)
    d = a - b
    print('a - b = ', d)
    e = a * b
    print('a * b = ', e)
    f = a / b
    print('a / b = ', f)
    g = a **2
    print('a^2 = ', g)

    # 34. np.add(a, b)
    # a, bの足し算
    print('a = ', a)
    print('b = ', b)
    c = np.add(a,b)
    print('a + b = ', c)

    # 35. np.subtract(a, b)
    # a, bの引き算
    c = np.subtract(a, b)
    print('a - b = ', c)

    # 36. np.sum
    # 配列の要素の合計値
    a = np.array([[1, 2, 3],[4,5,6]])
    print('a = ', a)
    print('np_sum = ', np.sum(a))
    b = np.sum(a, axis=0)   #列ごとの合計値
    print('b = ', b)
    c = np.sum(a, axis=1)   #行ごとの合計値
    print('c = ', c)

    # 37. np.multiply(a, b)
    # a, bの要素ごとの積（アダマール積）
    a = np.array([1, 2, 3])
    print('a = ', a)
    b = np.array([4, 5, 6])
    print('b = ', b)
    c = np.multiply(a,b)
    print('a * b = ', c)

    # 38. np.dot(a, b)
    # a, bの配列同士の積
    a = np.arange(3).reshape(1, 3)
    print('a = ', a)
    b = np.arange(3).reshape(3, 1)
    print('b = ', b)
    c = np.dot(a,b)
    print('ab = ', c)
    d = np.dot(b,a)
    print('ba = ', d)
    # 引数が両方とも一次元配列の場合は内積を返す
    a = np.array([1, 2, 3])
    print('a = ', a)
    b = np.array([4, 5, 6])
    print('b = ', b)
    e = np.dot(a,b)
    print('a.b = ', e)

    # 39. np.mean
    # 平均の算出
    a = np.arange(10).reshape(2, 5)
    print('a = ', a)
    print(np.mean(a))

    # 40. np.std
    # 標準偏差の算出
    print(np.std(a))

    # 41. np.power
    # 累乗の計算
    print(np.power(2,3))     #2の３乗
    a = np.array([1, 2, 3])
    print('a = ', a)
    b = np.power(a, 2)
    print('a^2 = ', b)

    # 42. np.sqrt
    # 平方根の計算
    print(np.sqrt(4))
    c = np.sqrt(a)
    print('sqrt_a = ', c)

    # 43. np.max
    # 最大値を返す
    print(np.max(a))

    # 44. np.min
    # 最小値を返す
    print(np.min(a))

    # 45. np.abs
    # 絶対値を求める
    print(np.abs(-1))
    a = np.array([-1, 2, -3])
    print('a = ', a)
    b = np.abs(a)
    print('abs_a = ', b)

    # 46. np.exp(x)
    # eのx乗
    print(np.exp(1))

    # 47. np.log(x)
    # eを底とするxの対数
    print(np.log(np.exp(1)))

    # 48. np.sin
    # sinを求める
    print(np.sin(np.pi/2))

    # 49. np.cos
    # cosを求める
    print(np.cos(np.pi))

    # 50. np.tan
    # tanを求める
    print(np.tan(np.pi/4))



if __name__ == '__main__':
    main()