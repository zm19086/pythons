# class
class fruit:
  color = 'red'
  def taste(self):
    return 'delicious'

apple = fruit()
print(apple.color)
print(apple.taste())

# オブジェクト
# オブジェクトとは、データと機能(メソッド)を持つもの
# データ型もデータとメソッドを持っているのでオブジェクト
# クラスもデータ(変数)とメソッド(関数)を持っているのでオブジェクト
color = 'green'
print(color.count('e'))
print(color.upper())

class staff:
  bonus = 30000
  def salary(self):
    salary = 10000 + self.bonus
    return salary

yamamoto = staff()
print(yamamoto.salary())

# 引数の初期値をセットする __init__メソッド
class staff:
  def __init__(self, bonus):
    self.bonus = bonus
  def salary(self):
    salary = 10000 + self.bonus
    return salary

yamamoto = staff(50000)
print(yamamoto.salary())

# クラスを使用してリストからデータを取得する
social_score = {'佐藤':76, '加藤':54, '伊藤':63, '近藤':81, '後藤':72, '安藤':96}
class social_exam:
  def __init__(self, student):
    self.student = student
  def result(self):
    return social_score[self.student]

sato = social_exam('佐藤')
kato = social_exam('加藤')
ito = social_exam('伊藤')
kondo = social_exam('近藤')
ando = social_exam('安藤')

print(sato.result())
print(kato.result())
print(ito.result())
print(kondo.result())
print(ando.result())

# 継承
class animalBaseClass:
  def __init__(self, num):
    self.animallegs = num
  def walk(self):
    print('歩く')
  def cry(self):
    print('なく')
  def getLegsNum(self):
    print(self.animallegs)

class dogClass(animalBaseClass):
  def __init__(self):
    print('犬です')

class catClass(animalBaseClass):
  def __init__(self, num):
    self.animallegs = num
    super().__init__(num)
    print('猫です')
  def cry(self):
    print('にゃー')

class snakeClass(animalBaseClass):
  def __init__(self):
    snakeLegs = 0
    super().__init__(snakeLegs)
    print('蛇です')

wanko = dogClass()
print(wanko.walk())
print(wanko.cry())

chachamaru = catClass(4)
print(chachamaru.walk())
print(chachamaru.cry())
print(chachamaru.getLegsNum())

nyoro = snakeClass()
print(nyoro.getLegsNum())