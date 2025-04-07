import datetime
from datetime import datetime, time

#started_at = datetime.strptime(input('Введите время начала разговора в формате %Y-%m-%d %H:%M:%S: '), "%Y-%m-%d %H:%M:%S")
#ended_at = datetime.strptime(input('Введите время окончания разговора в формате %Y-%m-%d %H:%M:%S: '), "%Y-%m-%d %H:%M:%S")
#price = float(input('Введите стоимость одной секунды разговора: '))

started_at = datetime.strptime('2025-04-06 23:59:50', "%Y-%m-%d %H:%M:%S")
ended_at = datetime.strptime('2025-04-07 00:00:10', "%Y-%m-%d %H:%M:%S")
price = 10

if ended_at.time() > started_at.time():
    duration = (ended_at - started_at).seconds
    if ended_at.weekday() < 5:
        cost = duration * price
    else:
        cost = duration * price * 0.8
else:
    duration_1 = (datetime.combine(ended_at, time.min) - started_at).seconds
    if ended_at.weekday() < 5:
        cost_1 = duration_1 * price
    else:
        cost_1 = duration_1 * price * 0.8
    duration_2 = (ended_at - datetime.combine(ended_at, time.min)).seconds
    if started_at.weekday() < 5:
        cost_2 = duration_2 * price
    else:
        cost_2 = duration_2 * price * 0.8
    cost = cost_1 + cost_2
print(cost)
