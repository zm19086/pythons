# print('ohayou')
# print('don')
# print('oha')
def washingMachine():
  print('給水します')
  print('洗います')
  print('すすぎます')
  print('脱水します')
  print('乾燥します')

washingMachine()

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