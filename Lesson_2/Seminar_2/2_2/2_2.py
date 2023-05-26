a1 = 0
a2 = 1
target = int(input())
count = 2
if target == a2:
  print(2)
elif target < 1 and target > 0:
  print(1)
elif target < 0:
  print (-1)
else:
  while target > a2:
    a2 = a2+ a1
    a1 = a2 - a1
    count += 1
print (a1)
print (a2)
if target != a2:
  print(-1)
else:
  print(count)
