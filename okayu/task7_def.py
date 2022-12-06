# 関数を使いこなそう

# 引数に二つの数字渡し、それらを足した結果を返す関数

def calc(a, b):
  print(a + b)
  return

calc(3, 4)

# 文字列の中の特定の文字の数を返す関数
# 関数charaCountを定義する
# 文字列は「josai univercity」
# 数える文字は「i」

string = 'josai univercity'
def charaCount(str, chara):
  count = 0
  for chr in str:
    if (chr == chara):
      count += 1
  print(count)

charaCount(string, 'i')

# 大文字と小文字が混ざったリストaの中身を小文字に統一してリストbに格納する関数
# 第一引数に変換前のリスト、第二引数に変換後のリストを定義する
a = ['a', 'B', 'Cd', 'eF']
b = []

def c(array, newArray):
  for str in array:
    newArray.append(str.lower())

c(a, b)
print(b)