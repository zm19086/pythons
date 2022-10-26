# 関数
# 洗濯機関数
def washingMachine():
  print('給水します')
  print('洗います')
  print('すすぎます')
  print('脱水します')
  print('乾燥します')

washingMachine()

# 優しく洗う洗濯機関数
def softWash():
  print('給水します')
  print('優しく洗います')
  print('すすぎます')
  print('脱水します')
  print('乾燥します')

softWash()

# 引数を使って柔軟に処理する
def washingMachine(mode):
  print('給水します')
  if (mode == 'soft'):
    print('やさしく洗う')
  elif (mode == 'hard'):
    print('激しく洗う')
  else:
    print('普通に洗う')

washingMachine('soft')
washingMachine('hard')
washingMachine('normal')

# 引数に円の半径を渡すと面積を返す関数
def area(radius):
  result = radius * radius * 3.14
  return result

print(area(5))

small = area(5)
big = area(10)
print(small)
print(big)



# 組み込み型の関数(定義せずとも元からある関数)
# 文字数、データの数を数える関数 len()
print(len('thunderbolt'))

animal = ['cat', 'dog', 'duck', 'lion']
print(len(animal))

# 引数で渡したデータの中から最も大きいものを返す max()
list = [100, 30, 45, 999, 12, 76]
print(max(list))
# 引数で渡したデータの中から最も小さいものを返す min()
print(min(list))

# 昇順は　数字 -> 大文字　-> 小文字
print(max('thunderbolt'))
print(max('1Aa'))
print(min('1Aa'))

# 63行目と同じ順序でデータを並べ替えてリスト型で返す関数 sorted()
print(sorted('thunderbolt'))
print(sorted('1Aa'))
print(sorted([100, 95, 55, 78, 80, 78]))

# 表示のための関数 print()
print(123 + 456)
print('Hello World')

# データの型を返す関数 type()
hatena_1 = 9800
print(type(hatena_1))
hatena_2 = 'marshmallow'
print(type(hatena_2))
hatena_3 = ['osomatsu', 'karamatsu']
print(type(hatena_3))

# データ型の種類に応じたメソッドの一覧を返す関数 dir()
string = 'nikuman'
print(dir(string))
# 引数を渡さなければ、そのファイル内の変数、関数も返してくれる
print(dir())