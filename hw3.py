from datetime import datetime, timedelta

users = [
    {'name': 'Bill', 'birthday': datetime(1987, 5, 10)},
    {'name': 'Jill', 'birthday': datetime(1990, 2, 20)},
    {'name': 'Kim', 'birthday': datetime(1992, 1, 15)},
    {'name': 'Jan', 'birthday': datetime(1985, 9, 3)},
    {'name': 'Bob', 'birthday': datetime(1982, 12, 31)},
    {'name': 'Mary', 'birthday': datetime(1995, 7, 25)},
    {'name': 'Mike', 'birthday': datetime(1980, 11, 11)}
]


def get_birthdays_per_week(users):
    today = datetime.today()
    next_monday = today + timedelta(days=-today.weekday(), weeks=1)

    weekdays = {}
    for i in range(7):
        weekdays[(next_monday + timedelta(days=i)).strftime('%A')] = []

    for user in users:
        user_birthday = user['birthday'].replace(year=next_monday.year)
        if user_birthday < next_monday:
            user_birthday = user_birthday.replace(year=next_monday.year + 1)
        weekdays[user_birthday.strftime('%A')].append(user['name'])

    for day, users in weekdays.items():
        print(f"{day}: {', '.join(users)}")
