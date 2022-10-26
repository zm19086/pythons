# エラーと例外

# print('Hello)
#       ^
# SyntaxError: unterminated string literal (detedted at line 2)

# 例外処理 try: ~ except:
try:
  prin('例外が発生してしまう処理')
except:
  print('例外をキャッチしました')

# 例外をキャッチして変数eにセットし、エラーメッセージを表示する
try:
  prin('a')
except Exception as e:
  print(e)
