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

myPokemon = kodakku
enemyPokemon = mukkuru

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

def pokemonBattle(me, enemy):
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

pokemonBattle(myPokemon, enemyPokemon)