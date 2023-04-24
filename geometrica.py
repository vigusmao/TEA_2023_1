from random import randint

def jogar_dado():
    return randint(1,6)

def realizar_geometrica():
    count = 0
    while True:
        count += 1
        a = jogar_dado()
        b = jogar_dado()
        c = jogar_dado()
        if a == b == c:
            return count 

def computar_media(repeticoes):
    total = 0
    for _ in range(repeticoes):
        total += realizar_geometrica()
    return total / repeticoes

while True:
    n = int(input("Quantas reps? "))
    if n <= 0:
        break
    print(computar_media(n))





