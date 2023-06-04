num_amount = int(input("Enter amount of elements in list: "))
num_amount_enterd__list = list(map(int, input
      ("Enter elements of the list, use space to divine them: ").split()))
if len(num_amount_enterd__list) != num_amount or num_amount < 1:
    print("Error wrong ammount in the list or massiv is empty")
else:
    x = int(input("Enter number you want to find in the list: "))
    min_difference = abs(x - num_amount_enterd__list[0])
    index = 0
    for i in range(1, num_amount):
        difference_2 = abs(x - num_amount_enterd__list[0])
        if difference_2 < min_difference:
            min_difference = difference_2
            index = i
    print(f''' Number {num_amount_enterd__list[index]} is the nearest to {x}''')

        