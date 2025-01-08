T = int(input())
for i in range(T):
    a,b = map(int, input().split())
    money = 0

    if a == 0:
        pass
    elif a<= 1:
        money += 500
    
    elif a<= 3:
        money += 300
    elif a<= 6:
        money += 200
    elif a<= 10:
        money += 50

    elif a<= 15:
        money += 30
    elif a<= 21:
        money += 10

    if b == 0:
        pass
    elif b<= 1:
        money += 512
    
    elif b<= 3:
        money += 256
    elif b<= 7:
        money += 128


    elif b<= 15:
        money += 64
    elif a<= 31:
        money += 32

    print(money*10000)