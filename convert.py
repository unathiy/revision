def convert_datetime(datetime_input):
    date, time = datetime_input.split()
    year, month, day = date.split('-')
    hour, minute = time.split(':')

    year = "'" + year[-2:]

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    month = months[int(month) - 1]

    hour = int(hour)
    if hour == 0:
        time_suffix = 'am'
        hour = 12
    elif hour < 12:
        time_suffix = 'am'
    elif hour == 12:
        time_suffix = 'pm'
    else:
        time_suffix = 'pm'
        hour -= 12

    day = int(day)
    if 4 <= day <=20 or 24 <= day <= 30:
        day_suffix = 'th'

    else:
        suffixes = ['st', 'nd', 'rd']
        day_suffix = suffixes[(day - 1) % 10]

    long_form = f"{hour}:{minute} {time_suffix} on the {day}{day_suffix} of {month}{year}"

    return long_form

datetime_input = input("Enter the date and time (yyyy-mm-dd hh:mm): ")
long_form_datetime = convert_datetime(datetime_input)

print(long_form_datetime)
