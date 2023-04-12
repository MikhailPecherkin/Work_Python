# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

n = int(input("Введите общее количество сделаных журавликов: "))

if n % 6 != 0:
    print("Что то не так с количеством")
else:  
    s = n // 6
    k = 4 * s
    print("Катя сделала ", k, " журавликов")
    print("Петя сделал  ", s, " журавликов")
    print("Серёжа сделал", s, " журавликов")