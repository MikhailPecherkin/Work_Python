# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

Sum = int(input("Введите сумму чисел: "))
Pr = int(input("Введите произведение чисел: "))
x = y = 0

if Sum > 2000 or Pr > 1000000:
    print("Петя назвал числа которые выходят за пределы допустимых, даже не надо пытаться подобрать")
else:
    for x in range(1,1001):
        y = Sum - x
        if x <= y and x * y == Pr:
            print("Первое число: ", x, "Второе число: ", y)
            break
        elif x == 1000:
            print("Петя хитрит, нет таких натуральных чисел")
            

