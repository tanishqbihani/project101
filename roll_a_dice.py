import random
response="y"

while response == "y":
    num = random.randint(1, 6)
    if num == 1:
        print("|-----|")
        print("|     |")
        print("|  *  |")
        print("|     |")
        print("|-----|")

    if num == 2:
        print("|-----|")
        print("|  *  |")
        print("|     |")
        print("|  *  |")
        print("|-----|")
  
    if num == 3:
        print("|-----|")
        print("| *   |")
        print("|  *  |")
        print("|   * |")
        print("|-----|")

    if num == 4:
        print("|-----|")
        print("|*   *|")
        print("|     |")
        print("|*   *|")
        print("|-----|")

    if num == 5:
        print("|-----|")
        print("|*   *|")
        print("|  *  |")
        print("|*   *|")
        print("|-----|")

    if num == 6:
        print("|-----|")
        print("|* * *|")
        print("|     |")
        print("|* * *|")
        print("|-----|")

    response=input("Do you want to roll a dice again? (y/n)")
    print("\n")