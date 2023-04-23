#todo:
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.
import calendar

c = calendar.Calendar(firstweekday=calendar.THURSDAY)

for i in range(1, 13):
    monthcal = c.monthdatescalendar(2023, i)
    all_thursdays = [day for week in monthcal for day in week if day.weekday() == calendar.THURSDAY and day.month == i]
    print(all_thursdays[2])
