def fonik():
    say = int(input())
    for x in range(say):
        print("")
        for y in range(say):
            print("*",end=" ")
fonik()
kenaru = int(input())
a = 1
while a <= kenaru:
    b = 1
    while b <= kenaru:
        print("*",end ="")
    a += 1
    b += 1


    def fonik():
        say = int(input())
        for x in range(say):
            print("")
            for y in range(say):
                if x == 0 or y == 0 or x == say - 1 or y == say - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")


    fonik()