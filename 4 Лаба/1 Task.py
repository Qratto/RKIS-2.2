from random import randint

array = []
for i in range(15):
    array.append(randint(0,100))

for i in array:
    print(i,end=" ")