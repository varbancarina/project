profit = float(input("Выручка фирмы "))
costs = float(input("Издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки {profit / costs:.2f}")
    workers = int(input("Количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
