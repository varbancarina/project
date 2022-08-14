a = float(input("Введите результаты пробежки первого дня в км: "))
b = float(input("Введите общий желаемый результат в км: "))
days = 1
print(days, '-й день:', round(a))

while a <= b:
        a = (a*0.1)+a
        days += 1
        print(days, '-й день:', round(a, 2))
else:
        print('на', days, ' день спортсмен достиг результата — не менее', round(a), 'км.')
