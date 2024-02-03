def faktor():
    n = int(input())
    i = 1
    carpim = 1
    while i <= n:
        carpim = carpim * i
        i += 1
while True:
    i = int(input("lutfen bir sayi giriniz"))
    x = 1
    carpanlar = []
    while x <= i:
        if i % x == 0:
            carpanlar.append(x)
        x += 1
    print(carpanlar)
def fonkum(x):
    return 5 * x
print(fonkum(3))
print(fonkum(5))
print(fonkum(9))






