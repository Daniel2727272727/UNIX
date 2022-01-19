import threading
from time import sleep

total = 100

def proc(n):
    sleep(2)
    global total
    if total >= n:
        total -= n

    print('Reducing ', n,  total)

for i in range(10):
    t1 = threading.Thread(target=proc, args=[15])

    t1.start()


#способ с помощью генератора
#t = [threading.Thread(target=proc, args=[i]) for i in range(10)]
#[t1.start() for t1 in t]

print('Total amount ', total)
