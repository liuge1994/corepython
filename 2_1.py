months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] + 7 * ['th'] \
        + ['st']

year = int(input('Year: '))
month = int(input('Month (1-12): '))
day = int(input('Day (1-31): '))
month_name = months[month - 1]
ordinal = str(day) + endings[day - 1]
print(str(month_name) + ' ' + str(ordinal) + ', ' + str(year))