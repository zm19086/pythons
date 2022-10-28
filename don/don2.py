# def keisan(num, price):
#     result = num * price 
#     return result

# print(keisan(5, 500))

# def area(radius):
#   result = radius * radius * 3.14
#   return result

# print(area(5))

# small = area(5)
# big = area(10)
# print(small)
# print(big)

# class fruit:
#   color = 'red'
#   def taste(self):
#     return 'delicious'

# apple = fruit()
# print(apple.color)
# print(apple.taste())
class staff:
  def __init__(self, num):
      self.bonus = num 
  
  def salary(self):
    salary = 10000 + self.bonus
    return salary

yamamoto = staff(15000)
tanaka = staff(13000)
print(yamamoto.salary())
print(tanaka.salary())