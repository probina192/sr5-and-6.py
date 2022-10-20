dec = int(input("Введите число: "))
r = 0
while (1):
    r=int(input("Введите разрядность: "))
    if (r==2 or r==8):
        break
result=""
hello = dec #изначальное число (для вывода)
while (dec>0):
    result +=str(dec%r) #остаток от деления
    dec//=r #целочисленное деление
reversedResult = result[::-1] 
print ("Вывод: ", hello , "->" , reversedResult)
    
