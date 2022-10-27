# pythonのデータ型を扱う

# Int(整数)
34 + 56
print(34 + 56)
number = 55
print(number)



# float(浮動小数点数)
5 + 3.4
print(5 + 3.4)
5 / 2
print(5 / 2)



# complex(複素数)
complex = 5 + 5j
print(complex)
print(complex + (3 + 1j))



# str(文字列型)
'happy birthday!!'
message = "おめでとう！"
print(message)
print('''
一行目
二行目
三行目
n行目
''')
print('thunder' + 'bolt')
print('hunter' * 2)

# 全て大文字にする機能 upperメソッド
text = 'hello'
print(text.upper())
# 全て小文字にする機能 lowerメソッド
text = 'KOMOJI'
print(text.lower())
# 指定した文字の数を数える機能 countメソッド
word = 'maintenance'
print(word.count('n'))



# bool(論理型)
print(46 < 49)
print(46 > 49)



# list(リスト型)
Agroup = ['kazu', 'gorou']
Bgroup = ['syun', 'haruka']
print(Agroup[0])
print(Bgroup[1])

# リストに追加 appendメソッド
Agroup = ['kazu', 'gorou']
Agroup.append('dai')
print(Agroup)

# リストから削除 removeメソッド
Agroup = ['kazu', 'gorou', 'dai']
Agroup.remove('kazu')
print(Agroup)

# リストの要素の順番を変更する sortメソッド
Agroup = ['kazu', 'gorou', 'dai']
Agroup.sort()
print(Agroup)
test_result = [87, 55, 99, 50, 66, 78]
test_result.sort()
print(test_result)



# dict (辞書型)
activities = {'Monday':'バスケ', 'Tuesday':'自転車', 'Wednesday':'軽音', 'Friday':'水泳'}
print(activities)
print(activities['Tuesday'])
print(activities['Friday'])

# 見出し(キー)を全て表示する keysメソッド
print(activities.keys())

# データを全て表示する valuesメソッド
print(activities.values())



# tuple(タプル型)
tuple_sample = ('apple', 3, 90.4)
print(tuple_sample)

# リスト型は書き換えられる (タプル型は書き換えられない -> エラーになる)
flavor_list = ['ミント', 'チョコ', 'ストロベリー', 'バニラ']
flavor_list[0] = 'ラムレーズン'
print(flavor_list)

# タプル型は辞書型のキーとして使える (リスト型はキーに使えない -> エラーになる)
diary = {}
key = ('kamata', '08-01')
diary[key] = '70kg'
print(diary)



# (集合型)
candy = {'delicious', 'fantastic'}
print(candy)

# 重複する文字を一つにまとめて、順番を保存しない集合型を作る　set関数
candy = set('delicious')
print(candy)

# set関数で順番が変わらないようにする方法 -> リスト型にしてからset関数に渡す
flavor = ['apple', 'peach', 'soda']
candy = set(flavor)
print(candy)

# 集合体に新規データを追加する updateメソッド
candy.update(['grape'])
print(candy)

# 重複したデータを削除する
music = ['my_love', 'life', 'life', 'good_time']
music_set = set(music)
print(music_set)
music = list(music_set)
print(music)

# 複数のデータ同士の計算
limited_cd = {'good_day', 'chocolate', 'loyalty'}
normal_cd = {'good_day', 'chocolate'}
print(limited_cd - normal_cd)
print(limited_cd & normal_cd)