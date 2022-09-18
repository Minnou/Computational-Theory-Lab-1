import random

print("Введите имя файла")
file_name = input()
print("Введите количество чисел")
length = int(input())

file = open(file_name+".txt","w")
for i in range(length-1):
    file.write(str(random.randint(0,100))+"\n")
file.write(str(random.randint(0,100)))
file.close()