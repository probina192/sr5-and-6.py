from random import randint
def inputmassive ():
    arr=[]
    arrSize=int(input("Введите размерность массива : "))
    while (1):
        f=input("Хотите ввести элемента массива? y/n ")
        if (f=="y" or f=="n"):
            break
        else:
            print ("Необходимо ввести y/n")
    if (f=="y"):
        for i in range (arrSize):
            arr.append (int(input()))
    else:
        for i in range (arrSize):
            arr.append (randint(0,10))
    return arr
print ("Ввод массива A")
arrA = inputmassive ()
print ("Ввод массива B")
arrB = inputmassive ()
print ("Массив А")
print (arrA)
print ("Массив B")
print (arrB)
massive=[]
for i in range (len(arrA)):
    for g in range (len(arrB)):
        if (arrA[i]==arrB[g] and arrA[i] not in massive):
            massive.append (arrA[i])
print ("Результат")
print (massive)
    