import random

class pokemon:
  def __init__(self, name, hp, atc, aim):
    self.name = name
    self.hp = hp
    self.atc = atc
    self.aim = aim
    
  def getName(self):
    return self.name
    
  def attack(self):
    return self.atc
  
  def hitPoint(self):
    return self.hp
  
  def lottery(self):
    return self.aim

class battle(pokemon):
  def __init__(self, myHp, myAtc, enemyHp, enemyAtc):
    self.myHp = myHp
    self.myAtc = myAtc
    self.enemyHp = enemyHp
    self.enemyAtc = enemyAtc
  
  def btl(self):
    atc = self.enemyAtc - self.myAtc
    defense = self.myHp - self.enemyAtc
    return atc, defense

kodakku = pokemon('コダック', 60, 12, 4)
sonansu = pokemon('ソーナンス', 65, 10, 2)
pikachu = pokemon('ピカチュウ', 50, 15, 5)
mukkuru = pokemon('ムックル', 45, 18, 3)
yadon = pokemon('ヤドン', 58, 11, 1)

myPokemon = kodakku
enemyPokemon = mukkuru



msg1 = myPokemon.getName() + 'のこうげき！'
msg2 = enemyPokemon.getName() + 'に、' + str(myPokemon.attack()) + 'ダメージ！'

print(msg1)
print(msg2)