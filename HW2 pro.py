#Задачи на циклы и оператор условия------
#----------------------------------------
# (!!!Подсказка на следующие 5 задач - превратите число в строку, а потом работайте с строкой)
# Задача 6
# Найти сумму цифр числа.

digit=4589
sum=0
for i in str(digit):
    sum=sum+int(i)
print ("Сумма цифр заданного числа=",sum)

# Задача 7
# Найти произведение цифр числа.

digit=4367
mult=1
for i in str(digit):
    mult=mult*int(i)
print ("Произведение цифр заданного числа=",mult)

# Задача 8
# Пользователь должен ввести число. Ваш код должен дать ответ на вопрос: есть ли среди цифр числа 5?
# Если есть, код должен вывексти "Цифра 5 есть в числе", в противном случае вывести: "Цифры 5 нет в числе".

digit=input("Введите любое число:")
for i in digit:
    if int(i)==5:
        print ("Цифра 5 есть в числе")
        break
else:
    print("Цифры 5 нет в числе")

# Задача 9
# Найти максимальную цифру в числе

n=24535468
n_list=list(str(n))
digit_max=max(n_list)
print (digit_max, "- максимальная цифра в числе n")

# Задача 10
# Найти количество цифр 5 в числе

n=4354897886543
fives=0
for i in str(n):
    if i=='5':
        fives+=1
print ('В числе', n,fives,'цифры 5')
