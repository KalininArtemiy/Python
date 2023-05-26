number = int(input())
print(number)
result = 1
i = 1
if number == 0:
  print(1)
else:
  while i <= number:
    result = result * i
    i += 1
print (result)