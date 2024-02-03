import math
sayi = int(input())
print(math.factorial(sayi))
print(math.fabs(-5))
print(math.floor(4.7))
print(math.comb(7,2))
print(math.perm(7,2))
import random
hak = 0
sayi = random.randint(1,100)
while hak<7:
    tahmin = int(input())
    if sayi < tahmin:
        print("sayi daha kucuk")
    elif sayi > tahmin:
        print("sayi daha buyuk")

    if sayi == tahmin:
        print("kazandın")
    else:
        print("kaybettin")
    hak += 1
else:
    print("hakkın bitti")
import random
import time
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

hamlebilg=random.randint(1,3)
if hamlebilg == 1:
    print("makas")
elif hamlebilg == 2:
    print("tas")
elif hamlebilg == 3:
    print("kagıt")
hamle = int(input())
if hamle == 1:
    print("makas")
elif hamle == 2:
    print("tas")
elif hamle == 3:
    print("kagıt")
if hamle == 1 and hamlebilg == 1:
    print("berabere")
if hamle == 2 and hamlebilg == 2:
    print("berabere")
if hamle == 3 and hamlebilg == 3:
    print("berabere")
if hamle == 1 and hamlebilg == 2:
    print("bilg kazandı")
if hamle == 2 and hamlebilg == 3:
    print("bilg kazandı")
if hamle == 1 and hamlebilg == 3:
    print("kull kazandı")
if hamle == 2 and hamlebilg == 1:
    print("kull kazandı")
if hamle == 3 and hamlebilg == 1:
    print("bilg kazandı")
if hamle == 3 and hamlebilg == 2:
    print("kull kazandı")