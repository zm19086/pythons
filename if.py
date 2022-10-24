# 条件分岐(もし〜だったら)
# if文
age = 29
if (18 <= age):
  print('チケットを売る')

age = 15
if (18 <= age):
  print('チケットを売る')

# else文
age = 15
if (18 <= age):
  print('チケットを売る')
else:
  print('チケットを売ることはできません')

# elif文
age = 70
if (60 <= age):
  print('チケットは1000円です')
elif (18 <= age):
  print('チケットは1800円です')
else:
  print('チケットを売ることはできません')

# 条件を工夫する
age = 70
if (18 <= age <= 59):
  print('チケットは1800円です')
elif (60 <= age):
  print('チケットは1000円です')
else:
  print('チケットを売る事はできません')

# ポイントカードと回数割引の判定
pointcard = True
count = 5
if (pointcard == True):
  if (count == 5):
    print('いつもありがとうございます。今回は1000円です')

# 条件を工夫する
pointcard = True
count = 5
if ((pointcard == True) and (count == 5)):
  print('いつもありがとうございます。今回は1000円です')

# 組み合わせる
age = 70
pointcard = True
count = 5
if (age < 18):
  print('チケットを売ることはできません')
elif ((60 <= age) or ((pointcard == True) and (count == 5))):
  print('チケットは1000円です')
else:
  print('チケットは1800円です')
