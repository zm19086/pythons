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

kodakku = pokemon('コダック', 60, 12, 4)
sonansu = pokemon('ソーナンス', 65, 10, 2)
pikachu = pokemon('ピカチュウ', 50, 15, 5)
mukkuru = pokemon('ムックル', 45, 18, 3)
yadon = pokemon('ヤドン', 58, 11, 1)

myPokemon = kodakku
myPokemonHp = kodakku.hitPoint()
myPokemonAtc = kodakku.attack()
enemyPokemon = mukkuru
enemyPokemonHp = mukkuru.hitPoint()
enemyPokemonAtc = mukkuru.attack()

def battle():
  while (myPokemonHp <= 0 or enemyPokemonHp <= 0):
    # 乱数抽選
    # 乱数をもとに条件分岐
    print('a')
    myPokemonHp = myPokemonHp - enemyPokemonAtc
    
    # 乱数抽選
    # 乱数をもとに条件分岐
    print('b')
    enemyPokemonHp = enemyPokemonHp - myPokemonAtc

battle()


