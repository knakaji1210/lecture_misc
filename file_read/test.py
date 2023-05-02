file_data = open("sample_file.txt", "r")
 
# まず１行読み込む
line = file_data.readline()
 
# while文を使い、読み込んだ行の表示と次の行の取得を行う
while line: # lineが取得できる限り繰り返す
    print(line)
    line = file_data.readline()
 
# 開いたファイルを閉じる
file_data.close()