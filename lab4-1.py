import math
#змінює значення двох цілих змінних a і b
a = int(input('Enter 1st number : '))
b = int(input('Enter 2nd number : '))
a,b = b,a
print('Сhange of meaning =', a , b)

print('-----------')

#середнє арифметичне,геометричне двох цілих чисел a і b
a = int(input('Input a = '))
b = int(input('Input b = '))
print('Cереднє арифметичне = ', (a+b)/2)
print('Cереднє геометричне = ', math.sqrt(a*b))

print('-----------')

#переставляє цифри трьохзначного числа у зворотному порядку і виводить нове число на екран

n = int(input('Enter tree-digit number : '))
rev = 0
while(n > 0):
	a = n % 10
	rev = rev * 10 + a
	n = n // 10
print('Reverse of your number is = ', rev)

print('-----------')

#Написати програму, яка визначає загальну кількість годин доби і загальну кількість хвилин доби

sec = int(input('Seconds = '))
seconds = sec
hour = int(sec/3600)
minute = int((sec - (hour * 3600))/60)
print(hour , 'hours , ' , minute, 'minutes.')

print('-----------')

#Написати програму, яка визначає значення кута в градусах (змінна corner) між станом годинникової стрілки на початку доби

print('-----------')

#Написати програму яка визначає чи є натуральне число, що ввів користувач:
x = int(input("Input x: "))
if (x % 2) == 0 :
    print("Number is even")
elif (x % 10 == 5 ):
   print("Last number is ending on 5")

print('-----------')

#Hаписати програму, яка визначає значення цілої змінної,в залежності від того,на який день тижня припадає день  невисокосного року, в якому 1 січня - понеділок

day = int(input('Enter number of a day : '))
days = {1: 'Monday', 2:'Tuesday' , 3: 'Wednesday' , 4: 'Thursday' , 5: 'Friday' , 6: 'Saturday' , 7: 'Sunday'}
print('Your day is - ' , days[int(day % 7)])

print('-----------')

# add task (variant 8)
n = input("Enter a 4-digit number : ")
n = int(n)

d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
d3 = n % 10
n = n // 10
d4 = n % 10
n = n // 10
print("Сумма цифр числа:", d1 + d2 + d3 + d4)



