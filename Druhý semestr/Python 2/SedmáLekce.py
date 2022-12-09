"""4 funkce.

vrátí aktuální týden v roce (číslo)

vrátí den v týdnu (číslo)

vrátí den v roce (číslo)

vrátí den v měsíci (číslo)"""

import datetime 
import pendulum as p

def weekOfTheYear(date):
    week = date.isocalendar().week
    return week

def dayOfTheWeek(date):
    week = date.isoweekday()
    return week

def dayOfTheYear(date):
    week = date.timetuple().tm_yday
    return week

def dayOfTheMonth(date):
    week = date.day
    return week

print(weekOfTheYear(datetime.date.today()))
print(dayOfTheWeek(datetime.date.today()))
print(dayOfTheYear(datetime.date.today()))
print(dayOfTheMonth(datetime.date.today()))

print(datetime.datetime.now())
now = p.now("Europe/Paris")
print(now.in_timezone("America/Los_Angeles").add(years=14,days=114,microseconds=20))

dur = p.duration(days=14)
print(dur.in_hours())
print(dur.in_seconds())
print(dur.in_weeks())

print(dur.in_words("en"))

cas = p.now().subtract(minutes=15)
print(cas.diff_for_humans(locale="en"))

print(datetime.datetime.now().strftime("dnes je %d. %m. %y, čas je %H:%M"))

ts = 1528797322

print(datetime.datetime.fromtimestamp(ts))

print(datetime.datetime.now().timestamp())

