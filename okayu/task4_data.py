# 4 データ型を理解して使いこなそう sample_folder/dataType.py line1~

# 4-1
# 数値型で「19273」と表示

print(19273)

# 4-2
# 文字列型で「19 + 273」と表示

print('19 + 273')

# 4-3
# 「python」「の練習」を連結して表示

print('python' + 'の練習')

# 4-4
# 「合計」「800」「円のお会計です」を連結して表示

print('合計' + '800' + '円のお会計です')

# 4-5
# 変数 money に数値型で「20000」を代入して、「20000」「円とられた。」を連結して表示 sample_folder/function.py line91~

money = 20000
print(str(money) + '円とられた。')

# 4-6
# 好きな食べ物(3つ)のリストを作って表示

myFavoriteFood = ['卵かけご飯', '肉', '寿司']
print(myFavoriteFood)

# 4-7
# 作ったリストにもう1つ好きな食べ物を追加

myFavoriteFood.append('金平糖')
print(myFavoriteFood)

# 4-8
# ポケモンsvの御三家の名前とタイプを辞書型にして全て表示

pokemon = {'ホゲータ':'ほのお', 'ニャオハ':'くさ', 'クワッス':'みず'}
print(pokemon)

# 4-9
# 4-8で作成した辞書型リストから2番目のポケモンのタイプを取得して表示

print(pokemon['ニャオハ'])
