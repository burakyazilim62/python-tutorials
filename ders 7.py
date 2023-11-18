ilksayi = 0
ikincisayi = 1
toplam = 0

for x in range(8):
    toplam = ilksayi + ikincisayi
    ilksayi = ikincisayi
    ikincisayi = toplam
print(toplam)

for x in range(21,50,3):
    print(x)



liste = [22,25,28,31,34,37,40,43,46,49]
for i in liste:
    print(i)
    if i%3 == 0:
    print(i,"/3")
    if i % 4 == 0:
    print(i,"/4")
    if i % 5 == 0:
    print(i,"/5")
    if i % 6 == 0:
    print(i,"/6")
    else print("none")



butuple = ("muz","elma","armut")
print(butuple)
print(len(butuple))
tuplem = ("karpuz",)
print(type(tuplem))
tuplemm = ("kavun")
print(type(tuplemm))