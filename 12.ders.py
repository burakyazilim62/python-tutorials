def fonksiyon():
    print("merhaba dunya")

fonksiyon()
fonksiyon()

def selamla(meyve):
    print(meyve, "suyu")
selamla(input("istedigin meyveyi gir"))


def fonk(n):
    i = 0
    while i<n:
        print("hello world")
        i += 1

fonk(9)

def topla(a,b,c):
    print("sayıların toplamı:",a+b+c)
a = int(input())
b = int(input())
c = int(input())
topla(a,b,c)
def cikar(a,b):
    print("sayıların cıkarması:",a-b)

cikar(a,b)
def carp(a,b):
    print("sayıların carpımı:",a*b)

carp(a,b)
def bol(a,b):
    print("sayıların bolumu:",a/b)

bol(a,b)
def usal(a,b):
    print("sayıların ussu:",a**b)
usal(a,b)