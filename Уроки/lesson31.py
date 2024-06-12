from datetime import date, datetime, timedelta
# today = date.today()
# print(today)
# print(today.day)
# print(today.month)
# print(today.year)
# print(today.weekday())


# now = datetime.now()
# now2 = datetime.today()
# print(now,now2,sep='\n')

# now = datetime.now()
# print(now)
# print(now.strftime('%A'))
# print(now.strftime('%A'))
import locale
locale.setlocale(locale.LC_ALL,'ru_RU.UTF-8')
now = datetime.now()
print (now)
print(f'Дата:{now.strftime("%A,%d %b %y")}')
print(f'Время:{now.strftime("%H:%M:%S")}')
now = datetime.today()
print(now.strftime('%c'))
d1 = now + timedelta(days=1, hours=2,minutes=10)
print(d1.strftime(('%c')))

