# 5 条件分岐で結果を変えよう sample_folder/if.py line11~

# 5-1
# 変数 flg = False を定義し、flgがTrueなら「good」、Falseなら「bad」を表示

flg = False
if(flg == True):
  print('good')
else:
  print('bad')

# 5-2
# 16歳未満は購入不可 =>「チケットは売れません」を表示
# 16歳以上かつ、学生証を持っていない場合 =>「チケットは1700円です」を表示
# 16歳以上かつ、学生証を持っていた場合 =>「チケットは1500円です」を表示
# 16歳以上で、学生証を持っているかつ、18時以降の利用なら =>「チケットは1000円です」を表示
# 70歳以上なら =>「チケットは1000円です」を表示
#　----- 以下、参考手順 -----
# 年齢の変数を作り、20を代入する
# 学生証の有無を判定する変数を作り、Trueを代入する
# 時間の変数を作り、19を代入する

age = 20
studentCard = True
time = 19
if(age >= 70 or (age >= 16 and studentCard == True and time > 18)):
  print('チケットは1000円です')
elif(age >= 16):
  if(studentCard == True):
    print('チケットは1500円です')
  else:
    print('チケットは1700円です')
else:
  print('チケットは売れません')