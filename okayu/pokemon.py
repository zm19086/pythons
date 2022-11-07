import random

class pokemon:
  def __init__(self, name, hp, atc, aim, luckyAim):
    self.name = name
    self.hp = hp
    self.atc = atc
    self.lottery = aim
    self.highLottery = luckyAim
    
  def getName(self):
    return self.name
    
  def attack(self):
    return self.atc
  
  def hitPoint(self):
    return self.hp
  
  def aim(self):
    return self.lottery
  
  def luckyAim(self):
    return self.highLottery

# ポケモン名 = pokemon(名前, HP, 攻撃力, 命中割合, 急所に当てる割合)
kodakku = pokemon('コダック', 60, 12, 6, 3)
sonansu = pokemon('ソーナンス', 65, 10, 7, 4)
pikachu = pokemon('ピカチュウ', 50, 15, 5, 1)
mukkuru = pokemon('ムックル', 45, 18, 7, 1)
yadon = pokemon('ヤドン', 58, 11, 8, 6)

pokemonList = [kodakku, sonansu, pikachu, mukkuru, yadon]

# インスタンス化したポケモンの数だけ候補として表示する処理
def msg1():
  print('仲間にしたいポケモンの番号をを入力してください。(半角数字)')
  for i in range(len(pokemonList)):
    print(str(i + 1) + ': ' + pokemonList[i].getName())

def msg2():
  print('戦いたいポケモンの番号をを入力してください。(半角数字)')
  for i in range(len(pokemonList)):
    print(str(i + 1) + ': ' + pokemonList[i].getName())

# 選んだ味方と相手でバトルを開始してもいいのかをユーザに確認してもらう処理
def check():
  result = input('味方は' + myPokemon.getName() + '、相手は' + enemyPokemon.getName() + 'でよろしいですか？\nYES -> y\nNo -> n\n=> ')
  if (str.lower(result) == 'y'):
    print('========================================')
    print('バトルを開始します。')
    print('========================================')
    return True
  elif (str.lower(result) == 'n'):
    print('選び直してください')
    return False
  else:
    print('「y」か「n」を入力してください。')
    return False

# 味方のポケモンをユーザに選んでもらう処理
def selectMyPokemon():
  msg1()
  result = input('=> ')
  
  for i in range(len(pokemonList)):
    if (int(result) == i + 1):
      print('--------------------------------')
      print(str(pokemonList[i].getName()) + 'が仲間になった！')
      print('--------------------------------')
      return pokemonList[i]

# 相手にするポケモンをユーザに選んでもらう処理
def selectEnemyPokemon():
  msg2()
  result = input('=> ')
  
  for i in range(len(pokemonList)):
    if (int(result) == i + 1):
      print('--------------------------------')
      print(str(pokemonList[i].getName()) + 'があらわれた！')
      print('--------------------------------')
      return pokemonList[i]

# 引数に渡された乱数(num)によって「命中」「急所」「不発」を決めて、ダメージ計算結果を返す処理
def attack(num, offense, defense):
  if (num >= offense.aim()):
    result = defense - offense.attack()
    return result
  elif (num >= offense.luckyAim()):
    result = defense - (offense.attack() * 2)
    return result
  else:
    result = defense - 0
    return result

# 引数に渡された乱数(num)によって「命中」「急所」「不発」を決めて、結果に応じたメッセージを表示する処理
def myTurn(num, me, enemy):
  if (num >= me.aim()):
    print(me.getName() + 'は' + enemy.getName() + 'に、' + str(me.attack()) + 'ダメージを あたえた！')
  elif (num >= me.luckyAim()):
    print(me.getName() + 'は' + enemy.getName() + 'に、' + str(me.attack() * 2) + 'ダメージを あたえた！')
    print('きゅうしょ に あたった！')
  else:
    print(myPokemon.getName() + 'は こうげきを はずした！')

def enemyTurn(num, enemy, me):
  if (num >= enemy.aim()):
    print(enemy.getName() + 'は' + me.getName() + 'に、' + str(enemy.attack()) + 'ダメージを あたえた！')
  elif (num >= enemy.luckyAim()):
    print(enemy.getName() + 'は' + me.getName() + 'に、' + str(enemy.attack() * 2) + 'ダメージを あたえた！')
    print('きゅうしょ に あたった！')
  else:
    print(enemyPokemon.getName() + 'は こうげきを はずした！')

# ポケモンバトルを行う処理
def pokemonBattle(me, enemy):
  
  if (check() == True):
  
    myHp = me.hitPoint()
    enemyHp = enemy.hitPoint()
    while (True):
      
      ransu = random.randint(1, 10)
      myTurn(ransu, me, enemy)
      enemyHp = attack(ransu, me, enemyHp)
      if (enemyHp <= 0):
        print(enemy.getName() + 'との しょうぶに かった！')
        break
      
      ransu = random.randint(1, 10)
      enemyTurn(ransu, enemy, me)
      myHp = attack(ransu, enemy, myHp)
      if (myHp <= 0):
        print(enemy.getName() + 'との しょうぶに まけた...')
        break
      
      print(me.getName() + '(' + str(myHp) + ')' + '  ' + enemy.getName() + '(' + str(enemyHp) + ')')
      
  else:
    return


myPokemon = selectMyPokemon()
enemyPokemon = selectEnemyPokemon()
pokemonBattle(myPokemon, enemyPokemon)