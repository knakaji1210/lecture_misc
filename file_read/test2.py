import sys

args = sys.argv

def file_read(file_name):

    file_data = open(file_name, "r")
 
    # まず１行読み込む
    line = file_data.readline()
 
    # while文を使い、読み込んだ行の表示と次の行の取得を行う
    while line: # lineが取得できる限り繰り返す
        print(line)
        line = file_data.readline()
 
    # 開いたファイルを閉じる
    file_data.close()

if __name__ == '__main__':
    file_name = args[1]
    file_read(file_name)

