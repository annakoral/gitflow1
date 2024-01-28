import string

print(string.capwords("делаем первые буквы заглавными в python"))
'''Добавляем новую функцию'''
def capitalize(x):
  for a in x:
    a.capitalize()
  print x

capitalize("heey")