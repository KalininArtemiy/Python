n = int(input('Enter N watermelons: '))
min = float('inf')
max = 1 
for i in range(n):
  a = int(input())
  if a < min:
    min = a
  elif a > max:
    max = a
print (f'''{min} is minimum weight,
{max} is maximum weight''')