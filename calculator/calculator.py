
print("airchie operacia:")
print("1. mimateba")
print("2. gamokleba")
print("3. gamravleba")
print("4. gayofa")

while True:
    choice = input("airchie (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("sheivane pirveli ricxvi: "))
        num2 = float(input("sheivane meore ricxvi: "))

        if choice == '1':
            print(num1 + num2)

        elif choice == '2':
            print(num1 - num2)

        elif choice == '3':
            print(num1 * num2)

        elif choice == '4':
            if num2 != 0:
                print(num1 / num2)
            else:
                print("Error!")
