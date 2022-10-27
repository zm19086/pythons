# 繰り返し処理
# for文
for count in range(3):
  print('繰り返します')
  print(count)

# 文字数分繰り返す
word = 'ninja'
for chara in word:
  print(chara)

# データの数だけ繰り返す
music_list = ['DEATH METAL', 'ROCK', 'ANIME', 'POP']
for music in music_list:
  print('now playing... ' + music)

# キーの数だけ繰り返す
menu = {'ラーメン':500, 'チャーハン':430, '餃子':210}
for order in menu:
  print(order)
  print(menu[order] * 1.10)



# while文
counter = 0
while (counter < 5):
  print(counter)
  counter = counter + 1

# # while文の無限ループ control + C で停止
# counter = 0
# while (counter < 5):
#   print(counter)

while (True):
  print('パンチ')
  print('キック')
  break
  print('必殺奥義')

# break文 処理を中断する
power = 2
while (True):
  print('パンチ')
  print('キック')
  print('必殺奥義')
  power = power - 1
  if (power == 0):
    break

# continue文 処理をスキップする
family = ['ryu-ko', 'mako', 'satsuki']
for kid in family:
  print('おはよう！' + kid)
  print('起床')
  print('朝ごはん')
  continue
  print('学校に出発')
