# ファイル作成&ファイル書き込み
file_object = open('python.txt', 'w')
print(file_object.write('this is sample of python.'))
file_object.close()
# file_object.write('this is sample of python')

# 書き込みのタイミングに実行するflushメソッド
file_object = open('python_flush_test.txt', 'w')
print(file_object.write('Use flush!!'))
file_object.flush()

# ファイル読み込み
file_object = open('python.txt', 'r')
print(file_object.read())

# 場所指定
file_object = open('/Users/koya/Desktop/vs.code/practices/python 共同開発/pythons/sample_folder/file/python_flush_test.txt', 'w')
file_object.write('Use flush!!')
file_object = open('/Users/koya/Desktop/vs.code/practices/python 共同開発/pythons/sample_folder/file/python_flush_test.txt', 'r')
print(file_object.read())

# 追記
file_object = open('/Users/koya/Desktop/vs.code/practices/python 共同開発/pythons/sample_folder/file/python_flush_test.txt', 'a')
file_object.write('\nAdd data from program!!')
file_object = open('/Users/koya/Desktop/vs.code/practices/python 共同開発/pythons/sample_folder/file/python_flush_test.txt', 'r')
print(file_object.read())
file_object.close()

# 読み込み＆書き込みモード
file_object = open('/Users/koya/Desktop/vs.code/practices/python 共同開発/pythons/sample_folder/file/python_flush_test.txt', 'r+')
print(file_object.read())
print(file_object.write('Use r+ mode.'))
file_object.close()

# 読み込み開始位置を最初に戻すseekメソッド
file_object = open('/Users/koya/Desktop/vs.code/practices/python 共同開発/pythons/sample_folder/file/python_flush_test.txt', 'r+')
print(file_object.read())
print(file_object.read())
file_object.write('Happy Hacking')
file_object.seek(0)
print(file_object.read())
file_object.close()

# withを使ってcloseメソッドを使わずにファイルオブジェクトをcloseする
with open('/Users/koya/Desktop/vs.code/practices/python 共同開発/pythons/sample_folder/file/python_flush_test.txt', 'w') as file_object:
  file_object.write('Using with!')

