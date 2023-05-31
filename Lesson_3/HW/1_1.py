num_amount = int(input("Enter amount of elements in list: "))
num_amount_enterd__list = list(map(int, input
      ("Enter elements of the list, use space to divine them: ").split()))
if len(num_amount_enterd__list) != num_amount:
    print("Error wrong ammount in the list.")
else:
    count = 0
    x = int(input("Enter number you want to count in the list: "))
    for i in range(num_amount):
        if num_amount_enterd__list[i] == x:
            count += 1
    print(f'''There are {count}  of {x} in list''' )
