# Напишите программу, которая выводит на экран текст «I***like***Python» (без кавычек).

print ("I", "like", "Python", sep="***")


# Напишите программу, которая считывает строку-разделитель и три строки, а затем выводит указанные строки через разделитель.

a=input()
b=input()
c=input()
d=input()

print (b, c, d, sep=a)


# Напишите программу, которая считывает три целых числа и выводит на экран их сумму. Каждое число записано в отдельной строке.

a = int(input())
a += int(input())
a += int(input())
print(a)


# Напишите программу, которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.

a = int(input())
print('Следующее за числом', a, 'число:', a+1)
print('Для числа', a, 'предыдущее число:', a-1)


# Напишите программу, которая считывает целое положительное число xx и выводит на экран последовательность чисел x, 2x, 3x, 4x, 5x, разделённых тремя черточками.

a = int(input())
print(a, a*2, a*3, a*4, a*5, sep='-'*3)


# Напишите программу, которая находит полное число метров по заданному числу сантиметров.

a = int(input())
print(a//100)
