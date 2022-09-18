import string
import time

def bubble_sort(array):
    N = len(array)
    for i in range(N - 1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def gnome_sort(array):
    N = len(array)
    index = 0
    while index < N:
        if index == 0:
            index = index + 1
        if array[index] >= array[index - 1]:
            index = index + 1
        else:
            array[index], array[index-1] = array[index-1], array[index]
            index = index - 1

print("Введите имя файла")
file_name = input()
file = open(file_name+".txt","r")
array = file.read()
array = array.split('\n')
array = list(map(int, array)) 
array_copy_bubble = array.copy()
array_copy_gnome = array.copy()
file.close()

print("Сортировка пузырьком")

start_time_bubble = time.perf_counter() 
bubble_sort(array_copy_bubble)
end_time_bubble = time.perf_counter()

print(end_time_bubble - start_time_bubble)

print("Гномья сортировка")

start_time_gnome = time.perf_counter() 
gnome_sort(array_copy_gnome)
end_time_gnome = time.perf_counter() 
print(end_time_gnome - start_time_gnome)

bubble_time = end_time_bubble - start_time_bubble
gnome_time = end_time_gnome - start_time_gnome

file = open(file_name+"_sorted.txt", "w")
N = len(array)
file.write("Bubble_Sort\tGnome_Sort\n"+ str(bubble_time)+"\t"+str(gnome_time)+"\n")
for i in range(N-1):
    file.write(str(array_copy_bubble[i])+"\t\t"+str(array_copy_gnome[i])+"\n")
file.close()