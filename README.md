# Basic_python_code
for i in range(6):
    if i <= 3:
        n = i
    else:
        n = 6 - i
    print(("ineuron " * n).center(25, " "))

n = 3
for i in range(n - 1):  # 0,1
    for j in range(i, n):  # 1,2
        print(" ", end=" ")

    for j in range(i + 1):
        print("ineuron", end=" ")
    print()
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i, n - 3):
        print("ineuron", end=" ")
    for j in range(i, n):
        print("ineuron", end=" ")
    print()
for i in range(3):
    for j in range(3 - i):
        print(" ", end=" ")
    for j in range(i + 1):
        print("aman", end=" ")
    print()
for i in range(2):
    for j in range(i + 2):
        print(" ", end=" ")
    for j in range(2 - i):
        print("aman", end=" ")
    print()


def fun():
    for i in range(3):  # 0,1,2
        for j in range(3 - i):  # 0,1,2
            print("*", end=" ")
        for j in range(i + 1):
            if i == 0:
                print("*   ", end=" ")
            else:
                print("    ", end=" ")
        for j in range(3 - i):
            print("* ", end=" ")
        print()
    for i in range(2):  # 0,1
        for j in range(i + 2):
            print("*", end=" ")
        for j in range(2 - i):
            print("    ", end=" ")
        for j in range(i + 2):
            print("* ", end=" ")
        print()


print(fun())
for i in range(1, 6):
    if i <= 3:
        n = i
    else:
        n = 6 - i
    print(("ineuron " * n).center(25, " "))
for i in range(1, 4):
    print(("python " * i).center(50, " "))
for i in range(2, 0, -1):
    print(("python " * i).center(50, " "))
for i in range(3):
    for j in range(3 - i):
        print(" ", end=" ")
    for j in range(i + 1):
        print("mEssi", end=" ")

    print()
for i in range(2):
    for j in range(i + 2):
        print(" ", end=" ")
    for j in range(2 - i):
        print("mEssi", end=" ")
    print()
for i in range(6):
    if i <= 3:
        a = i
    else:
        a = 6 - i
    print(("AmAn " * a).center(20, " "))















